import gradio as gr


def build_logs():

    return gr.Textbox(
        label="Processing Logs",
        lines=12,
        interactive=False,
    )