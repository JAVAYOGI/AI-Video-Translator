"""
Professional TTS Manager
"""

import asyncio
from pathlib import Path

import edge_tts
from gtts import gTTS

from models.tts_loader import (
    EDGE_VOICE,
    DEFAULT_LANGUAGE,
)

from utils import (
    ensure_dir,
    get_logger,
)

logger = get_logger()


class TextToSpeech:

    def __init__(self, output_dir="outputs/audio"):

        self.output_dir = Path(output_dir)

        ensure_dir(self.output_dir)

    async def _edge(self, text, output):

        communicate = edge_tts.Communicate(
            text=text,
            voice=EDGE_VOICE
        )

        await communicate.save(output)

    def speak(
        self,
        text,
        filename="dubbed.mp3"
    ):

        output = self.output_dir / filename

        # -----------------------
        # Try Edge TTS
        # -----------------------

        try:

            logger.info("Trying Edge TTS...")

            asyncio.run(
                self._edge(
                    text,
                    str(output)
                )
            )

            logger.info("Edge TTS Success")

            return str(output)

        except Exception as e:

            logger.warning(
                f"Edge TTS Failed : {e}"
            )

        # -----------------------
        # Fallback → gTTS
        # -----------------------

        try:

            logger.info("Trying gTTS...")

            tts = gTTS(

                text=text,

                lang=DEFAULT_LANGUAGE,

                slow=False

            )

            tts.save(str(output))

            logger.info("gTTS Success")

            return str(output)

        except Exception as e:

            logger.error(e)

            raise RuntimeError(
                "No TTS Engine Available."
            )