import pandas as pd

from transform.clean_customers import clean_customers
from transform.clean_payments import clean_payments
from transform.clean_tickets import clean_tickets


def run_transformations():
    """Transform all raw datasets and retain the existing summary output."""

    clean_customers(
        "data/raw/customers.json",
        "data/processed/customers.csv"
    )

    clean_payments(
        "data/raw/payments.json",
        "data/processed/payments.csv"
    )

    clean_tickets(
        "data/raw/tickets.json",
        "data/processed/tickets.csv"
    )

    customers = len(pd.read_csv("data/processed/customers.csv"))
    payments = len(pd.read_csv("data/processed/payments.csv"))
    tickets = len(pd.read_csv("data/processed/tickets.csv"))

    print("\nTransformation Summary")
    print("-" * 35)
    print(f"Customers Converted : {customers}")
    print(f"Payments Converted  : {payments}")
    print(f"Tickets Converted   : {tickets}")
    print()

    print("✓ customers.json -> customers.csv")
    print("✓ payments.json  -> payments.csv")
    print("✓ tickets.json   -> tickets.csv")
    print("-" * 35)

    return customers, payments, tickets


if __name__ == "__main__":
    run_transformations()
