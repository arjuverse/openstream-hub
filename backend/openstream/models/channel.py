from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from openstream.database.base import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)

    playlist_id = Column(
        Integer,
        ForeignKey("playlists.id"),
        nullable=False,
    )

    name = Column(
        String,
        nullable=False,
        index=True,
    )

    tvg_id = Column(String, nullable=True)
    tvg_name = Column(String, nullable=True)
    logo_url = Column(String, nullable=True)
    group_title = Column(String, nullable=True)
    stream_url = Column(String, nullable=False)

    country = Column(
        String,
        nullable=True,
        index=True,
    )

    language = Column(
        String,
        nullable=True,
        index=True,
    )

    category = Column(
        String,
        nullable=True,
        index=True,
    )

    epg_channel_id = Column(
        Integer,
        ForeignKey("epg_channels.id"),
        nullable=True,
        index=True,
    )

    playlist = relationship(
        "Playlist",
        back_populates="channels",
    )

    epg_channel = relationship(
        "EPGChannel",
        lazy="joined",
    )