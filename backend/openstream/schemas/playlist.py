from pydantic import BaseModel, HttpUrl


class PlaylistImportRequest(BaseModel):
    name: str
    url: HttpUrl


class PlaylistImportResponse(BaseModel):
    playlist_name: str
    total_found: int
    imported: int
    skipped_duplicates: int
