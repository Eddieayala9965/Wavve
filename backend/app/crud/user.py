from sqlalchemy.orm import Session
from uuid import UUID
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.security import hash_password

def create_user(db: Session, user: UserCreate) -> UserRead:
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserRead.model_validate(db_user)

def get_user_by_id(db: Session, user_id: UUID) -> UserRead:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    return UserRead.model_validate(db_user)

def get_user_by_email(db: Session, email: str) -> UserRead:
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        return None
    return UserRead.model_validate(db_user)

def update_user(db: Session, user_id: UUID, user_update: UserUpdate) -> UserRead:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    for key, value in user_update.model_dump(exclude_unset=True).items():
        if key == "password":
            value = hash_password(value)
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return UserRead.model_validate(db_user)

def delete_user(db: Session, user_id: UUID) -> bool:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True