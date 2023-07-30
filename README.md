![esolatgps_banner](https://user-images.githubusercontent.com/1905339/223016758-1c0c8058-7375-43d9-bd65-9fc00f48809c.png)\
![visitors](https://visitor-badge.glitch.me/badge?page_id=zubir2k.homeassistantesolatgps.visitor-badge)
[![Donate](https://img.shields.io/badge/donate-Coffee-yellow.svg)](https://zbrj.ml/buymecoffee)

This is an AppDaemon application used in Home Assistant that will create a Prayer Time sensor based on Person's GPS coordinates.
The GPS-based prayer time API is provided by **[Malaysia Prayer Time](https://mpt.i906.my/)**.

Prayer time information are made as sensor attributes with the following format:
- 12 hours (e.g. 6:01 AM)
- 24 hours (e.g. 06:01:00)
- Datetime UTC (e.g. 2023-07-29T22:01:00+00:00)

## Requirements
- Home Assistant 2021.x and above
- Device tracker with GPS coordinates assigned to person entity \
(usually from companion app)
- Highly Recommended: **[Home Assistant Adzan](https://github.com/zubir2k/HomeAssistantAdzan)** integration
- AppDaemon Add-On installed 

![logo](https://user-images.githubusercontent.com/1905339/219867109-6aa59585-438f-404f-b015-fd9968e2991f.png)

![image](https://user-images.githubusercontent.com/1905339/219868909-9a79791d-1d9e-43cb-83de-a968cce6011e.png)

[![Open your Home Assistant instance and show the Supervisor add-on store.](https://my.home-assistant.io/badges/supervisor_store.svg)](https://my.home-assistant.io/redirect/supervisor_store/)

## Installation
1. Download the files and copy to `config\appdaemon\apps` -- be sure that AppDaemon has been installed.

![image](https://user-images.githubusercontent.com/1905339/219869226-e17cffca-9163-4f14-9d9f-c1631a3fddba.png)

2. If you already have other AppDaemon apps loaded, open the `apps.yaml` and add the following lines and save.

```yaml
esolat_gps:
  module: esolat_gps
  class: EsolatGPS
```

3. Within few seconds, the sensors will be populated `sensor.esolat_` based on the person with GPS coordinates.

![image](https://user-images.githubusercontent.com/1905339/223009818-6e8b483e-a86d-48f7-8f3d-b6fd2035bdae.png)

## Example Use Case
- Send prayer time alert via Push Notification whenever the person is not at Home (otherwise, alert via [Adzan Automation](https://github.com/zubir2k/HomeAssistantAdzan))
- Make a condition that will automatically show the prayer time whenever the person is not at Home
- You may use conditional card to switch entity card showing local and gps based prayer time -- more info [here](https://www.home-assistant.io/dashboards/conditional)\
(sample [here](https://github.com/zubir2k/HomeAssistantEsolatGPS/blob/main/sample-entitycard.yaml))
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
  {{state_attr("sensor.esolat_zubir", "Subuh_12h")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Zohor_12h")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Asar_12h")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Maghrib_12h")}}</td>
  <td>{{state_attr("sensor.esolat_zubir", "Isyak_12h")}}</td>
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
- Prayer times data by [JAKIM](https://www.e-solat.gov.my/). Geolocation data by [Google](https://www.google.com.my)

*You may also try [Adzan Automation](https://github.com/zubir2k/HomeAssistantAdzan)*
