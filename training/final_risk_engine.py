import fasttext
import os
from rule_engine import apply_rules
from lang_detect import detect_language
from translate import translate_to_english


# ---------------------------------------
# Paths & model loading
# ---------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "model")
CURRENT_MODEL_FILE = os.path.join(MODEL_DIR, "current_model.txt")

with open(CURRENT_MODEL_FILE, "r") as f:
    model_name = f.read().strip()

MODEL_PATH = os.path.join(MODEL_DIR, model_name)
model = fasttext.load_model(MODEL_PATH)


# ---------------------------------------
# Thresholds
# ---------------------------------------
IS_SCAM_THRESHOLD = 60
HARD_RULE_OVERRIDE = 80


# ---------------------------------------
# Main inference function
# ---------------------------------------
def assess_message(text: str):
    original_text = str(text)

    # -----------------------------------
    # Language detection
    # -----------------------------------
    lang, lang_conf = detect_language(original_text)

    # -----------------------------------
    # Translation routing (if needed)
    # -----------------------------------
    if lang != "en" and lang_conf > 0.7:
        processed_text = translate_to_english(original_text, lang)
        used_translation = True
    else:
        processed_text = original_text
        used_translation = False

    # -----------------------------------
    # ML prediction
    # -----------------------------------
    label, prob = model.predict(processed_text)
    ml_confidence = min(max(prob[0], 0.05), 0.95)
    ml_score = int(ml_confidence * 100)

    # -----------------------------------
    # Rule engine
    # -----------------------------------
    rule_result = apply_rules(processed_text)
    rule_score = rule_result["rule_score"]
    triggers = rule_result["triggers"]

    # -----------------------------------
    # Fusion logic
    # -----------------------------------
    final_risk = int(0.5 * ml_score + 0.5 * rule_score)

    if rule_score >= HARD_RULE_OVERRIDE:
        final_risk = max(final_risk, 85)

    final_risk = max(0, min(final_risk, 100))
    is_scam = final_risk >= IS_SCAM_THRESHOLD

    # -----------------------------------
    # Explanation
    # -----------------------------------
    explanation_parts = []
    if triggers:
        explanation_parts.append(
            "Triggered rules: " + ", ".join(triggers[:5])
        )
    explanation_parts.append(
        f"ML confidence: {round(ml_confidence, 2)}"
    )

    # -----------------------------------
    # Final output (STABLE INTERFACE)
    # -----------------------------------
    return {
        "is_scam": is_scam,
        "final_risk": final_risk,
        "language": lang,
        "language_confidence": round(lang_conf, 2),
        "used_translation": used_translation,
        "ml_confidence": round(ml_confidence, 2),
        "rule_score": rule_score,
        "triggers": triggers,
        "explanation": " | ".join(explanation_parts)
    }
