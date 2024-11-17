from jose import jwt, JWTError
from fastapi import HTTPException
import requests
from datetime import timedelta, datetime
from passlib.context import CryptContext
from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Security:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using bcrypt."""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a plaintext password against a hashed one."""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict) -> str:
        """Create a JWT access token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHMS)
        return encoded_jwt

    @staticmethod
    def verify_auth0_token(token: str) -> dict:
        """Validate and decode an Auth0 token."""
        try:
            response = requests.get(f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json")
            response.raise_for_status()
            jwks = response.json()

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
                raise HTTPException(status_code=401, detail="Invalid token")

            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=[settings.ALGORITHMS],
                audience=settings.API_AUDIENCE,
                issuer=f"https://{settings.AUTH0_DOMAIN}/",
            )
            return payload
        except JWTError as e:
            raise HTTPException(status_code=401, detail="Token validation failed") from e
