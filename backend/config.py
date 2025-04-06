import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Optional: Email setup (used in task assignment notifications)
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
    EMAIL_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_PASS = os.environ.get("EMAIL_HOST_PASSWORD")


