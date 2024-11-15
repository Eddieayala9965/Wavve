from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class AttachmentCreate(BaseModel):
    message_id: UUID
    file_path: str
    file_type: str  

class AttachmentRead(BaseModel):
    id: UUID
    message_id: UUID
    file_path: str
    file_type: str
    uploaded_at: datetime

    class Config:
        orm_mode = True

class AttachmentUpdate(BaseModel):
    file_path: Optional[str] = None
    file_type: Optional[str] = None
