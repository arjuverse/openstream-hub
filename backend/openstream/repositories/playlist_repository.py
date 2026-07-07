from sqlalchemy.orm import Session

from openstream.models.playlist import Playlist


def get_by_url(db: Session, url: str) -> Playlist | None:
    return db.query(Playlist).filter(Playlist.url == url).first()


def create_playlist(db: Session, name: str, url: str) -> Playlist:
    playlist = Playlist(name=name, url=url)
    db.add(playlist)
    db.commit()
    db.refresh(playlist)
    return playlist
