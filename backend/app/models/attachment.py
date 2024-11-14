import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db.sessions import Base
from datetime import datetime

class Attachment(Base):
    __tablename__ = "attachments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    message_id = Column(UUID(as_uuid=True), ForeignKey("messages.id"), nullable=True)
    file_path = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    
    uploaded_at = Column(DateTime, default=datetime.now(datetime.UTC))