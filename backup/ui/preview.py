import gradio as gr


def build_preview():

    with gr.Row():

        video = gr.Video(
            label="Translated Video"
        )

        audio = gr.Audio(
            label="Translated Audio"
        )

    subtitle = gr.File(
        label="Subtitle"
    )

    return (
        video,
        audio,
        subtitle,
    )