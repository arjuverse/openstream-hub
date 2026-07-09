from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from openstream.database.session import SessionLocal
from openstream.repositories.playlist_repository import PlaylistRepository
from openstream.schemas.playlist import (
    PlaylistCreate,
    PlaylistResponse,
)
from openstream.services.playlist_service import PlaylistService

router = APIRouter(prefix="/playlists", tags=["Playlists"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_service(db: Session):
    return PlaylistService(PlaylistRepository(db))


@router.get("/", response_model=list[PlaylistResponse])
def list_playlists(
    db: Session = Depends(get_db),
):
    service = get_service(db)
    return service.get_all()


@router.post("/", response_model=PlaylistResponse)
def create_playlist(
    payload: PlaylistCreate,
    db: Session = Depends(get_db),
):
    service = get_service(db)
    return service.create(payload)


@router.get("/{playlist_id}", response_model=PlaylistResponse)
def get_playlist(
    playlist_id: int,
    db: Session = Depends(get_db),
):
    service = get_service(db)

    playlist = service.get(playlist_id)

    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist not found")

    return playlist


@router.delete("/{playlist_id}")
def delete_playlist(
    playlist_id: int,
    db: Session = Depends(get_db),
):
    service = get_service(db)

    playlist = service.get(playlist_id)

    if playlist is None:
        raise HTTPException(status_code=404, detail="Playlist not found")

    service.delete(playlist)

    return {"message": "Playlist deleted"}
