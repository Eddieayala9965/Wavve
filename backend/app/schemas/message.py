from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class MessageCreate(BaseModel):
    sender_id: UUID
    receiver_id: UUID
    content: str

class MessageRead(BaseModel):
    id: UUID
    sender_id: UUID
    receiver_id: UUID
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True

class MessageUpdate(BaseModel):
    content: Optional[str] = None

