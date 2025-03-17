# ACS712 sensor component for esphome

This is based on https://github.com/RobTillaart/ACS712

~~The code is working on ESP and ACS712-30A.~~

**Current version is WIP. Converting to external component. Not working yet.**

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
    pin: 0
    voltage: 3.3
    adc_bits: 1023
    mv_per_amp: 66
    line_voltage: 220
    noisemV: 43
    current_sensor:
      name: "Amperes"
    power_sensor:
      name: "Watts"


```


