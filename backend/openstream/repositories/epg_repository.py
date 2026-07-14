from sqlalchemy.orm import Session

from openstream.models.epg_channel import EPGChannel
from openstream.models.programme import Programme


class EPGRepository:
    def __init__(self, db: Session):
        self.db = db

    # ---------- Cleanup ----------

    def clear_programmes(self):
        self.db.query(Programme).delete()

    def clear_channels(self):
        self.db.query(EPGChannel).delete()

    def clear_database(self):
        """
        Remove all imported EPG data.
        """
        self.db.query(Programme).delete()
        self.db.query(EPGChannel).delete()
        self.db.commit()

    # ---------- Channels ----------

    def get_channel(self, epg_id: str):
        return (
            self.db.query(EPGChannel)
            .filter(EPGChannel.epg_id == epg_id)
            .first()
        )

    def add_channel(self, channel: EPGChannel):
        self.db.add(channel)
        self.db.flush()
        return channel

    # ---------- Bulk Inserts ----------

    def bulk_insert_programmes(self, programmes: list[dict]):
        if programmes:
            self.db.bulk_insert_mappings(
                Programme,
                programmes,
            )

    # ---------- Commit ----------

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()