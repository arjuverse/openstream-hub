from dataclasses import dataclass


@dataclass
class EPGProvider:
    name: str
    url: str
    filename: str


PROVIDERS = [
    EPGProvider(
        name="India",
        url="",
        filename="india.xml",
    ),
    EPGProvider(
        name="UK",
        url="",
        filename="uk.xml",
    ),
    EPGProvider(
        name="USA",
        url="",
        filename="usa.xml",
    ),
    EPGProvider(
        name="Sports",
        url="",
        filename="sports.xml",
    ),
]