#include "acs712_component.h"

namespace esphome {
namespace acs712 {

void ACS712Sensor::setup() {
  acs_.autoMidPoint();
  ESP_LOGD("acs712", "MidPoint: %d", acs_.getMidPoint());
}

void ACS712Sensor::update() {
  float average = 0;
  int count = 1;
  for (int i = 0; i < count; i++) {
    average += acs_.mA_AC();
  }
  float amps = average / count / 1000.0;
  current_sensor->publish_state(amps);
  power_sensor->publish_state(amps * line_voltage_);
}

}  // namespace acs712
}  // namespace esphome
