import gradio as gr

from ui.sidebar import build_sidebar
from ui.preview import build_preview
from ui.progress import build_progress
from ui.logs import build_logs
from ui.styles import CSS
from ui.theme import theme


def create_dashboard():

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

                (
                    language,
                    whisper,
                    voice,
                    translate,
                ) = build_sidebar()

        progress = build_progress()

        logs = build_logs()

        (
            output_video,
            output_audio,
            output_subtitle,
        ) = build_preview()

        return (
            demo,
            input_video,
            language,
            whisper,
            voice,
            translate,
            progress,
            logs,
            output_video,
            output_audio,
            output_subtitle,
        )