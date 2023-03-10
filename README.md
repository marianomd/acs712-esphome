# ACS712 sensor component for esphome

This is based on https://github.com/RobTillaart/ACS712

Refer to that README to initialize ACS object correctly.

The code is working on esp and ACS712-30A.

Watts estimation is done with a 220V supposed voltage.

Have in mind that without voltage divider on the ADC pin a 30A model will measure up to 20A.

Example yaml fragment:

```
esphome:
  name: tanque-agua
  friendly_name: tanque-agua
  libraries:
    - https://github.com/RobTillaart/ACS712.git
  includes:
    - acs712_component.h
  
```


