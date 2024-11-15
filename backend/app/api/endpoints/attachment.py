
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.crud.attachment import create_attachment, get_attachment, update_attachment, delete_attachment
from app.schemas.attachment import AttachmentCreate, AttachmentRead, AttachmentUpdate
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=AttachmentRead)
def create_new_attachment(attachment: AttachmentCreate, db: Session = Depends(get_db)):
    return create_attachment(db, attachment)

@router.get("/{attachment_id}", response_model=AttachmentRead)
def read_attachment(attachment_id: UUID, db: Session = Depends(get_db)):
    attachment = get_attachment(db, attachment_id)
    if not attachment:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return attachment

@router.put("/{attachment_id}", response_model=AttachmentRead)
def update_existing_attachment(attachment_id: UUID, attachment_update: AttachmentUpdate, db: Session = Depends(get_db)):
    updated_attachment = update_attachment(db, attachment_id, attachment_update)
    if not updated_attachment:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return updated_attachment

@router.delete("/{attachment_id}", response_model=dict)
def delete_existing_attachment(attachment_id: UUID, db: Session = Depends(get_db)):
    success = delete_attachment(db, attachment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Attachment not found")
    return {"message": "Attachment deleted successfully"}