from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password
from app.core.config import settings

def init_db(db: Session):
    admin_email = settings.ADMIN_EMAIL
    admin_password = settings.ADMIN_PASSWORD
    
    admin_user = db.query(User).filter(User.email == admin_email).first()
    
    if not admin_user:
        admin_user = User(
            email=admin_email, 
            hash_password=hash_password(admin_password)
        )
        db.add(admin_user)
        db.commit()
        print("Admin user created")
    else:
        print("Admin user already exists")    