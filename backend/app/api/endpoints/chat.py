from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.crud.chat import create_chat, get_chat_by_id, get_user_chats
from app.schemas.chat import ChatCreate, ChatRead
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=ChatRead)
def create_new_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    return create_chat(db, chat)

@router.get("/{chat_id}", response_model=ChatRead)
def read_chat(chat_id: UUID, db: Session = Depends(get_db)):
    chat = get_chat_by_id(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

@router.get("/user/{user_id}", response_model=list[ChatRead])
def get_chats_for_user(user_id: UUID, db: Session = Depends(get_db)):
    return get_user_chats(db, user_id)