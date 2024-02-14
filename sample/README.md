## Dynamic Prayer Time - Markdown Card

This markdown card will display prayer time based on logged in user. \
Please install this [template](https://github.com/zubir2k/HomeAssistantEsolatGPS/blob/main/sample/esolatnow.yaml) to make the markdown card work.

![image](https://github.com/zubir2k/HomeAssistantEsolatGPS/assets/1905339/3e894bd2-7982-44b9-adbd-024e12a4c3c8)

### Installation

1. Ensure the Appdaemon is working and esolat sensors being created.
2. Enable package by adding this line in your configuration.yaml

```yaml
homeassistant:
  packages: !include_dir_named HAMY/
```

3. Copy the template file [esolatnow.yaml](https://github.com/zubir2k/HomeAssistantEsolatGPS/blob/main/sample/esolatnow.yaml) into the HAMY folder.
4. Restart your Home Assistant
