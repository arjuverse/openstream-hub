from sqlalchemy.orm import Session

from openstream.models.channel import Channel
from openstream.models.playlist import Playlist
from openstream.repositories.channel_repository import ChannelRepository
from openstream.repositories.playlist_repository import PlaylistRepository
from openstream.schemas.imports import (
    PlaylistImportRequest,
    PlaylistImportResponse,
)
from openstream.services.downloader import download_playlist
from openstream.utils.m3u_parser import parse_m3u


def import_playlist(
    db: Session,
    payload: PlaylistImportRequest,
) -> PlaylistImportResponse:
    playlist_repo = PlaylistRepository(db)
    channel_repo = ChannelRepository(db)

    existing = playlist_repo.get_by_url(payload.url)

    if existing:
        return PlaylistImportResponse(
            playlist_id=existing.id,
            playlist_name=existing.name,
            channels_imported=0,
        )

    content = download_playlist(payload.url)
    parsed_channels = parse_m3u(content)

    playlist = Playlist(
        name=payload.name,
        url=payload.url,
    )

    playlist_repo.create(playlist)

    imported = 0

    for item in parsed_channels:
        channel = Channel(
            name=item.get("name", "Unknown"),
            stream_url=item["stream_url"],
            tvg_id=item.get("tvg-id"),
            tvg_name=item.get("tvg-name"),
            logo_url=item.get("tvg-logo"),
            group_title=item.get("group-title"),
            playlist_id=playlist.id,
        )

        channel_repo.create(channel)
        imported += 1

    channel_repo.commit()

    return PlaylistImportResponse(
        playlist_id=playlist.id,
        playlist_name=playlist.name,
        channels_imported=imported,
    )
