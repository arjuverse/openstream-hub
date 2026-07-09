from sqlalchemy.orm import Session

from openstream.models.channel import Channel
from openstream.schemas.channel import ParsedChannel


def get_existing_stream_urls(db: Session, stream_urls: list[str]) -> set[str]:
    if not stream_urls:
        return set()

    rows = (
        db.query(Channel.stream_url).filter(Channel.stream_url.in_(stream_urls)).all()
    )

    return {row[0] for row in rows}


def bulk_create_channels(
    db: Session,
    channels: list[ParsedChannel],
    playlist_id: int,
) -> int:
    objects = [
        Channel(
            name=channel.name,
            stream_url=channel.stream_url,
            logo_url=channel.logo_url,
            category=channel.category,
            country=channel.country,
            language=channel.language,
            tvg_id=channel.tvg_id,
            tvg_name=channel.tvg_name,
            group_title=channel.group_title,
            playlist_id=playlist_id,
        )
        for channel in channels
    ]

    db.add_all(objects)
    db.commit()

    return len(objects)
