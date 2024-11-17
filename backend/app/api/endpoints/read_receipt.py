from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.crud.read_receipt import create_read_receipt, get_read_receipts_for_message, get_read_receipts_for_user
from app.schemas.read_receipt import ReadReceiptCreate, ReadReceiptRead
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=ReadReceiptRead)
def create_new_read_receipt(receipt: ReadReceiptCreate, db: Session = Depends(get_db)):
    return create_read_receipt(db, receipt)

@router.get("/message/{message_id}", response_model=list[ReadReceiptRead])
def read_receipts_for_message(message_id: UUID, db: Session = Depends(get_db)):
    return get_read_receipts_for_message(db, message_id)

@router.get("/user/{user_id}", response_model=list[ReadReceiptRead])
def read_receipts_for_user(user_id: UUID, db: Session = Depends(get_db)):
    return get_read_receipts_for_user(db, user_id)