from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.config import settings

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """ Hash a plaintext password """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """ Verify if a plaintext password matches the hased password """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expire_delta: timedelta = None) -> str:
    """ Generate a JWT access token with optional expiration """
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now(datetime.UTC) + expire_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """Decode a JWT access token and return the payload if valid, else None."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None    

