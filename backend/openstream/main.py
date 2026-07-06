from fastapi import FastAPI

from openstream.core.config import settings
from openstream.database.init_db import init_db

init_db()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for legal public IPTV streams.",
)


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