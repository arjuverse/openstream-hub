from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from openstream.database.session import SessionLocal
from openstream.repositories.channel_repository import ChannelRepository
from openstream.schemas.channel import (
    ChannelResponse,
    PaginatedChannelResponse,
)
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


def get_service(db: Session):
    return ChannelService(ChannelRepository(db))


@router.get("/", response_model=PaginatedChannelResponse)
def list_channels(
    page: int = 1,
    size: int = 24,
    search: str | None = None,
    group: str | None = None,
    category: str | None = None,
    matched: bool | None = None,
    sort: str = "name",
    order: str = "asc",
    db: Session = Depends(get_db),
):
    service = get_service(db)

    return service.get_channels(
        page=page,
        size=size,
        search=search,
        group=group,
        category=category,
        matched=matched,
        sort=sort,
        order=order,
    )


@router.get("/categories", response_model=list[str])
def list_categories(
    db: Session = Depends(get_db),
):
    service = get_service(db)
    return service.get_categories()


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