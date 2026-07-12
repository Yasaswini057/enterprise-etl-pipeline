from extract.stripe_api import fetch_payments

payments = fetch_payments()

print("=" * 60)
print("REAL STRIPE API PAYMENTS")
print("=" * 60)

for p in payments:
    print(f"Payment ID : {p['payment_id']}")
    print(f"Amount     : ${p['amount']}")
    print(f"Currency   : {p['currency'].upper()}")
    print(f"Status     : {p['status']}")
    print("-" * 60)