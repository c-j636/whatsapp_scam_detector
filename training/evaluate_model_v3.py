import fasttext
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "scam_fasttext_v3.bin")
VAL_PATH = os.path.join(BASE_DIR, "data", "val.csv")

# Load model and validation data
model = fasttext.load_model(MODEL_PATH)
df = pd.read_csv(VAL_PATH)

df["message"] = df["message"].astype(str)
df["label"] = df["label"].astype(str).str.strip().str.lower()

correct = 0
total = len(df)

for _, row in df.iterrows():
    text = row["message"]
    true_label = "__label__" + row["label"]
    pred, _ = model.predict(text)
    if pred[0] == true_label:
        correct += 1

accuracy = correct / total

print("Validation samples:", total)
print("Correct predictions:", correct)
print("Validation Accuracy:", round(accuracy * 100, 2), "%")

tp = tn = fp = fn = 0

for _, row in df.iterrows():
    text = row["message"]
    true = row["label"]
    pred, _ = model.predict(text)
    pred = pred[0].replace("__label__", "")

    if pred == "spam" and true == "spam":
        tp += 1
    elif pred == "not_spam" and true == "not_spam":
        tn += 1
    elif pred == "spam" and true == "not_spam":
        fp += 1
    elif pred == "not_spam" and true == "spam":
        fn += 1

print("TP:", tp, "TN:", tn, "FP:", fp, "FN:", fn)
