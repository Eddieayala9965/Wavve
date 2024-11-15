from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional

class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    username: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    auth0_id: Optional[str] = None  # Optional field for mapping Auth0 ID

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None