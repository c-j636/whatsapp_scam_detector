import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULE_PATH = os.path.join(BASE_DIR, "rules", "rules_v2.json")

with open(RULE_PATH, "r", encoding="utf-8") as f:
    RULES = json.load(f)

def apply_rules(text: str):
    text = text.lower()
    score = 0
    triggers = []

    for category, rules in RULES.items():
        for key, weight in rules.items():
            if key in text:
                score += weight
                triggers.append(key)

    # Clamp score safely
    score = max(0, min(score, 100))

    return {
        "rule_score": score,
        "triggers": list(set(triggers))
    }
