from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ReadReceiptCreate(BaseModel):
    message_id: UUID
    user_id: UUID
    is_read: bool

class ReadReceiptRead(BaseModel):
    id: UUID
    message_id: UUID
    user_id: UUID
    is_read: bool
    read_at: datetime

    class Config:
        from_attributes = True

