from fastapi import APIRouter, Depends
from sqlalchemy import distinct
from sqlalchemy.orm import Session

from openstream.api.dependencies import get_db
from openstream.models.channel import Channel

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"],
)


@router.get("/categories")
def categories(db: Session = Depends(get_db)):
    rows = (
        db.query(distinct(Channel.category))
        .filter(Channel.category.is_not(None))
        .order_by(Channel.category)
        .all()
    )

    return [r[0] for r in rows]


@router.get("/countries")
def countries(db: Session = Depends(get_db)):
    rows = (
        db.query(distinct(Channel.country))
        .filter(Channel.country.is_not(None))
        .order_by(Channel.country)
        .all()
    )

    return [r[0] for r in rows]


@router.get("/languages")
def languages(db: Session = Depends(get_db)):
    rows = (
        db.query(distinct(Channel.language))
        .filter(Channel.language.is_not(None))
        .order_by(Channel.language)
        .all()
    )

    return [r[0] for r in rows]


@router.get("/groups")
def groups(db: Session = Depends(get_db)):
    rows = (
        db.query(distinct(Channel.group_title))
        .filter(Channel.group_title.is_not(None))
        .order_by(Channel.group_title)
        .all()
    )

    return [r[0] for r in rows]
