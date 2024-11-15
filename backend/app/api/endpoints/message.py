from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.crud.message import create_message, get_message, update_message, delete_message
from app.schemas.message import MessageCreate, MessageRead, MessageUpdate
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=MessageRead)
def create_new_message(message: MessageCreate, db: Session = Depends(get_db)):
    return create_message(db, message)

@router.get("/{message_id}", response_model=MessageRead)
def read_message(message_id: UUID, db: Session = Depends(get_db)):
    message = get_message(db, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

@router.put("/{message_id}", response_model=MessageRead)
def update_existing_message(message_id: UUID, message_update: MessageUpdate, db: Session = Depends(get_db)):
    updated_message = update_message(db, message_id, message_update)
    if not updated_message:
        raise HTTPException(status_code=404, detail="Message not found")
    return updated_message

@router.delete("/{message_id}", response_model=dict)
def delete_existing_message(message_id: UUID, db: Session = Depends(get_db)):
    success = delete_message(db, message_id)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": "Message deleted successfully"}