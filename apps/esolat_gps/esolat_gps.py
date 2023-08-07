# Malaysia Prayer Time based on GPS Location using AppDaemon
# Creation date: 18/02/2023; Modified date: 06/08/2023
# Changes: Added logger and restructure repository to HACS standard.

import appdaemon.plugins.hass.hassapi as hass
import requests
import pytz
from datetime import datetime, timezone, timedelta

class EsolatGPS(hass.Hass):

    def initialize(self):
        self.url = "https://mpt.i906.my/api/prayer/"
        self.geo = "https://nominatim.openstreetmap.org/reverse?format=json&"
        self.run_every(self.update_sensors, self.datetime(), 15*60)
        self.update_sensors(None)
        self.log("*** Prayer Time sensors updated.")

    def update_sensors(self, kwargs):
        # Prayer Time Sensor for ALL Person Entities
        person_entities = self.get_state("person")
        for entity_id, entity_state in person_entities.items():
            latitude = entity_state["attributes"].get("latitude")
            longitude = entity_state["attributes"].get("longitude")
            person_friendly_name = entity_state["attributes"].get("friendly_name")
            person_entity_name = entity_id.split('.')[1]
            person_icon = "mdi:account-clock"
            sensor_entity_id = f"sensor.esolat_{person_entity_name}"
            sensor_unique_id = sensor_entity_id.split('.')[1]
            sensor_friendly_name = f"{person_friendly_name}'s Prayer Time"
            if latitude is not None and longitude is not None:
                self.update_prayer_time(sensor_entity_id, sensor_unique_id, sensor_friendly_name, person_icon, latitude, longitude, entity_id)
            else:
                # Remove the sensor if the entity no longer has a GPS coordinate
                if self.entity_exists(sensor_entity_id):
                    self.remove_entity(sensor_entity_id)
                    self.log(f"*** REMOVING {sensor_entity_id} due to no longer having GPS coordinates.")
            
        # Prayer Time Sensor for Home
        home_latitude = self.get_state("zone.home", attribute="latitude")
        home_longitude = self.get_state("zone.home", attribute="longitude")
        home_icon = "mdi:home-clock"
        self.update_prayer_time("sensor.esolat_home", "esolat_home", "Home Prayer Time", home_icon, home_latitude, home_longitude, "zone.home")

    def update_prayer_time(self, sensor_entity_id, sensor_unique_id, sensor_friendly_name, sensor_icon, latitude, longitude, prayer_entity_id):
        response = requests.get(self.url + f"{latitude},{longitude}")
        if response.status_code == 404:
            # Set the sensor state to "Outside Malaysia" if the API response has a 404 status code and obtain location as attribute
            geo = requests.get(self.geo + f"lat={latitude}&lon={longitude}")
            geodata = geo.json()["address"]
            geostate = geodata["state"]
            geocountry = geodata["country_code"].upper()
            self.set_state(sensor_entity_id, replace=True, unique_id=sensor_unique_id, state="Outside Malaysia", attributes={"icon": sensor_icon, "source": prayer_entity_id, "friendly_name": sensor_friendly_name, "location": f"{geostate}, {geocountry}", "gps": f"{latitude},{longitude}"})
            #self.log(f"*** Sensors updated for {sensor_friendly_name} (Outside Malaysia)")
        elif response.status_code == 200:
            data = response.json()["data"]
            prayer_times = {}
            for i, prayer_name in enumerate(["Subuh", "Syuruk", "Zohor", "Asar", "Maghrib", "Isyak"]):
                yesterday = datetime.now(timezone.utc).date() - timedelta(days=1)
                prayer_time = data["times"][yesterday.day][i]
                prayer_times[prayer_name.lower()] = self.timestamp_to_utc(prayer_time).astimezone(pytz.utc).isoformat()
                prayer_times[(f"{prayer_name}_12h").lower()] = self.convert_to_local_12time(prayer_time)
                prayer_times[(f"{prayer_name}_24h").lower()] = self.convert_to_local_24time(prayer_time)
            self.set_state(sensor_entity_id, replace=True, unique_id=sensor_unique_id, state=data["place"], attributes={"icon": sensor_icon, "source": prayer_entity_id, "friendly_name": sensor_friendly_name, "gps": f"{latitude},{longitude}", **prayer_times})
            #self.log(f"*** Sensors updated for {sensor_friendly_name} ({data['place']})")
        else:
            self.set_state(sensor_entity_id, replace=True, unique_id=sensor_unique_id, state=f"unavailable", attributes={"icon": sensor_icon, "source": prayer_entity_id, "friendly_name": sensor_friendly_name, "location": f"ERROR CODE:{response.status_code}", "gps": f"{latitude},{longitude}"})
            self.log(f"API Response for {sensor_friendly_name} -- {response.json()}")
            
    def convert_to_local_12time(self, time):
        return self.timestamp_to_utc(time).strftime("%-I:%M %p")

    def convert_to_local_24time(self, time):
        return self.timestamp_to_utc(time).strftime("%H:%M:%S")

    def timestamp_to_utc(self, timestamp):
        return datetime.fromtimestamp(timestamp)
