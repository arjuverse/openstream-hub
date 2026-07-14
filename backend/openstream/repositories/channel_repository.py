from math import ceil

from sqlalchemy import asc, desc, or_
from sqlalchemy.orm import Session

from openstream.models.channel import Channel


class ChannelRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, channel_id: int):
        return (
            self.db.query(Channel)
            .filter(Channel.id == channel_id)
            .first()
        )

    def get_channels(
        self,
        *,
        page: int = 1,
        size: int = 50,
        search: str | None = None,
        group: str | None = None,
        category: str | None = None,
        matched: bool | None = None,
        sort: str = "name",
        order: str = "asc",
    ):
        query = self.db.query(Channel)

        if search:
            pattern = f"%{search}%"

            query = query.filter(
                or_(
                    Channel.name.ilike(pattern),
                    Channel.tvg_id.ilike(pattern),
                    Channel.tvg_name.ilike(pattern),
                )
            )

        if group:
            query = query.filter(Channel.group_title == group)

        if category:
            query = query.filter(Channel.category == category)

        if matched:
            query = query.filter(Channel.epg_channel_id.is_not(None))

        sort_column = getattr(Channel, sort, Channel.name)

        if order.lower() == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        total = query.count()

        items = (
            query.offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return {
            "items": items,
            "page": page,
            "size": size,
            "total": total,
            "pages": ceil(total / size) if total else 0,
        }