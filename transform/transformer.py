from transform.clean_customers import clean_customers
from transform.clean_payments import clean_payments
from transform.clean_tickets import clean_tickets

def run_transformations():
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

if __name__ == "__main__":
    run_transformations()