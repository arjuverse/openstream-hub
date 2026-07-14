from pydantic import BaseModel, ConfigDict


class ChannelResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    stream_url: str

    tvg_id: str | None = None
    tvg_name: str | None = None

    logo_url: str | None = None

    group_title: str | None = None
    category: str | None = None

    country: str | None = None
    language: str | None = None

    playlist_id: int
    epg_channel_id: int | None = None


class PaginatedChannelResponse(BaseModel):
    items: list[ChannelResponse]

    page: int
    size: int
    total: int
    pages: int