import fasttext
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "scam_fasttext.bin")

print("Loading model from:", MODEL_PATH)

model = fasttext.load_model(MODEL_PATH)

tests = [
    "Your KYC is pending click link now",
    "Congratulations you won lottery prize claim now",
    "Your OTP is 123456 do not share",
    "Hi bro are we meeting today",
    "Mom asked why random links keep coming",
    "Exclusive adult room access click to enter"
]

for text in tests:
    label, prob = model.predict(text)
    print("TEXT:", text)
    print("PREDICTION:", label[0], "CONFIDENCE:", round(prob[0], 3))
    print("-" * 50)
