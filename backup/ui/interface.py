import gradio as gr

from ui.dashboard import create_dashboard
from services.pipeline_service import PipelineService
from ui.widgets import LANGUAGES

pipeline = PipelineService()

(
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
) = create_dashboard()


def run_pipeline(video, language, whisper, voice):

    if video is None:
        raise gr.Error("Please upload a video.")

    result = pipeline.run(
        video,
        target_language=LANGUAGES.get(language, "ta")
        if isinstance(LANGUAGES, dict)
        else "ta",
    )

    return (
        100,
        "Translation completed successfully.",
        result["video"],
        result["audio"],
        result["subtitle"],
    )


translate.click(
    fn=run_pipeline,
    inputs=[
        input_video,
        language,
        whisper,
        voice,
    ],
    outputs=[
        progress,
        logs,
        output_video,
        output_audio,
        output_subtitle,
    ],
)