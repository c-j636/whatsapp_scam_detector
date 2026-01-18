from final_risk_engine import assess_message

tests = [
    "Your KYC is pending verify immediately click link",
    "Scan QR urgently to receive refund",
    "Exclusive adult private room access",
    "Refund initiated please verify details",
    "Hi bro are we meeting today",
    "Mom call me when free"
]

for t in tests:
    print("TEXT:", t)
    print(assess_message(t))
    print("=" * 80)
