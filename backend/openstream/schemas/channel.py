from pydantic import BaseModel


class ParsedChannel(BaseModel):
    name: str
    stream_url: str
    logo_url: str | None = None
    category: str | None = None
    country: str | None = None
    language: str | None = None
    tvg_id: str | None = None
    tvg_name: str | None = None
    group_title: str | None = None
