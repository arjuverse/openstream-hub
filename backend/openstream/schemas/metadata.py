from pydantic import BaseModel


class MetadataItem(BaseModel):
    name: str
    count: int


class StatsResponse(BaseModel):
    playlists: int
    channels: int
    countries: int
    languages: int
    categories: int