from fastapi import FastAPI

from openstream.core.config import settings
from openstream.routers.channels import router as channels_router
from openstream.routers.playlists import router as playlists_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for legal public IPTV streams.",
)

app.include_router(channels_router)
app.include_router(playlists_router)


@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    return {
        "message": "OpenStream Hub API is running",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
    }
