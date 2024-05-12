import yaml
from pydantic_settings import BaseSettings

from config.utils import PATH


class Settings(BaseSettings):
    def __init__(self, **data):
        with open(PATH.CONF_DIR / self.__yaml_file__) as file:
            data = yaml.safe_load(file)
        super().__init__(**data)


class HuggingFaceSettings(Settings):
    __yaml_file__ = "huggingface.yaml"
    token: str
    transcription: str
    translation: str


hugging_face = HuggingFaceSettings()
