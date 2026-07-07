from sqlalchemy import text
from load.database import engine

with engine.connect() as conn:
    print("Customers:", conn.execute(text("SELECT COUNT(*) FROM customers")).scalar())
    print("Payments :", conn.execute(text("SELECT COUNT(*) FROM payments")).scalar())
    print("Tickets  :", conn.execute(text("SELECT COUNT(*) FROM tickets")).scalar())