from fastapi import APIRouter

router = APIRouter(
    prefix="/epg",
    tags=["EPG"],
)


@router.get("")
def list_epg():

    return {
        "message": "Coming in Sprint 5.2"
    }
