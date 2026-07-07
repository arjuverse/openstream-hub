import re

from openstream.schemas.channel import ParsedChannel


def _extract_attr(line: str, attr: str) -> str | None:
    match = re.search(rf'{attr}="([^"]*)"', line)
    return match.group(1).strip() if match else None


def parse_m3u(text: str) -> list[ParsedChannel]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    channels: list[ParsedChannel] = []

    for index, line in enumerate(lines):
        if not line.startswith("#EXTINF"):
            continue

        if index + 1 >= len(lines):
            continue

        stream_url = lines[index + 1]

        if not stream_url.startswith("http"):
            continue

        name = line.split(",")[-1].strip()

        if not name:
            name = _extract_attr(line, "tvg-name") or "Unknown Channel"

        group_title = _extract_attr(line, "group-title")

        channels.append(
            ParsedChannel(
                name=name,
                stream_url=stream_url,
                logo_url=_extract_attr(line, "tvg-logo"),
                category=group_title,
                country=_extract_attr(line, "tvg-country"),
                language=_extract_attr(line, "tvg-language"),
                tvg_id=_extract_attr(line, "tvg-id"),
                tvg_name=_extract_attr(line, "tvg-name"),
                group_title=group_title,
            )
        )

    return channels
