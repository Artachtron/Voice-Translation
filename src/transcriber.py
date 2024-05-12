import logging
from dataclasses import dataclass, field
from typing import Any

import numpy as np
from faster_whisper import WhisperModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class BaseTranscriber:
    def transcribe(self, data: bytes, source_language: str | None = None) -> str:
        raise NotImplementedError

    def _process_audio(self, audio: Any) -> Any:
        raise NotImplementedError


@dataclass
class WhisperTranscriber(BaseTranscriber):
    model: WhisperModel = field(init=False)
    beam_size: int = 5
    chunk_length: int = 20

    def __post_init__(self):
        self.model = WhisperModel(
            model_size_or_path="tiny", device="cpu", cpu_threads=8, compute_type="int8"
        )

    def _process_audio(self, audio: bytes) -> np.ndarray:
        return np.frombuffer(audio, np.int16).flatten().astype(np.float32) / 32768.0

    # TODO: Log the language of the transcription with the transcription
    def transcribe(self, data: bytes | str, source_language: str | None = None) -> str:
        processed_data: str | np.ndarray

        if isinstance(data, bytes):
            processed_data = self._process_audio(data)

        elif isinstance(data, str):
            processed_data = data

        segments, info = self.model.transcribe(
            processed_data,
            beam_size=self.beam_size,
            chunk_length=self.chunk_length,
        )

        return " ".join((segment.text for segment in segments)), info.language
