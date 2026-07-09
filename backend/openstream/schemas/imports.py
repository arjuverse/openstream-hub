from pydantic import BaseModel


class PlaylistImportRequest(BaseModel):
    name: str
    url: str


class PlaylistImportResponse(BaseModel):
    playlist_id: int
    playlist_name: str
    channels_imported: int
