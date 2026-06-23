from database import SessionLocal
from models import Customer

session = SessionLocal()

customer = Customer(
    name="John Doe",
    email="john@gmail.com",
    revenue=2500
)

session.add(customer)
session.commit()

print("Customer Inserted")