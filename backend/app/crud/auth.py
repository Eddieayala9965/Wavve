from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.crud.user import get_user_by_email, create_user

def register_user(db: Session, token_payload: dict) -> UserRead:
    """
    Register a user in the database if they don't already exist.

    Args:
        db (Session): The database session.
        token_payload (dict): Decoded Auth0 token payload.

    Returns:
        UserRead: The user object.
    """
    email = token_payload.get("email")
    username = token_payload.get("nickname") or token_payload.get("name")  

    if not email:
        raise ValueError("Token does not contain an email address.")


    user = get_user_by_email(db, email)
    if user:
        return user


    user_create = UserCreate(email=email, username=username, password="")  
    return create_user(db, user_create)
