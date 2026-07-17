from datetime import datetime
from sqlalchemy import and_, asc, desc
from sqlalchemy.orm import Session

from openstream.models.channel import Channel
from openstream.models.programme import Programme


class ChannelRepository:
    def __init__(self, db: Session):
        self.db = db
        self.model = Channel

    def get(
        self,
        channel_id: int,
    ):
        return (
            self.db.query(self.model)
            .filter(self.model.id == channel_id)
            .first()
        )

    def get_categories(self) -> list[str]:
        rows = (
            self.db.query(self.model.group_title)
            .filter(self.model.group_title.isnot(None))
            .distinct()
            .order_by(self.model.group_title)
            .all()
        )

        return [row[0] for row in rows if row[0]]

    def get_channels(
        self,
        page: int,
        size: int,
        search: str | None = None,
        group: str | None = None,
        category: str | None = None,
        matched: bool | None = None,
        sort: str = "name",
        order: str = "asc",
    ):
        query = self.db.query(self.model)

        if search:
            query = query.filter(
                self.model.name.ilike(f"%{search}%")
            )

        if group:
            query = query.filter(
                self.model.group_title == group
            )

        if category:
            query = query.filter(
                self.model.category == category
            )

        if matched is not None:
            if matched:
                query = query.filter(
                    self.model.epg_channel_id.isnot(None)
                )
            else:
                query = query.filter(
                    self.model.epg_channel_id.is_(None)
                )

        total = query.count()

        sort_column = getattr(self.model, sort, self.model.name)

        if order.lower() == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        items = (
            query.offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return items, total

    def get_now_playing(self, epg_channel_id: int):
        now = datetime.utcnow()
        
        return (
            self.db.query(Programme)
            .filter(Programme.epg_channel_id == epg_channel_id)
            .filter(
                and_(
                    Programme.start_time <= now,
                    Programme.stop_time > now
                )
            )
            .first()
        )