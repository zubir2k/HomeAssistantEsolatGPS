# 🕋 Home Assistant eSolat GPS
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Donate](https://img.shields.io/badge/donate-Coffee-yellow.svg)](https://zubirco.de/buymecoffee)
[![Repo](https://img.shields.io/badge/zubir2k-repository-brightgreen?logo=github)](https://zubirco.de/) 

This is an AppDaemon application used in Home Assistant that will create a Prayer Time sensor based on Person's GPS coordinates.
The GPS-based prayer time API is provided by **[Malaysia Prayer Time](https://mpt.i906.my/)**.

Prayer time information are made as sensor attributes with the following format:
- 12 hours (e.g. 6:01 AM)
- 24 hours (e.g. 06:01:00)
- Datetime UTC (e.g. 2023-07-29T22:01:00+00:00)

## Requirements
- Home Assistant 2021.x and above
- [AppDaemon](https://github.com/hassio-addons/addon-appdaemon) Add-On installed 
- Device tracker with GPS coordinates assigned to person entity \
(usually from companion app)

## IMPORTANT
- Since AppDaemon [v0.15.0](https://github.com/hassio-addons/addon-appdaemon/releases/tag/v0.15.0), the location for the addon has been moved out from `/config/appdaemon`. It is now stored in a dedicated `addon_config` folder outside of the `/config` path.
- To continue using the current path `/config/appdaemon`, you need to define the app_dir in your `appdaemon.yaml` file located in the `addon_config`

```yaml
secrets: /homeassistant/secrets.yaml
appdaemon:
  app_dir: /homeassistant/appdaemon/apps
```

## Installation
1. Download and it will install into your AppDaemon App folder `/homeassistant/appdaemon/apps/`.
2. Add below line in `apps.yaml` located in the AppDaemon App folder.
3. Done. You will start seeing new sensors that start with `sensor.esolat_`

```yaml
esolat_gps:
  module: esolat_gps
  class: EsolatGPS
```
