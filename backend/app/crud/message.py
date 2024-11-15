from sqlalchemy.orm import Session
from uuid import UUID
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageRead, MessageUpdate

def create_message(db: Session, message: MessageCreate) -> MessageRead:
    db_message = Message(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return MessageRead.model_validate(db_message)

def get_message(db: Session, message_id: UUID) -> MessageRead:
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if not db_message:
        return None
    return MessageRead.model_validate(db_message)

def update_message(db: Session, message_id: UUID, message_update: MessageUpdate) -> MessageRead:
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if not db_message:
        return None
    for key, value in message_update.model_dump(exclude_unset=True).items():
        setattr(db_message, key, value)
    db.commit()
    db.refresh(db_message)
    return MessageRead.model_validate(db_message)

def delete_message(db: Session, message_id: UUID) -> bool:
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if not db_message:
        return False
    db.delete(db_message)
    db.commit()
    return True