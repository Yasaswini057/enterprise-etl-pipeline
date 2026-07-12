import json
import os

from extract.salesforce_api import fetch_customers
from extract.stripe_api import fetch_payments
from extract.zendesk_api import fetch_tickets


def run_extraction():
    # Create raw data folder if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Fetch data from APIs
    customers = fetch_customers()
    payments = fetch_payments()
    tickets = fetch_tickets()

    # Save Customers JSON
    with open("data/raw/customers.json", "w") as f:
        json.dump(customers, f, indent=4)

    # Save Payments JSON
    with open("data/raw/payments.json", "w") as f:
        json.dump(payments, f, indent=4)

    # Save Tickets JSON
    with open("data/raw/tickets.json", "w") as f:
        json.dump(tickets, f, indent=4)

    # Extraction Summary
    print("\nExtraction Summary")
    print("-" * 35)

    customer_count = len(customers)
    payment_count = len(payments)
    ticket_count = len(tickets.get("posts", []))

    print(f"Customers Extracted : {customer_count}")
    print(f"Payments Extracted  : {payment_count}")
    print(f"Tickets Extracted   : {ticket_count}")

    print("-" * 35)
    print("All raw data saved successfully")