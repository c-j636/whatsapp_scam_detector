from rule_engine import apply_rules

tests = [
    "Your KYC is pending verify immediately",
    "Congratulations you won lottery prize",
    "Scan QR urgently to receive refund",
    "Exclusive adult private video chat",
    "Hi bro lunch today"
]

for t in tests:
    print("TEXT:", t)
    print(apply_rules(t))
    print("-" * 60)
