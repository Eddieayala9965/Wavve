from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional

class User(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
