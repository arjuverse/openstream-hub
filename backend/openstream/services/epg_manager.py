from pathlib import Path

from openstream.repositories.epg_repository import EPGRepository
from openstream.repositories.epg_source_repository import (
    EPGSourceRepository,
)
from openstream.services.epg_service import EPGService


class EPGManager:

    def __init__(self, db):

        self.db = db

        self.epg_repo = EPGRepository(db)
        self.source_repo = EPGSourceRepository(db)

        self.service = EPGService(self.epg_repo)

    def import_all(self):

        sources = self.source_repo.get_enabled()

        print(f"\nFound {len(sources)} EPG sources\n")

        # Clear the EPG database ONCE
        self.epg_repo.clear_database()

        for source in sources:

            print("=" * 60)
            print(f"Importing: {source.name}")
            print("=" * 60)

            if not Path(source.url).exists():

                print(f"Missing file: {source.url}")
                continue

            self.service.import_xml(source.url)

        print("\nFinished importing all sources.")