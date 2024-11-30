from pydantic import BaseModel, EmailStr
from typing import Dict


class Login(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    user: Dict[str, str]  
