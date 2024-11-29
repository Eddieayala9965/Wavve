from sqlalchemy.orm import Session
from uuid import UUID
from app.models.chat import Chat
from app.models.user import User
from app.schemas.chat import ChatCreate, ChatRead


def create_chat(db: Session, chat: ChatCreate) -> ChatRead:
    # Resolve usernames to user IDs
    user1 = db.query(User).filter(User.username == chat.user1_username).first()
    user2 = db.query(User).filter(User.username == chat.user2_username).first()

    if not user1 or not user2:
        raise ValueError("One or both users not found")

    # Create the chat using resolved IDs
    db_chat = Chat(
        user1_id=user1.id,
        user2_id=user2.id,
        name=chat.name or f"Chat between {user1.username} and {user2.username}",
    )
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
