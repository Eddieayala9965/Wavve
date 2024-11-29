from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class ChatCreate(BaseModel):
    user1_username: str
    user2_username: str
    name: Optional[str] = None


class ChatRead(BaseModel):
    id: UUID
    user1_id: UUID
    user2_id: UUID
    name: str

    class Config:
        from_attributes = True