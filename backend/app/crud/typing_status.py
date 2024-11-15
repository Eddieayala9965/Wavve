from sqlalchemy.orm import Session
from uuid import UUID
from app.models.typing_status import TypingStatus
from app.schemas.typing_status import TypingStatusCreate, TypingStatusRead

def set_typing_status(db: Session, typing_status: TypingStatusCreate) -> TypingStatusRead:
    db_status = db.query(TypingStatus).filter(TypingStatus.user_id == typing_status.user_id).first()
    if not db_status:
        db_status = TypingStatus(**typing_status.model_dump())
        db.add(db_status)
    else:
        db_status.is_typing = typing_status.is_typing
    db.commit()
    db.refresh(db_status)
    return TypingStatusRead.model_validate(db_status)

def get_typing_status(db: Session, user_id: UUID) -> TypingStatusRead:
    db_status = db.query(TypingStatus).filter(TypingStatus.user_id == user_id).first()
    if not db_status:
        return None
    return TypingStatusRead.model_validate(db_status)