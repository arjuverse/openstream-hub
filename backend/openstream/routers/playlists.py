from fastapi import APIRouter, Depends, HTTPException
from requests import RequestException
from sqlalchemy.orm import Session

from openstream.database.session import SessionLocal
from openstream.schemas.playlist import PlaylistImportRequest, PlaylistImportResponse
from openstream.services.playlist_service import import_playlist

router = APIRouter(prefix="/playlists", tags=["Playlists"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/import", response_model=PlaylistImportResponse)
def import_playlist_endpoint(
    payload: PlaylistImportRequest,
    db: Session = Depends(get_db),
):
    try:
        return import_playlist(db=db, payload=payload)
    except RequestException as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Could not download playlist: {exc}",
        ) from exc
