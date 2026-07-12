import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def fetch_payments():

    payments = stripe.PaymentIntent.list(limit=10)

    payment_list = []

    for payment in payments.data:

        payment_list.append({
            "payment_id": payment.id,
            "amount": payment.amount / 100,
            "currency": payment.currency,
            "status": payment.status,
            "created": payment.created
        })

    return payment_list