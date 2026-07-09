from sqlalchemy.orm import Session

from openstream.models.playlist import Playlist


class PlaylistRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Playlist).all()

    def get(self, playlist_id: int):
        return self.db.query(Playlist).filter(Playlist.id == playlist_id).first()

    def create(self, playlist: Playlist):
        self.db.add(playlist)
        self.db.commit()
        self.db.refresh(playlist)
        return playlist

    def delete(self, playlist: Playlist):
        self.db.delete(playlist)
        self.db.commit()

    def get_by_url(self, url: str):
        return self.db.query(Playlist).filter(Playlist.url == url).first()
