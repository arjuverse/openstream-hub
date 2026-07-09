from openstream.models.playlist import Playlist


class PlaylistService:
    def __init__(self, repository):
        self.repository = repository

    def create(self, data):
        playlist = Playlist(**data.model_dump())
        return self.repository.create(playlist)

    def get_all(self):
        return self.repository.get_all()

    def get(self, playlist_id):
        return self.repository.get(playlist_id)

    def delete(self, playlist):
        self.repository.delete(playlist)
