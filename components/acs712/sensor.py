import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID, CONF_PIN, CONF_VOLTAGE, UNIT_AMPERE, UNIT_WATT,
    ICON_CURRENT_AC, ICON_FLASH, DEVICE_CLASS_CURRENT, DEVICE_CLASS_POWER
)

# Agregamos la dependencia a la biblioteca ACS712
cg.add_library(
    name="ACS712",
    repository="https://github.com/RobTillaart/ACS712.git",
    version=">=0.3.0"
)

DEPENDENCIES = []
#MULTI_CONF = True

# Nombres de los nuevos campos para los sensores hijos
CONF_CURRENT_SENSOR = "current_sensor"
CONF_POWER_SENSOR = "power_sensor"

# Constantes de configuración originales
CONF_ADC_BITS = "adc_bits"
CONF_MV_PER_AMP = "mv_per_amp"
CONF_LINE_VOLTAGE = "line_voltage"
CONF_NOISE_MV = "noisemV"
CONF_MID_POINT = "mid_point"

# Define el namespace sin puntos
acs712_ns = cg.esphome_ns.namespace("acs712")
ACS712Sensor = acs712_ns.class_("ACS712Sensor", cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ACS712Sensor),
    cv.Required(CONF_PIN): cv.int_,
    cv.Required(CONF_VOLTAGE): cv.float_,
    cv.Required(CONF_ADC_BITS): cv.int_,
    cv.Required(CONF_MV_PER_AMP): cv.float_,
    cv.Required(CONF_LINE_VOLTAGE): cv.float_,
    cv.Optional(CONF_NOISE_MV, default=43): cv.float_,
    cv.Optional(CONF_MID_POINT): cv.int_,
    # Se definen los schemas para los sensores internos
    cv.Optional(CONF_CURRENT_SENSOR): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=2,
            device_class=DEVICE_CLASS_CURRENT,
            icon=ICON_CURRENT_AC,
    ),
    cv.Optional(CONF_POWER_SENSOR): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            accuracy_decimals=2,
            device_class=DEVICE_CLASS_POWER,
            icon=ICON_FLASH,
    ),
}).extend(cv.polling_component_schema("15s"))

async def to_code(config):
    var = cg.new_Pvariable(
        config[CONF_ID],
        config[CONF_PIN],
        config[CONF_VOLTAGE],
        config[CONF_ADC_BITS],
        config[CONF_MV_PER_AMP],
        config[CONF_LINE_VOLTAGE]
    )
    await cg.register_component(var, config)
    if CONF_NOISE_MV in config:
        cg.add(var.set_noisemV(config[CONF_NOISE_MV]))
    if CONF_MID_POINT in config:
        cg.add(var.set_mid_point(config[CONF_MID_POINT]))
    
    # Registra el sensor de corriente (amperes) si se ha definido en el YAML
    if CONF_CURRENT_SENSOR in config:
        current_sensor = await sensor.new_sensor(config[CONF_CURRENT_SENSOR])
        cg.add(var.set_current_sensor(current_sensor))
    
    # Registra el sensor de potencia (watts) si se ha definido en el YAML
    if CONF_POWER_SENSOR in config:
        power_sensor = await sensor.new_sensor(config[CONF_POWER_SENSOR])
        cg.add(var.set_power_sensor(power_sensor))
