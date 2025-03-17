import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID, CONF_PIN, CONF_VOLTAGE, UNIT_AMPERE, UNIT_WATT,
    ICON_CURRENT_AC, ICON_FLASH, DEVICE_CLASS_CURRENT, DEVICE_CLASS_POWER
)

DEPENDENCIES = []
MULTI_CONF = True

CONF_ADC_BITS = 'adc_bits'
CONF_MV_PER_AMP = 'mv_per_amp'
CONF_LINE_VOLTAGE = 'line_voltage'
CONF_NOISE_MV = 'noisemV'
CONF_MID_POINT = 'mid_point'

acs712_ns = cg.esphome_ns.namespace('acs712_component')
ACS712Sensor = acs712_ns.class_('ACS712Sensor', cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ACS712Sensor),
    cv.Required(CONF_PIN): cv.int_,
    cv.Required(CONF_VOLTAGE): cv.float_,
    cv.Required(CONF_ADC_BITS): cv.int_,
    cv.Required(CONF_MV_PER_AMP): cv.float_,
    cv.Required(CONF_LINE_VOLTAGE): cv.float_,
    cv.Optional(CONF_NOISE_MV, default=43): cv.float_,
    cv.Optional(CONF_MID_POINT): cv.int_,
}).extend(cv.polling_component_schema('15s'))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_PIN], config[CONF_VOLTAGE],
                           config[CONF_ADC_BITS], config[CONF_MV_PER_AMP], config[CONF_LINE_VOLTAGE])
    await cg.register_component(var, config)
    if CONF_NOISE_MV in config:
        cg.add(var.set_noisemV(config[CONF_NOISE_MV]))
    if CONF_MID_POINT in config:
        cg.add(var.set_mid_point(config[CONF_MID_POINT]))

    # Configuración de los sensores de corriente y potencia
    current_sensor = sensor.Sensor.new_sensor({
        'name': 'Amperes',
        'unit_of_measurement': UNIT_AMPERE,
        'icon': ICON_CURRENT_AC,
        'device_class': DEVICE_CLASS_CURRENT,
        'accuracy_decimals': 2,
    })
    cg.add(var.current_sensor.set_parent(current_sensor))
    await sensor.register_sensor(current_sensor, var.current_sensor)

    power_sensor = sensor.Sensor.new_sensor({
        'name': 'Watts',
        'unit_of_measurement': UNIT_WATT,
        'icon': ICON_FLASH,
        'device_class': DEVICE_CLASS_POWER,
        'accuracy_decimals': 2,
    })
    cg.add(var.power_sensor.set_parent(power_sensor))
    await sensor.register_sensor(power_sensor, var.power_sensor)
