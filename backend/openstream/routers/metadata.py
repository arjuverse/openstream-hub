from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from openstream.database.session import SessionLocal
from openstream.repositories.metadata_repository import MetadataRepository
from openstream.schemas.metadata import (
    MetadataItem,
    StatsResponse,
)
from openstream.services.metadata_service import MetadataService

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_service(db: Session):
    return MetadataService(
        MetadataRepository(db)
    )


@router.get(
    "/stats",
    response_model=StatsResponse,
)
def stats(
    db: Session = Depends(get_db),
):
    return get_service(db).stats()


@router.get(
    "/categories",
    response_model=list[MetadataItem],
)
def categories(
    db: Session = Depends(get_db),
):
    return get_service(db).categories()


@router.get(
    "/countries",
    response_model=list[MetadataItem],
)
def countries(
    db: Session = Depends(get_db),
):
    return get_service(db).countries()


@router.get(
    "/languages",
    response_model=list[MetadataItem],
)
def languages(
    db: Session = Depends(get_db),
):
    return get_service(db).languages()