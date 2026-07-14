import gradio as gr

from core.pipeline import VideoTranslatorPipeline
from ui.theme import theme
from ui.components import LANGUAGES

pipeline = VideoTranslatorPipeline()


def translate_video(video, language):

    if video is None:
        raise gr.Error("Please upload a video.")

    result = pipeline.run(
        video,
        target_language=LANGUAGES[language],
    )

    return (
        result["video"],
        result["audio"],
        result["subtitle"],
    )


with gr.Blocks(
    theme=theme,
    title="AI Video Translator",
) as demo:

    gr.Markdown(
        "# 🎬 AI Video Translator"
    )

    with gr.Row():

        video = gr.Video(
            label="Upload Video"
        )

        language = gr.Dropdown(
            choices=list(LANGUAGES.keys()),
            value="Tamil",
            label="Target Language",
        )

    translate = gr.Button(
        "Translate Video",
        variant="primary",
    )

    output_video = gr.Video(
        label="Translated Video"
    )

    output_audio = gr.Audio(
        label="Translated Audio"
    )

    output_subtitle = gr.File(
        label="Subtitle (.srt)"
    )

    translate.click(
        translate_video,
        [video, language],
        [
            output_video,
            output_audio,
            output_subtitle,
        ],
    )