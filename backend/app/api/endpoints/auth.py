from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError
import requests
from datetime import datetime, timedelta
from app.api.dependencies import get_db
from app.schemas.auth import Login, Token
from app.schemas.user import UserCreate
from app.crud.user import get_user_by_email, create_user
from app.core.config import settings
from passlib.context import CryptContext

router = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a plaintext password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    """Generate a JWT token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHMS)

def verify_auth0_token(token: str) -> dict:
    """Verify and decode Auth0 JWT tokens."""
    try:
        # Fetch Auth0's public keys
        response = requests.get(f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json")
        response.raise_for_status()
        jwks = response.json()

        # Extract and validate the correct RSA key
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = None
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"],
                }
                break
        if not rsa_key:
            raise HTTPException(status_code=401, detail="Invalid token header")

        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=[settings.ALGORITHMS],
            audience=settings.API_AUDIENCE,
            issuer=f"https://{settings.AUTH0_DOMAIN}/",
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Auth0 token")

@router.post("/login", response_model=Token)
def login(credentials: Login, db: Session = Depends(get_db)):
    """Login endpoint to authenticate a user."""
    user = get_user_by_email(db, credentials.email)
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/auth/callback", response_model=Token)
def auth0_callback(token: str, db: Session = Depends(get_db)):
    """Callback endpoint for Auth0 token validation and user registration."""
    token_payload = verify_auth0_token(token)

    
    email = token_payload.get("email")
    username = token_payload.get("nickname") or token_payload.get("name")
    if not email:
        raise HTTPException(status_code=400, detail="Token missing email field")
    
    user = get_user_by_email(db, email)
    if not user:
        user_data = UserCreate(email=email, username=username, password=None)
        user = create_user(db, user_data)
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
