from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from openstream.database.base import Base


class EPGChannel(Base):
    __tablename__ = "epg_channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    epg_id: Mapped[str] = mapped_column(String, unique=True, index=True)

    display_name: Mapped[str] = mapped_column(String)

    icon: Mapped[str | None] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    source_id: Mapped[int] = mapped_column(
        ForeignKey("epg_sources.id"),
        nullable=False,
    )       


