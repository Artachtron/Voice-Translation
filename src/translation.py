import logging
from dataclasses import dataclass

from huggingface_hub import InferenceClient

from config.conf import hugging_face

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

target_language_map = {
    "Français": "fr_XX",
    "English": "en_XX",
    "Deutsch": "de_DE",
    "Español": "es_XX",
    "Hindi": "hi_IN",
}

source_language_map = {
    "fr": "fr_XX",
    "en": "en_XX",
    "de": "de_DE",
    "es": "es_XX",
    "hi": "hi_IN",
}


@dataclass
class BaseTranslator:

    def translate(self, text: str, source_language: str, target_language: str) -> str:
        raise NotImplementedError


@dataclass
class HuggingFaceTranslator(BaseTranslator):
    client: InferenceClient = InferenceClient(token=hugging_face.token)
    model: str = hugging_face.translation

    def translate(self, text: str, source_language: str, target_language: str) -> str:
        target_language = target_language_map.get(target_language, "fr_XX")
        source_language = source_language_map.get(source_language, "en_XX")
        logger.info(f"Source: {source_language}, Target: {target_language}")

        return self.client.translation(
            text,
            src_lang=source_language,
            tgt_lang=target_language,
            model=self.model,
        )
