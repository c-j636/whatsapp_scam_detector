import fasttext
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "scam_fasttext_v2.bin")
VAL_PATH = os.path.join(BASE_DIR, "data", "val.csv")

model = fasttext.load_model(MODEL_PATH)
df = pd.read_csv(VAL_PATH)

correct = 0

for _, row in df.iterrows():
    text = str(row["message"])
    true_label = "__label__" + str(row["label"]).strip().lower()
    pred, _ = model.predict(text)
    if pred[0] == true_label:
        correct += 1

accuracy = correct / len(df)
print("Validation Accuracy:", round(accuracy * 100, 2), "%")
