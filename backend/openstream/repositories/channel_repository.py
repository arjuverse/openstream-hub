from sqlalchemy.orm import Session

from openstream.models.channel import Channel


class ChannelRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, channel: Channel) -> None:
        self.db.add(channel)

    def commit(self) -> None:
        self.db.commit()

    def get_all(self) -> list[Channel]:
        return self.db.query(Channel).order_by(Channel.name).all()

    def get(self, channel_id: int) -> Channel | None:
        return self.db.query(Channel).filter(Channel.id == channel_id).first()
