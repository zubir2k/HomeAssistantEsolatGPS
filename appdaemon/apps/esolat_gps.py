# Malaysia Prayer Time based on GPS Location using AppDaemon
# This script was generated with the assistant from ChatGPT
# Creation date: 18/02/2023; Modified date: 20/02/2023

import appdaemon.plugins.hass.hassapi as hass
import requests
from datetime import datetime, timezone, timedelta

class EsolatGPS(hass.Hass):

    def initialize(self):
        self.url = "https://mpt.i906.my/api/prayer/"
        self.run_every(self.update_sensors, self.datetime(), 15*60)
        self.update_sensors(None)

    def update_sensors(self, kwargs):
        person_entities = self.get_state("person")
        for entity_id, entity_state in person_entities.items():
            latitude = entity_state["attributes"].get("latitude")
            longitude = entity_state["attributes"].get("longitude")
            person_friendly_name = entity_state["attributes"].get("friendly_name")
            person_entity_name = entity_id.split('.')[1]
            sensor_entity_id = f"sensor.esolat_{person_entity_name}"
            sensor_unique_id = sensor_entity_id.split('.')[1]
            sensor_friendly_name = f"{person_friendly_name}'s Prayer Time"
            if latitude is not None and longitude is not None:
                response = requests.get(self.url + f"{latitude},{longitude}")
                data = response.json()["data"]
                prayer_times = {}
                for i, prayer_name in enumerate(["Subuh", "Syuruk", "Zohor", "Asar", "Maghrib", "Isyak"]):
                    yesterday = datetime.now(timezone.utc).date() - timedelta(days=1)
                    prayer_time = data["times"][yesterday.day][i]
                    prayer_times[prayer_name] = self.convert_to_local_12time(prayer_time)
                    prayer_times[f"{prayer_name}_24h"] = self.convert_to_local_24time(prayer_time)
                    prayer_times[f"{prayer_name}_timestamp"] = self.timestamp_to_utc(prayer_time).isoformat()
                    #prayer_times[prayer_name] = self.timestamp_to_utc(prayer_time)
                self.set_state(sensor_entity_id, unique_id=sensor_unique_id, state=data["place"], attributes={"icon": "mdi:account-clock", "source": entity_id, "friendly_name": sensor_friendly_name, "GPS": f"{latitude},{longitude}", **prayer_times})
            else:
                # Remove the sensor if the entity no longer has a GPS coordinate
                if self.entity_exists(sensor_entity_id):
                    self.remove_entity(sensor_entity_id)

    def convert_to_local_12time(self, time):
        return self.timestamp_to_utc(time).strftime("%-I:%M %p")

    def convert_to_local_24time(self, time):
        return self.timestamp_to_utc(time).strftime("%H:%M:%S")

    def timestamp_to_utc(self, timestamp):
        return datetime.fromtimestamp(timestamp)
