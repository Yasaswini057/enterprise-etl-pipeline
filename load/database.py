from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read PostgreSQL credentials from .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# PostgreSQL Connection URL
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Create SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    echo=False,          # Change to True if you want SQL queries printed
    future=True
)

# Session Factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


def get_db():
    """
    Returns a database session.
    Usage:
        session = get_db()
    """
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


def test_connection():
    """
    Test PostgreSQL connection.
    """
    try:
        connection = engine.connect()
        print("✓ PostgreSQL Connected Successfully")
        connection.close()
    except Exception as e:
        print("✗ Database Connection Failed")
        print(e)


if __name__ == "__main__":
    test_connection()