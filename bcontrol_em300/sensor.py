from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.const import (
    UnitOfPower,
    UnitOfEnergy,
    UnitOfElectricPotential,
    UnitOfElectricCurrent,
    UnitOfFrequency,
)
from .const import DOMAIN
from .bcontrol_api import EM300Api


from .const import (
    UNIT_VAR,
    UNIT_KILO_VAR_HOUR,
    UNIT_VOLT_AMPERE,
    UNIT_KILO_VOLT_AMPERE_HOUR,
)

SENSOR_DEFINITIONS = {
    # Gesamtsystem
    "active_powerplus": (
        "Leistung Bezug",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "total_energyplus": (
        "Energie Bezug",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "active_powerminus": (
        "Leistung Einspeisung",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "total_energyminus": (
        "Energie Einspeisung",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "reactive_powerplus": (
        "Blindleistung Bezug",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "reactive_energyplus": (
        "Blindenergie Bezug",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "apparent_powerplus": (
        "Scheinleistung Bezug",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "apparent_energyplus": (
        "Scheinenergie Bezug",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "reactive_powerminus": (
        "Blindleistung Einspeisung",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "reactive_energyminus": (
        "Blindenergie Einspeisung",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "apparent_powerminus": (
        "Scheinleistung Einspeisung",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "apparent_energyminus": (
        "Scheinenergie Einspeisung",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "power_factor": (
        "Leistungsfaktor",
        None,
        SensorDeviceClass.POWER_FACTOR,
        SensorStateClass.MEASUREMENT,
    ),
    "frequency": (
        "Frequenz",
        UnitOfFrequency.HERTZ,
        SensorDeviceClass.FREQUENCY,
        SensorStateClass.MEASUREMENT,
    ),
    # L1
    "l1_active_powerplus": (
        "L1 Leistung Bezug",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_total_energyplus": (
        "L1 Energie Bezug",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l1_active_powerminus": (
        "L1 Leistung Einspeisung",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_total_energyminus": (
        "L1 Energie Einspeisung",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l1_reactive_powerplus": (
        "L1 Blindleistung Bezug",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_reactive_energyplus": (
        "L1 Blindenergie Bezug",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l1_apparent_powerplus": (
        "L1 Scheinleistung Bezug",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_apparent_energyplus": (
        "L1 Scheinenergie Bezug",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l1_reactive_powerminus": (
        "L1 Blindleistung Einspeisung",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_reactive_energyminus": (
        "L1 Blindenergie Einspeisung",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l1_apparent_powerminus": (
        "L1 Scheinleistung Einspeisung",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_apparent_energyminus": (
        "L1 Scheinenergie Einspeisung",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l1_power_factor": (
        "L1 Leistungsfaktor",
        None,
        SensorDeviceClass.POWER_FACTOR,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_voltage": (
        "L1 Spannung",
        UnitOfElectricPotential.VOLT,
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ),
    "l1_current": (
        "L1 Strom",
        UnitOfElectricCurrent.AMPERE,
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ),
    # L2
    "l2_active_powerplus": (
        "L2 Leistung Bezug",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_total_energyplus": (
        "L2 Energie Bezug",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l2_active_powerminus": (
        "L2 Leistung Einspeisung",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_total_energyminus": (
        "L2 Energie Einspeisung",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l2_reactive_powerplus": (
        "L2 Blindleistung Bezug",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_reactive_energyplus": (
        "L2 Blindenergie Bezug",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l2_apparent_powerplus": (
        "L2 Scheinleistung Bezug",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_apparent_energyplus": (
        "L2 Scheinenergie Bezug",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l2_reactive_powerminus": (
        "L2 Blindleistung Einspeisung",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_reactive_energyminus": (
        "L2 Blindenergie Einspeisung",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l2_apparent_powerminus": (
        "L2 Scheinleistung Einspeisung",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_apparent_energyminus": (
        "L2 Scheinenergie Einspeisung",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l2_power_factor": (
        "L2 Leistungsfaktor",
        None,
        SensorDeviceClass.POWER_FACTOR,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_voltage": (
        "L2 Spannung",
        UnitOfElectricPotential.VOLT,
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ),
    "l2_current": (
        "L2 Strom",
        UnitOfElectricCurrent.AMPERE,
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ),
    # L3
    "l3_active_powerplus": (
        "L3 Leistung Bezug",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_total_energyplus": (
        "L3 Energie Bezug",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l3_active_powerminus": (
        "L3 Leistung Einspeisung",
        UnitOfPower.WATT,
        SensorDeviceClass.POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_total_energyminus": (
        "L3 Energie Einspeisung",
        UnitOfEnergy.WATT_HOUR,
        SensorDeviceClass.ENERGY,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l3_reactive_powerplus": (
        "L3 Blindleistung Bezug",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_reactive_energyplus": (
        "L3 Blindenergie Bezug",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l3_apparent_powerplus": (
        "L3 Scheinleistung Bezug",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_apparent_energyplus": (
        "L3 Scheinenergie Bezug",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l3_reactive_powerminus": (
        "L3 Blindleistung Einspeisung",
        UNIT_VAR,
        SensorDeviceClass.REACTIVE_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_reactive_energyminus": (
        "L3 Blindenergie Einspeisung",
        UNIT_KILO_VAR_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l3_apparent_powerminus": (
        "L3 Scheinleistung Einspeisung",
        UNIT_VOLT_AMPERE,
        SensorDeviceClass.APPARENT_POWER,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_apparent_energyminus": (
        "L3 Scheinenergie Einspeisung",
        UNIT_KILO_VOLT_AMPERE_HOUR,
        None,
        SensorStateClass.TOTAL_INCREASING,
    ),
    "l3_power_factor": (
        "L3 Leistungsfaktor",
        None,
        SensorDeviceClass.POWER_FACTOR,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_voltage": (
        "L3 Spannung",
        UnitOfElectricPotential.VOLT,
        SensorDeviceClass.VOLTAGE,
        SensorStateClass.MEASUREMENT,
    ),
    "l3_current": (
        "L3 Strom",
        UnitOfElectricCurrent.AMPERE,
        SensorDeviceClass.CURRENT,
        SensorStateClass.MEASUREMENT,
    ),
}


async def async_setup_entry(hass, entry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]
    api = data["api"]

    serial = api.serial or "unbekannt"

    entities = []
    for key, (name, unit, device_class, state_class) in SENSOR_DEFINITIONS.items():
        if key in coordinator.data:
            entities.append(
                EM300Sensor(
                    coordinator,
                    key=key,
                    name=name,
                    unit=unit,
                    device_class=device_class,
                    state_class=state_class,
                    serial=serial,
                )
            )

    async_add_entities(entities)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    host = config.get("host")
    password = config.get("password")
    if not host or not password:
        return

    api = EM300Api(host, password)
    data = await api.async_get_data()
    serial = api.serial or "unbekannt"

    class DummyCoordinator:
        def __init__(self, data):
            self.data = data

    coordinator = DummyCoordinator(data)

    entities = []
    for key, (name, unit, device_class, state_class) in SENSOR_DEFINITIONS.items():
        if key in data:
            entities.append(
                EM300Sensor(
                    coordinator,
                    key=key,
                    name=name,
                    unit=unit,
                    device_class=device_class,
                    state_class=state_class,
                    serial=serial,
                )
            )

    async_add_entities(entities)


class EM300Sensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, key, name, unit, device_class, state_class, serial):
        super().__init__(coordinator)
        self._key = key
        self._attr_name = f"EM300 {name}"
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = device_class
        self._attr_state_class = state_class
        self._serial = serial

    @property
    def unique_id(self):
        return f"em300_{self._serial}_{self._key}"

    @property
    def native_value(self):
        return self.coordinator.data.get(self._key)

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._serial)},
            "name": "B-Control EM300",
            "manufacturer": "TQ-Systems",
            "model": "EM300",
            "sw_version": self.coordinator.data.get("firmware"),
            "serial_number": self._serial,
            "configuration_url": f"http://{self.coordinator.data.get('host', '0.0.0.0')}",
        }
