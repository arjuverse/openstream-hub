from fastapi import APIRouter

router = APIRouter(
    prefix="/playlists",
    tags=["Playlists"],
)


@router.get("")
def list_playlists():

    return {
        "message": "Coming in Sprint 5.3"
    }
