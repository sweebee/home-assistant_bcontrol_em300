from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, PLATFORMS, CONF_SCAN_INTERVAL
from .bcontrol_api import EM300Api
import logging

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    host = entry.data["host"]
    password = entry.data["password"]
    scan_interval = entry.options.get(CONF_SCAN_INTERVAL, 60)

    api = EM300Api(hass, host, password)

    async def async_update_data():
        try:
            return await api.async_get_data()
        except Exception as err:
            raise UpdateFailed(f"Fehler beim Abrufen der EM300-Daten: {err}") from err

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="bcontrol_em300",
        update_method=async_update_data,
        update_interval=timedelta(seconds=scan_interval),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "coordinator": coordinator,
        "api": api,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass, entry):
    await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
