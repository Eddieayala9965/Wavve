from sqlalchemy.orm import Session
from uuid import UUID
from app.models.chat import Chat
from app.schemas.chat import ChatCreate, ChatRead

def create_chat(db: Session, chat: ChatCreate) -> ChatRead:
    db_chat = Chat(**chat.model_dump())
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return ChatRead.model_validate(db_chat)

def get_chat_by_id(db: Session, chat_id: UUID) -> ChatRead:
    db_chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not db_chat:
        return None
    return ChatRead.model_validate(db_chat)

def get_user_chats(db: Session, user_id: UUID) -> list[ChatRead]:
    db_chats = db.query(Chat).filter(
        (Chat.user1_id == user_id) | (Chat.user2_id == user_id)
    ).all()
    return [ChatRead.model_validate(chat) for chat in db_chats]