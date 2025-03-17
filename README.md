# ACS712 sensor component for esphome

This is based on https://github.com/RobTillaart/ACS712

Refer to that README to initialize ACS object correctly.

The code is working on esp and ACS712-30A.

Watts estimation is done with a 220V supposed voltage.

Have in mind that without voltage divider on the ADC pin a 30A model will measure up to 20A.

Example yaml fragment:

```
esphome:
  name: tanque_agua

external_components:
  - source:
      type: git
      url: https://github.com/marianomd/acs712-esphome
    components: [acs712]

sensor:
  - platform: acs712
    id: acs712_sensor
    pin: A0
    voltage: 3.3
    adc_bits: 1023
    mv_per_amp: 66
    line_voltage: 220
    noisemV: 43


```


