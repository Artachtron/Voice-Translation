import logging
import threading
from dataclasses import dataclass

from recorder import BaseRecorder, SpeechRecorder
from speaker import BaseSpeaker, GoogleSpeaker
from transcriber import BaseTranscriber, WhisperTranscriber
from translation import BaseTranslator, HuggingFaceTranslator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Assistant:
    transcriber: BaseTranscriber = WhisperTranscriber()
    translator: BaseTranslator = HuggingFaceTranslator()
    recorder: BaseRecorder = SpeechRecorder()
    speaker: BaseSpeaker = GoogleSpeaker()

    stop_requested: threading.Event = threading.Event()

    def _is_sentence(self, text: str):
        delimiters = [".", "?", "!", ","]

        return any((delimiter in text for delimiter in delimiters))

    def run(self):
        while not self.stop_requested.is_set():
            self.recorder.listen()

    def stop(self):
        self.stop_requested.set()

    def transcribe(self, audio: bytes):
        return self.transcriber.transcribe(audio)

    def translate(self, text: str, source_language: str, target_language: str):
        return self.translator.translate(text, source_language, target_language)

    def speech2translation(self, source_language: str, target_language: str):
        audio = self.recorder.pending_audio
        text = self.transcriber.transcribe(audio)

        if text:
            logger.info(f"Translating: {text}")
            translation = self.translator.translate(
                text, source_language, target_language
            )
            logger.info(f"Translation: {translation}")

            self.recorder.flush()

    def text2speech(self, text: str, language: str):
        return self.speaker.speak(text, language)

    def speak(self, text: str, language: str):
        return self.text2speech(text, language)
