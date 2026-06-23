from database import SessionLocal
from models import Customer

session = SessionLocal()

record = {
    "name": "John Updated",
    "email": "john@gmail.com",
    "revenue": 5000
}

existing = (
    session.query(Customer)
    .filter_by(email=record["email"])
    .first()
)

if existing:
    existing.name = record["name"]
    existing.revenue = record["revenue"]
else:
    session.add(Customer(**record))

session.commit()

print("Upsert Completed")