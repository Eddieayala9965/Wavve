from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.core.auth import verify_auth0_token
from app.api.dependencies import get_db
from app.crud.user import get_user_by_id, create_user, update_user, delete_user
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the database. This is only for storing metadata.
    """
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: UUID, db: Session = Depends(get_db), current_user: dict = Depends(verify_auth0_token)):
    """
    Get user profile. Requires Auth0 token.
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
def update_existing_user(user_id: UUID, user_update: UserUpdate, db: Session = Depends(get_db), current_user: dict = Depends(verify_auth0_token)):
    """
    Update user profile. Requires Auth0 token.
    """
    updated_user = update_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=dict)
def delete_existing_user(user_id: UUID, db: Session = Depends(get_db), current_user: dict = Depends(verify_auth0_token)):
    """
    Delete user from the database. Requires Auth0 token.
    """
    success = delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}