from collections.abc import Generator
import os
from openstream.database.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



print("Current working directory:", os.getcwd())