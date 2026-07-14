import gradio as gr


def build_progress():

    return gr.Slider(
        minimum=0,
        maximum=100,
        value=0,
        label="Progress",
        interactive=False,
    )