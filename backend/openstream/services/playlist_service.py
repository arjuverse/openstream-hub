import requests
from sqlalchemy.orm import Session

from openstream.repositories import channel_repository, playlist_repository
from openstream.schemas.playlist import PlaylistImportRequest, PlaylistImportResponse
from openstream.services.m3u_parser import parse_m3u


def import_playlist(
    db: Session,
    payload: PlaylistImportRequest,
) -> PlaylistImportResponse:
    url = str(payload.url)

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    parsed_channels = parse_m3u(response.text)

    playlist = playlist_repository.get_by_url(db, url)

    if playlist is None:
        playlist = playlist_repository.create_playlist(
            db=db,
            name=payload.name,
            url=url,
        )

    imported = 0
    skipped = 0

    for channel in parsed_channels:
        if channel_repository.exists_by_stream_url(db, channel.stream_url):
            skipped += 1
            continue

        channel_repository.create_channel(
            db=db,
            channel_data=channel,
            playlist_id=playlist.id,
        )
        imported += 1

    return PlaylistImportResponse(
        playlist_name=playlist.name,
        total_found=len(parsed_channels),
        imported=imported,
        skipped_duplicates=skipped,
    )
