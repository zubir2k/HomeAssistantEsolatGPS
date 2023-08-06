![esolatgps_banner](https://user-images.githubusercontent.com/1905339/223016758-1c0c8058-7375-43d9-bd65-9fc00f48809c.png)\
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Donate](https://img.shields.io/badge/donate-Coffee-yellow.svg)](https://zbrj.ml/buymecoffee)

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

## Installation
1. Download and copy `esolat_gps` to your AppDaemon folder `/config/appdaemon/apps/`.
2. Add below line in `apps.yaml` located in the AppDaemon folder.
3. Done. You will start seeing new sensors that start with `sensor.esolat_`
```yaml
esolat_gps:
  module: esolat_gps
  class: EsolatGPS
```
