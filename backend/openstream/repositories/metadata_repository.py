from sqlalchemy import func
from sqlalchemy.orm import Session

from openstream.models.channel import Channel
from openstream.models.playlist import Playlist


class MetadataRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_stats(self):
        return {
            "playlists": self.db.query(func.count(Playlist.id)).scalar() or 0,
            "channels": self.db.query(func.count(Channel.id)).scalar() or 0,
            "countries": (
                self.db.query(Channel.country)
                .filter(Channel.country.isnot(None))
                .distinct()
                .count()
            ),
            "languages": (
                self.db.query(Channel.language)
                .filter(Channel.language.isnot(None))
                .distinct()
                .count()
            ),
            "categories": (
                self.db.query(Channel.category)
                .filter(Channel.category.isnot(None))
                .distinct()
                .count()
            ),
        }

    def get_categories(self):
        rows = (
            self.db.query(
                Channel.category,
                func.count(Channel.id),
            )
            .filter(Channel.category.isnot(None))
            .group_by(Channel.category)
            .order_by(Channel.category)
            .all()
        )

        return [
            {"name": category, "count": count}
            for category, count in rows
        ]

    def get_countries(self):
        rows = (
            self.db.query(
                Channel.country,
                func.count(Channel.id),
            )
            .filter(Channel.country.isnot(None))
            .group_by(Channel.country)
            .order_by(Channel.country)
            .all()
        )

        return [
            {"name": country, "count": count}
            for country, count in rows
        ]

    def get_languages(self):
        rows = (
            self.db.query(
                Channel.language,
                func.count(Channel.id),
            )
            .filter(Channel.language.isnot(None))
            .group_by(Channel.language)
            .order_by(Channel.language)
            .all()
        )

        return [
            {"name": language, "count": count}
            for language, count in rows
        ]