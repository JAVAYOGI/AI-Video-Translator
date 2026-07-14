import gradio as gr

from ui.widgets import (
    LANGUAGES,
    WHISPER_MODELS,
    VOICES,
)


def build_sidebar():

    gr.Markdown("## ⚙ Settings")

    language = gr.Dropdown(
        choices=LANGUAGES,
        value="Tamil",
        label="Target Language",
    )

    whisper = gr.Dropdown(
        choices=WHISPER_MODELS,
        value="base",
        label="Whisper Model",
    )

    voice = gr.Dropdown(
        choices=VOICES,
        value="Female",
        label="Voice",
    )

    translate = gr.Button(
        "🚀 Translate",
        variant="primary",
    )

    return (
        language,
        whisper,
        voice,
        translate,
    )