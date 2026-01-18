import fasttext
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIN_PATH = os.path.join(BASE_DIR, "data", "fasttext_train.txt")
MODEL_DIR = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "scam_fasttext.bin")

os.makedirs(MODEL_DIR, exist_ok=True)

print("Training data:", TRAIN_PATH)
print("Model output:", MODEL_PATH)

model = fasttext.train_supervised(
    input=TRAIN_PATH,
    epoch=30,
    lr=0.5,
    wordNgrams=2,
    dim=100,
    loss="softmax"
)

model.save_model(MODEL_PATH)

print("MODEL TRAINING COMPLETE")
