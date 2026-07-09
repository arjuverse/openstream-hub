import httpx
from sqlalchemy.orm import Session

from openstream.repositories import channel_repository, playlist_repository
from openstream.schemas.channel import ParsedChannel
from openstream.schemas.playlist import PlaylistImportRequest, PlaylistImportResponse
from openstream.services.m3u_parser import parse_m3u


def _download_playlist(url: str) -> str:
    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        response = client.get(url)
        response.raise_for_status()
        return response.text


def _deduplicate_parsed_channels(
    channels: list[ParsedChannel],
) -> list[ParsedChannel]:
    seen: set[str] = set()
    unique_channels: list[ParsedChannel] = []

    for channel in channels:
        if channel.stream_url in seen:
            continue

        seen.add(channel.stream_url)
        unique_channels.append(channel)

    return unique_channels


def import_playlist(
    db: Session,
    payload: PlaylistImportRequest,
) -> PlaylistImportResponse:
    url = str(payload.url)

    playlist_text = _download_playlist(url)
    parsed_channels = parse_m3u(playlist_text)
    unique_channels = _deduplicate_parsed_channels(parsed_channels)

    playlist = playlist_repository.get_by_url(db, url)

    if playlist is None:
        playlist = playlist_repository.create_playlist(
            db=db,
            name=payload.name,
            url=url,
        )

    stream_urls = [channel.stream_url for channel in unique_channels]

    existing_urls = channel_repository.get_existing_stream_urls(
        db=db,
        stream_urls=stream_urls,
    )

    channels_to_insert = [
        channel
        for channel in unique_channels
        if channel.stream_url not in existing_urls
    ]

    imported = channel_repository.bulk_create_channels(
        db=db,
        channels=channels_to_insert,
        playlist_id=playlist.id,
    )

    skipped_duplicates = len(parsed_channels) - imported

    return PlaylistImportResponse(
        playlist_name=playlist.name,
        total_found=len(parsed_channels),
        imported=imported,
        skipped_duplicates=skipped_duplicates,
    )
