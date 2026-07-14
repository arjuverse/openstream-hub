import re

REMOVE_WORDS = [
    "hd",
    "fhd",
    "uhd",
    "4k",
    "1080p",
    "720p",
    "576p",
    "540p",
    "480p",
    "sd",
    ".in",
    "channel",
    "tv",
    "television",
    "live",
]


def normalize(name: str) -> str:
    if not name:
        return ""

    name = name.lower()

    name = name.replace("&", "and")

    name = re.sub(r"\([^)]*\)", "", name)

    for word in REMOVE_WORDS:
        name = name.replace(word, "")

    name = re.sub(r"[^a-z0-9]", "", name)

    return name.strip()