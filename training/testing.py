from final_risk_engine import assess_message

tests = [
    # unseen but realistic scams
    "Dear customer your account access limited please confirm",
    "Earn 3000 daily work from home no investment",
    "Scan QR to reverse failed transaction",

    # tricky safe messages
    "Bank called me today regarding my loan",
    "Refund from college is processed",
    "Urgent meeting at office today"
]

for t in tests:
    print(t)
    print(assess_message(t))
    print("-"*60)
