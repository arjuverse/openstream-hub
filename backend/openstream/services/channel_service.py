from openstream.repositories.channel_repository import ChannelRepository


class ChannelService:
    def __init__(self, repository: ChannelRepository):
        self.repository = repository

    def get_channels(self, **kwargs):
        return self.repository.get_channels(**kwargs)

    def get_channel(self, channel_id: int):
        return self.repository.get(channel_id)