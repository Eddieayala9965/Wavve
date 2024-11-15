from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import jwt, JWTError
from app.core.config import settings

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://{settings.AUTH0_DOMAIN}/authorize",
    tokenUrl=f"https://{settings.AUTH0_DOMAIN}/oauth/token",
)

def verify_auth0_token(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Validate the Auth0 JWT token.
    """
    try:
        payload = jwt.decode(
            token,
            key="your-auth0-public-key",  # Replace with your Auth0 JWKS setup
            algorithms=settings.ALGORITHMS,
            audience=settings.API_AUDIENCE,
            issuer=f"https://{settings.AUTH0_DOMAIN}/",
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")