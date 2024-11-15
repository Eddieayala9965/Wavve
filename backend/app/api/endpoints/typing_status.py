from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.crud.typing_status import set_typing_status, get_typing_status
from app.schemas.typing_status import TypingStatusCreate, TypingStatusRead
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=TypingStatusRead)
def set_user_typing_status(status: TypingStatusCreate, db: Session = Depends(get_db)):
    return set_typing_status(db, status)

@router.get("/{user_id}", response_model=TypingStatusRead)
def read_typing_status(user_id: UUID, db: Session = Depends(get_db)):
    return get_typing_status(db, user_id)