from __future__ import annotations

from typing import TYPE_CHECKING, Any

from rhasspyclient import RhasspyClient
import voluptuous as vol


from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_SSL
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession 

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.components.tts import TtsAudioType


DEFAULT_PORT = 12101
DEFAULT_HOST = '127.0.0.1'


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_HOST, default=DEFAULT_HOST): cv.string,
    vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
    vol.Optional(CONF_SSL, default=False): cv.boolean,
})


async def async_get_engine(hass: HomeAssistant, conf: dict, discovery_info=None):
    port = conf.get(CONF_PORT)
    host = conf.get(CONF_HOST)
    proto = "https" if conf.get(CONF_SSL) else "http"
    client = RhasspyClient(f"{proto}://{host}:{port}/api", async_get_clientsession(hass))
    return RhasspyTTSProvider(hass, client)


class RhasspyTTSProvider(Provider):

    def __init__(self, hass: HomeAssistant, rhasspy: RhasspyClient) -> None:
        self.hass = hass
        self._rhasspy = rhasspy
        self._rhasspy.tts_url = self._rhasspy.tts_url + "?play=false"
        self.name = "RhasspyTTS"

    @property
    def default_language(self) -> str | None:
        return "en_US"

    @property
    def supported_languages(self) -> list[str] | None:
        return ["en_US"]

    @property
    def default_options(self) -> dict[str, Any] | None:
        return {}

    @property
    def supported_options(self) -> list[str] | None:
        return {}

    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any] | None = None) -> TtsAudioType:
        data = await self._rhasspy.text_to_speech(message)
        return "wav", data
