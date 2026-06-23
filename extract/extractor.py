import json
import os

from extract.salesforce_api import fetch_customers
from extract.stripe_api import fetch_payments
from extract.zendesk_api import fetch_tickets


def run_extraction():
    os.makedirs("data/raw", exist_ok=True)

    customers = fetch_customers()
    payments = fetch_payments()
    tickets = fetch_tickets()

    with open("data/raw/customers.json", "w") as f:
        json.dump(customers, f, indent=4)

    with open("data/raw/payments.json", "w") as f:
        json.dump(payments, f, indent=4)

    with open("data/raw/tickets.json", "w") as f:
        json.dump(tickets, f, indent=4)

    print("All raw data saved successfully")