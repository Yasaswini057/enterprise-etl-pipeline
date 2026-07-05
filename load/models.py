from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Text, Date, ForeignKey
from load.database import engine

Base = declarative_base()


# -------------------------
# Customers Table
# -------------------------
class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(String, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(20))
    city = Column(String(100))
    registration_date = Column(Date)


# -------------------------
# Tickets Table
# -------------------------
class Ticket(Base):
    __tablename__ = "tickets"

    ticket_id = Column(String, primary_key=True)
    customer_id = Column(
        String,
        ForeignKey("customers.customer_id"),
        nullable=False
    )
    issue_type = Column(String(150))
    description = Column(Text)
    status = Column(String(50))
    priority = Column(String(50))
    created_date = Column(Date)


# -------------------------
# Payments Table
# -------------------------
class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(String, primary_key=True)
    customer_id = Column(
        String,
        ForeignKey("customers.customer_id"),
        nullable=False
    )
    ticket_id = Column(
        String,
        ForeignKey("tickets.ticket_id"),
        nullable=False
    )
    amount = Column(Float)
    payment_method = Column(String(50))
    payment_status = Column(String(50))
    payment_date = Column(Date)


# -------------------------
# Create Tables
# -------------------------
Base.metadata.create_all(bind=engine)

print("✓ PostgreSQL Tables Created Successfully")