def parse_m3u(content: str) -> list[dict]:
    """
    Parse an M3U playlist into channel dictionaries.
    """

    channels = []

    current = None

    for line in content.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("#EXTINF"):
            current = _parse_extinf(line)

        elif not line.startswith("#") and current:
            current["stream_url"] = line
            channels.append(current)
            current = None

    return channels


def _parse_extinf(line: str) -> dict:
    metadata = {}

    info, name = line.split(",", 1)

    metadata["name"] = name.strip()

    for token in info.split():
        if "=" not in token:
            continue

        key, value = token.split("=", 1)

        metadata[key] = value.strip('"')

    return metadata
