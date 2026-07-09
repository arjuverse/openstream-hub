from pydantic import BaseModel


class ChannelResponse(BaseModel):
    id: int
    name: str
    stream_url: str
    logo_url: str | None
    country: str | None
    language: str | None
    category: str | None

    model_config = {
        "from_attributes": True,
    }
