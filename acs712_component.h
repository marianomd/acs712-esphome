#include "ACS712.h"

class ACS712Sensor : public PollingComponent {
   public:
    ACS712 *ACS = new ACS712(A0, 3.3, 1023, 66);
    Sensor *current_sensor = new Sensor();
    Sensor *power_sensor = new Sensor();

    ACS712Sensor() : PollingComponent(15000) {}

    void setup() override {
        ACS->autoMidPoint();
        ESP_LOGD("acs712", "MidPoint: %d", ACS->getMidPoint());
        ACS->setNoisemV(43);
        ESP_LOGD("acs712", "Noise mV: %d", ACS->getNoisemV());
    }

    void update() override {
        float average = 0;
        //uint32_t start = millis();
        int count = 5;
        for (int i = 0; i < count; i++) {
            average += ACS->mA_AC();
        }
        float amps = average / count / 1000.0;
        // float mA = ACS.mA_AC(50,10);
        //uint32_t duration = millis() - start;

        //ESP_LOGD("acs712", "Time: %d A: ", duration, amps);

        current_sensor->publish_state(amps);
        power_sensor->publish_state(amps * 220);
    }
};