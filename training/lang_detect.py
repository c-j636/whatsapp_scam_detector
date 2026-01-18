import fasttext
import os

# ---------------------------------------
# Resolve base directory
# ---------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------
# Path to FastText language ID model
# ---------------------------------------
LANG_MODEL_PATH = os.path.join(BASE_DIR, "model", "lid.176.ftz")

# ---------------------------------------
# Load language detection model (once)
# ---------------------------------------
if not os.path.exists(LANG_MODEL_PATH):
    raise FileNotFoundError(
        "Language detection model not found. "
        "Download lid.176.ftz and place it in /model directory."
    )

lang_model = fasttext.load_model(LANG_MODEL_PATH)

# ---------------------------------------
# Language detection function
# ---------------------------------------
def detect_language(text: str):
    """
    Detects the language of a given text using FastText.

    Args:
        text (str): Input message text

    Returns:
        lang (str): ISO language code (e.g. 'en', 'hi', 'bn')
        confidence (float): Probability score between 0 and 1
    """

    # Clean input
    text = str(text).replace("\n", " ").strip()

    if len(text) == 0:
        return "en", 0.0

    # Predict language
    labels, probabilities = lang_model.predict(text)

    lang = labels[0].replace("__label__", "")
    confidence = probabilities[0]

    return lang, confidence
