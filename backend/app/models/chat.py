import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.sessions import Base
from datetime import datetime


id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
user1_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
user2_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
last_mesage = Column(String)
last_updated = Column(DateTime, default=datetime.now(datetime.UTC))

user1 = relationship("Users", foreign_keys=[user1_id])
user2 = relationship("Users", foreign_keys=[user2_id])
message = relationship("Message", back_populates="chat")
