#ifndef ACS712_COMPONENT_H
#define ACS712_COMPONENT_H

#include "esphome.h"
#include "ACS712.h"

namespace esphome {
namespace acs712_component {

class ACS712Sensor : public PollingComponent {
 public:
  ACS712Sensor(uint8_t pin, float voltage, uint16_t adc_bits, float mV_per_amp, float line_voltage)
      : PollingComponent(15000),
        acs_(pin, voltage, adc_bits, mV_per_amp),
        line_voltage_(line_voltage) {}

  void setup() override;
  void update() override;

  void set_noisemV(float noisemV) { acs_.setNoisemV(noisemV); }
  void set_mid_point(uint16_t mid_point) { acs_.setMidPoint(mid_point); }

  Sensor *current_sensor = new Sensor();
  Sensor *power_sensor = new Sensor();

 private:
  ACS712 acs_;
  float line_voltage_;
};

}  // namespace acs712_component
}  // namespace esphome

#endif
