from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from openstream.api.routers import metadata
from openstream.api.routers import (
    channels,
    epg,
    playlists,
    system,
)

app = FastAPI(
    title="OpenStream Hub",
    version="0.1.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system.router)
app.include_router(channels.router)
app.include_router(epg.router)
app.include_router(playlists.router)
app.include_router(metadata.router)