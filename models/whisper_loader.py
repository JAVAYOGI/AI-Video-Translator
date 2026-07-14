"""
Whisper Model Loader
"""

from faster_whisper import WhisperModel

_model = None


def get_whisper_model(
    model_size="base",
    device="auto",
    compute_type="int8",
):
    global _model

    if _model is None:

        _model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type,
        )

    return _model