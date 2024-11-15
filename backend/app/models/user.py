from sqlalchemy import Column, String, UUID
from app.db.base import Base

class User(Base):
    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    auth0_id = Column(String, unique=True, nullable=True) 