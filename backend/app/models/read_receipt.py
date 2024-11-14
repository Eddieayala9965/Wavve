import uuid
from sqlalchemy import Column, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.db.sessions import Base
from datetime import datetime

class ReadReceipt(Base):
    __tablename__ = "read_receipts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    message_id = Column(UUID(as_uuid=True), ForeignKey("messages.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime, default=datetime.now(datetime.UTC))