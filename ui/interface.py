import gradio as gr

from core.pipeline import VideoTranslatorPipeline
from ui.theme import theme
from ui.styles import CSS
from ui.widgets import LANGUAGES

pipeline = VideoTranslatorPipeline()


def translate_video(video, language):

    if video is None:
        raise gr.Error("Please upload a video.")

    if isinstance(LANGUAGES, dict):
        target = LANGUAGES.get(language, "ta")
    else:
        target = "ta"

    result = pipeline.run(
        video,
        target_language=target,
    )

    return (
        100,
        "Translation completed successfully.",
        result["video"],
        result["audio"],
        result["subtitle"],
    )


with gr.Blocks(
    theme=theme,
    css=CSS,
    title="AI Video Translator v2.0",
) as demo:

    gr.Markdown(
        """
# 🎬 AI Video Translator v2.0

Professional AI Video Translation Platform
"""
    )

    with gr.Row():

        with gr.Column(scale=3):

            input_video = gr.Video(
                label="📹 Upload Video"
            )

        with gr.Column(scale=1):

            language = gr.Dropdown(
                choices=list(LANGUAGES.keys()) if isinstance(LANGUAGES, dict) else LANGUAGES,
                value="Tamil",
                label="🌍 Target Language",
            )

            whisper = gr.Dropdown(
                choices=[
                    "tiny",
                    "base",
                    "small",
                    "medium",
                    "large-v3",
                ],
                value="base",
                label="🤖 Whisper Model",
            )

            voice = gr.Dropdown(
                choices=[
                    "Female",
                    "Male",
                ],
                value="Female",
                label="🎤 Voice",
            )

            translate = gr.Button(
                "🚀 Translate",
                variant="primary",
            )

    progress = gr.Slider(
        minimum=0,
        maximum=100,
        value=0,
        label="Progress",
        interactive=False,
    )

    logs = gr.Textbox(
        label="Processing Logs",
        lines=8,
        interactive=False,
    )

    with gr.Row():

        output_video = gr.Video(
            label="🎥 Translated Video"
        )

        output_audio = gr.Audio(
            label="🔊 Dubbed Audio"
        )

    output_subtitle = gr.File(
        label="📄 Subtitle (.srt)"
    )

    translate.click(
        fn=translate_video,
        inputs=[
            input_video,
            language,
        ],
        outputs=[
            progress,
            logs,
            output_video,
            output_audio,
            output_subtitle,
        ],
    )