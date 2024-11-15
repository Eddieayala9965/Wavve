from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ChatCreate(BaseModel):
    user1_id: UUID
    user2_id: UUID

class ChatRead(BaseModel):
    id: UUID
    user1_id: UUID
    user2_id: UUID
    last_message: str
    last_update: datetime
    
    class Config:
        orm_mode = True