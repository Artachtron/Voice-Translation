import logging
import tempfile
from dataclasses import dataclass

from gtts import gTTS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

language_map = {
    "Français": "fr",
    "English": "en",
    "Deutsch": "de",
    "Español": "es",
    "Hindi": "hi",
}


@dataclass
class BaseSpeaker:
    def speak(self, text: str, language: str) -> str:
        raise NotImplementedError


@dataclass
class GoogleSpeaker(BaseSpeaker):
    def speak(self, text: str, language: str) -> str:
        language = language_map.get(language, "en")
        tts = gTTS(text, lang=language)
        temp_filename: str = ""

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_filename = temp_file.name
            tts.save(temp_filename)

        return temp_filename
