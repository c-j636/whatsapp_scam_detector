import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(BASE_DIR, "data", "cleaned.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "fasttext_train.txt")

print("Reading data from:", INPUT_PATH)

df = pd.read_csv(INPUT_PATH)

rows_written = 0

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    for _, row in df.iterrows():

        message = str(row["message"]).strip()
        if not message or message == "nan":
            continue  # skip empty rows

        label_raw = str(row["label"]).strip().lower()

        # Normalize labels to 2 classes only
        if label_raw in ["spam", "scam", "fraud"]:
            label = "__label__spam"
        else:
            label = "__label__not_spam"

        message = message.replace("\n", " ")

        f.write(f"{label} {message}\n")
        rows_written += 1

print("FASTTEXT TRAIN FILE CREATED AT:", OUTPUT_PATH)
print("ROWS USED FOR TRAINING:", rows_written)
