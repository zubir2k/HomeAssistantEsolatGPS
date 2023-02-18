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

## Special Thanks
- [HomeAssistantMalaysia](https://www.facebook.com/groups/homeassistantmalaysia)
- [Malaysia Prayer Time](https://github.com/MalaysiaPrayerTimes)
- Prayer times data by [JAKIM](https://www.e-solat.gov.my/). Geolocation data by [Google](https://www.google.com.my)

*You may also try [Adzan Automation](https://github.com/zubir2k/HomeAssistantAdzan)*
