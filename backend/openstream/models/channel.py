from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from openstream.database.base import Base


class Channel(Base):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    stream_url: Mapped[str] = mapped_column(Text, unique=True, nullable=False)

    logo_url: Mapped[str | None] = mapped_column(Text, nullable=True)

    category: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    country: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    language: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)

    tvg_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    tvg_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    group_title: Mapped[str | None] = mapped_column(
        String(255), index=True, nullable=True
    )

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_checked: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    playlist_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("playlists.id"),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    playlist = relationship("Playlist", back_populates="channels")
