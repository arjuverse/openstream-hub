import re
from datetime import datetime

COUNTRY_SUFFIX = re.compile(r"\.[a-z]{2,3}$", re.IGNORECASE)

QUALITY = re.compile(
    r"\b(?:240p|360p|480p|540p|576p|720p|1080p|2160p|4k|uhd|fhd|hd|sd)\b",
    re.IGNORECASE,
)

BRACKETS = re.compile(r"\(.*?\)|\[.*?\]")


def normalize_channel_name(name: str) -> str:
    if not name:
        return ""

    name = name.lower().strip()

    name = COUNTRY_SUFFIX.sub("", name)
    name = QUALITY.sub("", name)
    name = BRACKETS.sub("", name)

    name = re.sub(r"[^a-z0-9]", "", name)

    return name


def parse_xmltv_datetime(value: str):
    value = value.split()[0]
    return datetime.strptime(value, "%Y%m%d%H%M%S")