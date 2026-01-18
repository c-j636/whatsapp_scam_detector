import fasttext
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIN_CSV = os.path.join(BASE_DIR, "data", "train.csv")
TRAIN_TXT = os.path.join(BASE_DIR, "data", "fasttext_train_v2.txt")
MODEL_PATH = os.path.join(BASE_DIR, "model", "scam_fasttext_v2.bin")

df = pd.read_csv(TRAIN_CSV)

with open(TRAIN_TXT, "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        label = "__label__" + str(row["label"]).strip().lower()
        text = str(row["message"]).replace("\n", " ")
        f.write(f"{label} {text}\n")

model = fasttext.train_supervised(
    input=TRAIN_TXT,
    epoch=40,          # higher learning cycles
    lr=0.3,            # smoother learning
    wordNgrams=2,      # context
    dim=150,           # richer embeddings
    loss="softmax"
)

model.save_model(MODEL_PATH)

print("Improved model saved at:", MODEL_PATH)
