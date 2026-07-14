from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
def root():
    return {
        "application": "OpenStream Hub",
        "version": "0.1.0",
        "status": "running",
    }


@router.get("/health")
def health():
    return {
        "status": "ok",
    }
