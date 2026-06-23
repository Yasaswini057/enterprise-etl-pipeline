from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float
from database import engine

Base = declarative_base()

class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    revenue = Column(Float)

Base.metadata.create_all(bind=engine)

print("Tables Created")