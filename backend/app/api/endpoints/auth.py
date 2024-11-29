from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.crud.user import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token
from app.api.dependencies import get_db
from app.schemas.auth import Login, Token

router = APIRouter()


@router.post("/register", response_model=UserRead)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    hashed_password = hash_password(user_data.password)
    user_data.password = hashed_password
    return create_user(db, user_data)


@router.post("/login", response_model=Token)
def login(credentials: Login, db: Session = Depends(get_db)):
    """
    Login endpoint to authenticate a user and return a JWT token.
    """
    user = get_user_by_email(db, credentials.email)
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
