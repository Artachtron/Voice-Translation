import gradio as gr
import numpy as np

from assistant import Assistant

assistant = Assistant()


def speech_to_text(speech, target_language="Français"):
    text, source_language = assistant.transcribe(speech)
    translation = assistant.translate(
        text, source_language=source_language, target_language=target_language
    ).translation_text

    translation_speech = assistant.text2speech(translation, language=target_language)

    return translation, translation_speech


demo = gr.Blocks()

with demo:
    audio_file = gr.Audio(type="filepath")
    language_selection = gr.Dropdown(
        choices=["Français", "English", "Deutsch", "Español", "Hindi"],
        label="Target Language",
        value="Français",
    )
    text = gr.Textbox()
    audio_output = gr.Audio(type="numpy", label="Translated Speech")

    b1 = gr.Button("Translate Speech")

    b1.click(
        speech_to_text,
        inputs=[audio_file, language_selection],
        outputs=[text, audio_output],
    )


if __name__ == "__main__":
    demo.launch()
