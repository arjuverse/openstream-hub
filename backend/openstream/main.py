from fastapi import FastAPI
from sqlalchemy import text
from openstream.core.config import settings
from openstream.routers.channels import router as channels_router
from openstream.routers.playlists import router as playlists_router
from openstream.routers.metadata import router as metadata_router
from openstream.database.base import Base
from openstream.database.session import engine
from fastapi.middleware.cors import CORSMiddleware

import openstream.models.epg_channel
import openstream.models.programme

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for legal public IPTV streams.",
)

app.include_router(channels_router)
app.include_router(playlists_router)
app.include_router(metadata_router)


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


@app.get("/debug/db")
def debug_db():
    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM channels")).scalar()

    return {
        "database": str(settings.database_url),
        "channels": count,
    }


@app.get("/debug/channels")
def debug_channels():
    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM channels")).scalar()
        first = conn.execute(text("SELECT id, name FROM channels LIMIT 5")).fetchall()

    return {
        "count": count,
        "first": [tuple(row) for row in first],
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://localhost",
        "http://127.0.0.1",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)