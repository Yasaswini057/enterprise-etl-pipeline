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
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    city = Column(String(255))
    phone = Column(String(50))
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
# Delete existing tables
Base.metadata.drop_all(bind=engine)

# Create tables again with the new schema
Base.metadata.create_all(bind=engine)

print("✓ PostgreSQL Tables Recreated Successfully")