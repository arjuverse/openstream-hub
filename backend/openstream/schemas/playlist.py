from pydantic import BaseModel, HttpUrl


class PlaylistCreate(BaseModel):
    name: str
    url: HttpUrl


class PlaylistUpdate(BaseModel):
    name: str
    url: HttpUrl


class PlaylistResponse(BaseModel):
    id: int
    name: str
    url: str

    model_config = {"from_attributes": True}
