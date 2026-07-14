import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

from load.database import SessionLocal
from load.models import Customer, Payment, Ticket
from config.logger import logger


# -------------------------
# Load Customers
# -------------------------
def load_customers(session):
    """Insert or update customer rows from the existing processed CSV file."""

    df = pd.read_csv("data/processed/customers.csv")

    count = 0

    for _, row in df.iterrows():

        customer = session.get(Customer, row["customer_id"])

        if customer:

            customer.first_name = row["first_name"]
            customer.last_name = row["last_name"]
            customer.email = row["email"]
            customer.phone = str(row["phone"])
            customer.city = row["city"]
            customer.registration_date = pd.to_datetime(
                row["registration_date"]
            ).date()

        else:

            customer = Customer(
                customer_id=row["customer_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                email=row["email"],
                phone=str(row["phone"]),
                city=row["city"],
                registration_date=pd.to_datetime(
                    row["registration_date"]
                ).date()
            )

            session.add(customer)

        count += 1

    return count


# -------------------------
# Load Tickets
# -------------------------
def load_tickets(session):
    """Insert or update ticket rows from the existing processed CSV file."""

    df = pd.read_csv("data/processed/tickets.csv")

    count = 0

    for _, row in df.iterrows():

        ticket = session.get(Ticket, row["ticket_id"])

        if ticket:

            ticket.customer_id = row["customer_id"]
            ticket.issue_type = row["issue_type"]
            ticket.description = row["description"]
            ticket.status = row["status"]
            ticket.priority = row["priority"]
            ticket.created_date = pd.to_datetime(
                row["created_date"]
            ).date()

        else:

            ticket = Ticket(
                ticket_id=row["ticket_id"],
                customer_id=row["customer_id"],
                issue_type=row["issue_type"],
                description=row["description"],
                status=row["status"],
                priority=row["priority"],
                created_date=pd.to_datetime(
                    row["created_date"]
                ).date()
            )

            session.add(ticket)

        count += 1

    return count


# -------------------------
# Load Payments
# -------------------------
def load_payments(session):
    """Insert or update payment rows from the existing processed CSV file."""

    df = pd.read_csv("data/processed/payments.csv")

    count = 0

    for _, row in df.iterrows():

        payment = session.get(Payment, row["payment_id"])

        if payment:

            payment.customer_id = row["customer_id"]
            payment.ticket_id = row["ticket_id"]
            payment.amount = row["amount"]
            payment.payment_method = row["payment_method"]
            payment.payment_status = row["payment_status"]
            payment.payment_date = pd.to_datetime(
                row["payment_date"]
            ).date()

        else:

            payment = Payment(
                payment_id=row["payment_id"],
                customer_id=row["customer_id"],
                ticket_id=row["ticket_id"],
                amount=row["amount"],
                payment_method=row["payment_method"],
                payment_status=row["payment_status"],
                payment_date=pd.to_datetime(
                    row["payment_date"]
                ).date()
            )

            session.add(payment)

        count += 1

    return count


# -------------------------
# Main Loader
# -------------------------
def run_loader():
    """Load processed datasets using the established transaction sequence."""

    session = SessionLocal()

    try:

        customers = load_customers(session)
        session.commit()

        tickets = load_tickets(session)
        session.commit()

        payments = load_payments(session)
        session.commit()

        return customers, payments, tickets

    except SQLAlchemyError as e:

        session.rollback()

        print("\n" + "=" * 60)
        print("DATABASE ERROR")
        print("=" * 60)
        print(e)
        print("=" * 60)

        logger.exception(f"Database Error: {e}")

        raise

    finally:

        session.close()


if __name__ == "__main__":

    c, p, t = run_loader()

    print("\nFinal Summary")
    print("-----------------------------------")
    print(f"Customers Loaded : {c}")
    print(f"Payments Loaded  : {p}")
    print(f"Tickets Loaded   : {t}")
    print("-----------------------------------")
