from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# from app.models.user import User
# from app.models.message import Message
# from app.models.chat import Chat
# from app.models.read_receipt import ReadReceipt
# from app.models.typing_status import TypingStatus
# from app.models.attachment import Attachment


