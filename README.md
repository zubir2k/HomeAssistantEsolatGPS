# Home Assistant eSolat GPS ![visitors](https://visitor-badge.glitch.me/badge?page_id=zubir2k.homeassistantesolatgps.visitor-badge)
Malaysia Prayer time based on GPS Location using AppDaemon

![logo](https://user-images.githubusercontent.com/1905339/219867109-6aa59585-438f-404f-b015-fd9968e2991f.png)

## Requirements
- Home Assistant 2021.x and above
- Device tracker with GPS coordinates assigned to person entity \
(usually from companion app)
- AppDeamon Add-On installed 

![image](https://user-images.githubusercontent.com/1905339/219868909-9a79791d-1d9e-43cb-83de-a968cce6011e.png)

[![Open your Home Assistant instance and show the Supervisor add-on store.](https://my.home-assistant.io/badges/supervisor_store.svg)](https://my.home-assistant.io/redirect/supervisor_store/)

## Installation
1. Copy all files `config\appdaemon\apps`

![image](https://user-images.githubusercontent.com/1905339/219869226-e17cffca-9163-4f14-9d9f-c1631a3fddba.png)

2. Append [apps.yaml](https://github.com/zubir2k/HomeAssistantEsolatGPS/blob/main/appdaemon/apps/apps.yaml) with the following line

```yaml
esolat_gps:
  module: esolat_gps
  class: EsolatGPS
```

3. Within few seconds, the sensors will be populated `sensor.esolat_` based on the person with GPS coordinates.

![image](https://user-images.githubusercontent.com/1905339/219869327-b7995984-fa9a-44dc-aeef-da2b77143809.png)

## Example Use Case
- Send prayer time alert via Push Notification whenever the person is not at Home (otherwise, alert via [Adzan Automation](https://github.com/zubir2k/HomeAssistantAdzan))
- Make a condition that will automatically show the prayer time whenever the person is not at Home
- Below is an example of Markdown card:

![image](https://user-images.githubusercontent.com/1905339/219870342-7498fddf-0893-4e16-a7a0-9daca6b80e6f.png)

```jinja
<table align=center width=100%>
<tr align=center>
  <td>Subuh</td>
  <td>Zohor</td>
  <td>Asar</td>
  <td>Maghrib</td>
  <td>Isyak</td>
</tr>
<tr align=center>
  <td><ha-icon icon="mdi:star-crescent"></ha-icon></td>
  <td><ha-icon icon="mdi:star-crescent"></ha-icon></td>
  <td><ha-icon icon="mdi:star-crescent"></ha-icon></td>
  <td><ha-icon icon="mdi:star-crescent"></ha-icon></td>
  <td><ha-icon icon="mdi:star-crescent"></ha-icon></td>
</tr>

<tr align=center><td>
{%if user == "Zubir" and not is_state("person.zubir", "home")%}
  {{state_attr("sensor.esolat_zubir", "Subuh")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Zohor")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Asar")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Maghrib")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Isyak")}}</td>
  <tr><ha-alert alert-type="info">Location: <b>{{states("sensor.esolat_zubir")}}</b></ha-alert></tr>

{%else%}{{state_attr("sensor.solat_subuh", "12hours")}}</td>
  <td>{{state_attr("sensor.solat_zohor", "12hours")}}</td>
  <td>{{state_attr("sensor.solat_asar", "12hours")}}</td>
  <td>{{state_attr("sensor.solat_maghrib", "12hours")}}</td>
  <td>{{state_attr("sensor.solat_isyak", "12hours")}}</td>
  <tr><ha-alert alert-type="info">Location: <b>Home</b> 🏠</ha-alert></tr>

{%endif%}</tr>
</table>
```

## Special Thanks
- [HomeAssistantMalaysia](https://www.facebook.com/groups/homeassistantmalaysia)
- Saudara [Noorzaini Ilhami](https://github.com/i906) for his [MPT API](https://github.com/MalaysiaPrayerTimes)
- ChatGPT by [OpenAI](https://chat.openai.com/chat)
- Prayer times data by [JAKIM](https://www.e-solat.gov.my/). Geolocation data by [Google](https://www.google.com.my)

*You may also try [Adzan Automation](https://github.com/zubir2k/HomeAssistantAdzan)*
