import fasttext
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIN_CSV = os.path.join(BASE_DIR, "data", "train.csv")
TRAIN_TXT = os.path.join(BASE_DIR, "data", "fasttext_train_v3.txt")
MODEL_PATH = os.path.join(BASE_DIR, "model", "scam_fasttext_v3.bin")

# Load training data
df = pd.read_csv(TRAIN_CSV)

# Sanity cleanup
df["message"] = df["message"].astype(str)
df["label"] = df["label"].astype(str).str.strip().str.lower()

# Convert to FastText format
with open(TRAIN_TXT, "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        label = "__label__" + row["label"]
        text = row["message"].replace("\n", " ")
        f.write(f"{label} {text}\n")

print("FastText training file created:", TRAIN_TXT)
print("Training rows:", len(df))

# Train model
model = fasttext.train_supervised(
    input=TRAIN_TXT,
    epoch=50,          # more epochs since data is small
    lr=0.25,           # stable learning
    wordNgrams=2,      # context awareness
    dim=150,           # richer embeddings
    loss="softmax"
)

# Save model
model.save_model(MODEL_PATH)

print("Model saved at:", MODEL_PATH)
