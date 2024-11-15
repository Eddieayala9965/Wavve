from sqlalchemy.orm import Session
from uuid import UUID
from app.models.read_receipt import ReadReceipt
from app.schemas.read_receipt import ReadReceiptCreate, ReadReceiptRead

def create_read_receipt(db: Session, receipt: ReadReceiptCreate) -> ReadReceiptRead:
    db_receipt = ReadReceipt(**receipt.model_dump())
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return ReadReceiptRead.model_validate(db_receipt)

def get_read_receipts_for_message(db: Session, message_id: UUID) -> list[ReadReceiptRead]:
    db_receipts = db.query(ReadReceipt).filter(ReadReceipt.message_id == message_id).all()
    return [ReadReceiptRead.model_validate(receipt) for receipt in db_receipts]

def get_read_receipts_for_user(db: Session, user_id: UUID) -> list[ReadReceiptRead]:
    db_receipts = db.query(ReadReceipt).filter(ReadReceipt.user_id == user_id).all()
    return [ReadReceiptRead.model_validate(receipt) for receipt in db_receipts]