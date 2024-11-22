from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.schemas.auth import Login, Token
from app.schemas.user import UserCreate
from app.crud.user import get_user_by_email, create_user
from app.core.security import Security

router = APIRouter()


@router.post("/register", response_model=Token)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    
    user_data.password = Security.hash_password(user_data.password)
    user = create_user(db, user_data)
    
    access_token = Security.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login(credentials: Login, db: Session = Depends(get_db)):
    """Login and get a JWT token."""
    user = get_user_by_email(db, credentials.email)
    if not user or not Security.verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = Security.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
