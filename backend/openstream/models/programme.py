from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from openstream.database.base import Base


class Programme(Base):
    __tablename__ = "programmes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    epg_channel_id: Mapped[int] = mapped_column(
        ForeignKey("epg_channels.id"),
        index=True,
    )

    title: Mapped[str] = mapped_column(String)

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    category: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    start_time: Mapped[datetime] = mapped_column(DateTime)

    stop_time: Mapped[datetime] = mapped_column(DateTime)

    episode: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    rating: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )
