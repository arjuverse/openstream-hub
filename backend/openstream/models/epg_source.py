from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from openstream.database.base import Base


class EPGSource(Base):
    __tablename__ = "epg_sources"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    country: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    last_download: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    last_import: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )