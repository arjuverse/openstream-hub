from abc import ABC


class EPGProvider(ABC):
    name: str
    url: str
    filename: str