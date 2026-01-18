import sys
from lang_detect import detect_language

tests = [
    "Scan QR now",
    "आपका खाता निलंबित है",
    "আপনার KYC আপডেট করুন",
    "Hi bro",
    "OTP"
]

for t in tests:
    lang, conf = detect_language(t)

    sys.stdout.buffer.write(
        f"Text: {t}\nDetected: {lang}, Confidence: {round(conf, 2)}\n{'-'*50}\n".encode("utf-8")
    )
