from sqlalchemy.orm import Session

from openstream.models.epg_source import EPGSource


class EPGSourceRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(EPGSource)
            .order_by(EPGSource.name)
            .all()
        )

    def get_enabled(self):
        return (
            self.db.query(EPGSource)
            .filter(EPGSource.enabled.is_(True))
            .all()
        )

    def get_by_name(self, name: str):
        return (
            self.db.query(EPGSource)
            .filter(EPGSource.name == name)
            .first()
        )

    def add(self, source: EPGSource):
        self.db.add(source)
        self.db.commit()
        self.db.refresh(source)
        return source

    def exists(self, name: str):
        return (
            self.db.query(EPGSource)
            .filter(EPGSource.name == name)
            .first()
            is not None
        )
