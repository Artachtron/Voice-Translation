import logging
from dataclasses import dataclass

from huggingface_hub import InferenceClient

from config.conf import hugging_face

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class BaseTranslator:

    def translate(self, text: str, source_language: str, target_language: str) -> str:
        raise NotImplementedError


@dataclass
class HuggingFaceTranslator(BaseTranslator):
    client: InferenceClient = InferenceClient(token=hugging_face.token)
    model: str = hugging_face.translation

    def translate(self, text: str, source_language: str, target_language: str) -> str:
        return self.client.translation(
            text,
            src_lang=source_language,
            tgt_lang=target_language,
            model=self.model,
        )
