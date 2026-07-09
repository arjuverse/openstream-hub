from openstream.models.channel import Channel
from openstream.repositories.channel_repository import ChannelRepository


class ChannelService:
    def __init__(self, repository: ChannelRepository):
        self.repository = repository

    def get_all(self) -> list[Channel]:
        return self.repository.get_all()

    def get(self, channel_id: int) -> Channel | None:
        return self.repository.get(channel_id)
