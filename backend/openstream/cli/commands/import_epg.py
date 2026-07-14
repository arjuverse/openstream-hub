from openstream.database.session import SessionLocal
from openstream.services.epg_manager import EPGManager


def run():

    db = SessionLocal()

    manager = EPGManager(db)

    manager.import_all()

    db.close()
