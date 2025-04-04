import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load database URL from environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://user:password@db/weather_db")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Function to get a new database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
