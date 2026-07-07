from sqlalchemy.orm import Session

from openstream.models.channel import Channel
from openstream.schemas.channel import ParsedChannel


def exists_by_stream_url(db: Session, stream_url: str) -> bool:
    return db.query(Channel).filter(Channel.stream_url == stream_url).first() is not None


def create_channel(
    db: Session,
    channel_data: ParsedChannel,
    playlist_id: int,
) -> Channel:
    channel = Channel(
        name=channel_data.name,
        stream_url=channel_data.stream_url,
        logo_url=channel_data.logo_url,
        category=channel_data.category,
        country=channel_data.country,
        language=channel_data.language,
        tvg_id=channel_data.tvg_id,
        tvg_name=channel_data.tvg_name,
        group_title=channel_data.group_title,
        playlist_id=playlist_id,
    )

    db.add(channel)
    db.commit()
    db.refresh(channel)
    return channel
