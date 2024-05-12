import logging
from dataclasses import dataclass, field
from typing import Any

import speech_recognition as sr

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Queue:
    data: list[bytes] = field(default_factory=list)

    def put(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(0)

    def get(self):
        return b"".join(self.data)

    def flush(self):
        self.data = []

    @property
    def empty(self):
        return len(self.data) == 0

    @property
    def size(self):
        return len(self.data)


@dataclass
class BaseRecorder:
    audio_queue: Queue = Queue()

    def _record(self, source: Any) -> bytes:
        raise NotImplementedError

    def flush(self):
        self.audio_queue.flush()

    @property
    def pending_audio(self):
        return self.audio_queue.get()


@dataclass
class SpeechRecorder(BaseRecorder):
    model: sr.Recognizer = sr.Recognizer()
    microphones: dict[str, sr.Microphone] = field(default_factory=dict)
    sample_rate: int = 16000
    phrase_time_limit: int = 5

    def __post_init__(self):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            self.microphones[name] = sr.Microphone(
                device_index=index,
                sample_rate=self.sample_rate,
            )

    def listen(self, name: str = ""):
        microphone = self.microphones.get(name, None) or sr.Microphone(
            sample_rate=self.sample_rate
        )

        with microphone as source:
            logger.info(f"Listening from {name}")
            audio = self._record(source)
            self.audio_queue.put(audio)
            logger.info("Audio added to queue")

    def _record(self, source: sr.Microphone) -> bytes:
        return self.model.listen(
            source, phrase_time_limit=self.phrase_time_limit
        ).get_raw_data()
