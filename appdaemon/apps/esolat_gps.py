# Malaysia Prayer Time based on GPS Location using AppDaemon
# This script was generated with the assistant from ChatGPT
# Creation date: 18/02/2023

import appdaemon.plugins.hass.hassapi as hass
import requests
from datetime import datetime, timezone, timedelta

class EsolatGPS(hass.Hass):

    def initialize(self):
        self.url = "https://mpt.i906.my/api/prayer/"
        self.run_every(self.update_sensors, self.datetime(), 60*60)
        self.update_sensors(None)

    def update_sensors(self, kwargs):
        person_entities = self.get_state("person")
        for entity_id, entity_state in person_entities.items():
            latitude = entity_state["attributes"].get("latitude")
            longitude = entity_state["attributes"].get("longitude")
            if latitude is not None and longitude is not None:
                response = requests.get(self.url + f"{latitude},{longitude}")
                data = response.json()["data"]
                prayer_times = {}
                for i, prayer_name in enumerate(["Subuh", "Syuruk", "Zohor", "Asar", "Maghrib", "Isyak"]):
                    yesterday = datetime.now(timezone.utc).date() - timedelta(days=1)
                    prayer_time = data["times"][yesterday.day-1][i]
                    prayer_times[prayer_name] = self.convert_to_local_time(prayer_time)
                person_entity_name = entity_id.split('.')[1]
                sensor_entity_id = f"sensor.esolat_{person_entity_name}"
                sensor_unique_id = f"esolat_{person_entity_name}"
                sensor_friendly_name = f"{person_entity_name}'s esolatGPS"
                self.set_state(sensor_entity_id, state=data["place"], attributes={"friendly_name": sensor_friendly_name, "unique_id": sensor_unique_id, "GPS": f"{latitude},{longitude}", **prayer_times})
            else:
                # Remove the sensor if the entity no longer has a GPS coordinate
                sensor_entity_id = f"sensor.esolat_{entity_id}"
                if self.entity_exists(sensor_entity_id):
                    self.remove_entity(sensor_entity_id)

    def convert_to_local_time(self, time):
        return self.timestamp_to_utc(time).strftime("%-I:%M %p")

    def timestamp_to_utc(self, timestamp):
        return datetime.fromtimestamp(timestamp)
