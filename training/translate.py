def translate_to_english(text: str, lang: str):
    """
    Translates non-English text to English.

    NOTE:
    - This is a placeholder for laptop testing
    - Android app will handle real translation using ML Kit
    - We keep this function so pipeline never breaks
    """

    text = str(text).strip()

    # For now, return text as-is
    # (Android will replace this logic)
    return text
