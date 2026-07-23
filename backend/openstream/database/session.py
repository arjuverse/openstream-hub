import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import your settings (adjust the import path if yours looks slightly different)
from openstream.core.config import settings

# 1. Grab the URL from the terminal environment variable first (used by ingestion script).
# 2. If it's not there, fallback to the Pydantic settings.
db_url = os.getenv("DATABASE_URL")
if not db_url:
    if hasattr(settings, "SQLALCHEMY_DATABASE_URI"):
        db_url = str(settings.SQLALCHEMY_DATABASE_URI)
    elif hasattr(settings, "DATABASE_URL"):
        db_url = str(settings.DATABASE_URL)
    else:
        # Absolute fallback for local development
        db_url = "sqlite:///./openstream.db"

# 3. Create the engine with the correct arguments based on the database type
if db_url.startswith("sqlite"):
    engine = create_engine(
        db_url, connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL does not use or allow 'check_same_thread'
    engine = create_engine(db_url)

# 4. Create the configured SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)