from openstream.database.base import Base
from openstream.database.session import engine

from openstream.models.channel import Channel
from openstream.models.playlist import Playlist


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
