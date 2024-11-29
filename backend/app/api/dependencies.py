from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.sessions import SessionLocal
from app.crud.user import get_user_by_id
from app.core.security import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")  

def get_db():
    """
    Provides a database session for requests.
    Ensures proper session closing after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    """
    Retrieves the current authenticated user based on the JWT token.

    Args:
        db: The database session.
        token: The JWT token verified by `decode_access_token`.

    Returns:
        The current user object from the database.

    Raises:
        HTTPException: If the token or user is invalid.
    """
    try:
        payload = decode_access_token(token)  # Decode the JWT token
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        user = get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
