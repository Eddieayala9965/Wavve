from sqlalchemy.orm import Session
from uuid import UUID
from app.models.attachment import Attachment
from app.schemas.attachment import AttachmentCreate, AttachmentRead, AttachmentUpdate

def create_attachment(db: Session, attachment: AttachmentCreate) -> AttachmentRead:
    db_attachment = Attachment(**attachment.model_dump())
    db.add(db_attachment)
    db.commit()
    db.refresh(db_attachment)
    return AttachmentRead.model_validate(db_attachment)

def get_attachment(db: Session, attachment_id: UUID) -> AttachmentRead:
    db_attachment = db.query(Attachment).filter(Attachment.id == attachment_id).first()
    if not db_attachment:
        return None
    return AttachmentRead.model_validate(db_attachment)

def update_attachment(db: Session, attachment_id: UUID, attachment_update: AttachmentUpdate) -> AttachmentRead:
    db_attachment = db.query(Attachment).filter(Attachment.id == attachment_id).first()
    if not db_attachment:
        return None
    for key, value in attachment_update.model_dump(exclude_unset=True).items():
        setattr(db_attachment, key, value)
    db.commit()
    db.refresh(db_attachment)
    return AttachmentRead.model_validate(db_attachment)

def delete_attachment(db: Session, attachment_id: UUID) -> bool:
    db_attachment = db.query(Attachment).filter(Attachment.id == attachment_id).first()
    if not db_attachment:
        return False
    db.delete(db_attachment)
    db.commit()
    return True