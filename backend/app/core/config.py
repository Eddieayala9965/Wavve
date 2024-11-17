from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load the environment variables from the `.env` file
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHMS: str = os.getenv("ALGORITHMS", "RS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    AUTH0_DOMAIN: str = os.getenv("AUTH0_DOMAIN")
    API_AUDIENCE: str = os.getenv("API_AUDIENCE")

settings = Settings()
