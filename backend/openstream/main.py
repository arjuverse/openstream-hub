from fastapi import FastAPI

from openstream.routers.playlists import router as playlists_router
from openstream.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for legal public IPTV streams.",
)

app.include_router(playlists_router)


@app.get("/")
def root():
    return {
        "message": "OpenStream Hub API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
    }
