from app.db.sessions import SessionLocal
from fastapi import Depends, HTTPException
from app.core.security import Security

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
def get_current_user(token: str = Depends(Security.verify_token)):
    """Retrieve the current user from the token."""
    if not token:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return token