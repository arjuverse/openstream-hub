from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from openstream.database.session import SessionLocal
from openstream.repositories.channel_repository import ChannelRepository
from openstream.schemas.channel import ChannelResponse
from openstream.services.channel_service import ChannelService

router = APIRouter(
    prefix="/channels",
    tags=["Channels"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_service(db: Session) -> ChannelService:
    return ChannelService(ChannelRepository(db))


@router.get("/", response_model=list[ChannelResponse])
def list_channels(
    db: Session = Depends(get_db),
):
    service = get_service(db)
    return service.get_all()


@router.get("/{channel_id}", response_model=ChannelResponse)
def get_channel(
    channel_id: int,
    db: Session = Depends(get_db),
):
    service = get_service(db)

    channel = service.get(channel_id)

    if channel is None:
        raise HTTPException(
            status_code=404,
            detail="Channel not found",
        )

    return channel
