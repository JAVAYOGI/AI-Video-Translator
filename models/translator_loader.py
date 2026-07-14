from deep_translator import GoogleTranslator


def get_translator(source="auto", target="ta"):
    return GoogleTranslator(
        source=source,
        target=target
    )