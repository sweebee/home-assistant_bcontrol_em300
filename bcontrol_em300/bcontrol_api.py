from bcontrolpy import BControl
from homeassistant.helpers.aiohttp_client import async_get_clientsession


class EM300Api:
    def __init__(self, hass, host: str, password: str):
        session = async_get_clientsession(hass)
        self._client = BControl(host, password, session=session)
        self.serial = None
        self._login_done = False
        self.host = host

    async def async_get_data(self):
        if not self._login_done:
            await self._client.login()
            self._login_done = True
        raw_data = await self._client.get_data()
        self.serial = raw_data.get("serial", "unknown")
        processed_data = {}
        for key, value in raw_data.items():
            attr_name = (
                key.lower().replace(" ", "_").replace("+", "plus").replace("-", "minus")
            )
            processed_data[attr_name] = value
        processed_data["host"] = self.host
        return processed_data

    async def async_get_serial(self):
        if not self.serial:
            await self.async_get_data()
        return self.serial
