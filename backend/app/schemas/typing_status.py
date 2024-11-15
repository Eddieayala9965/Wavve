from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class TypingStatusCreate(BaseModel):
    user_id: UUID
    is_typing: bool

class TypingStatusRead(BaseModel):
    id: UUID
    user_id: UUID
    is_typing: bool
    updated_at: datetime

    class Config:
        orm_mode = True

class TypingStatusUpdate(BaseModel):
    is_typing: Optional[bool] = None