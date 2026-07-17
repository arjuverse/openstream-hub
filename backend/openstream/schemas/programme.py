from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ProgrammeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    
    description: str | None = None
    category: str | None = None
    
    start_time: datetime
    stop_time: datetime
    
    episode: str | None = None
    rating: str | None = None