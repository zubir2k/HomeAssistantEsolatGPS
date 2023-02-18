# Home Assistant eSolat GPS ![visitors](https://visitor-badge.glitch.me/badge?page_id=zubir2k.homeassistantesolatgps.visitor-badge)
Malaysia Prayer time based on GPS Location using AppDaemon

![logo](https://user-images.githubusercontent.com/1905339/219867109-6aa59585-438f-404f-b015-fd9968e2991f.png)

## Installation
1. copy all files `config\appdaemon\apps`

2. append apps.yaml with the following line

```yaml
esolat_gps:
  module: esolat_gps
  class: EsolatGPS
```

3. Within few seconds, the sensors will be populated based on the person with GPS coordinates.

## Special Thanks
- [HomeAssistantMalaysia](https://www.facebook.com/groups/homeassistantmalaysia)

*You may also try [Adzan Automation](https://github.com/zubir2k/HomeAssistantAdzan)*
