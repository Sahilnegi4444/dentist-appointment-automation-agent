import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_USER = os.getenv("MYSQL_USER")
    DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
    DB_HOST = os.getenv("MYSQL_HOST")
    DB_PORT = os.getenv("MYSQL_PORT")
    DB_NAME = os.getenv("MYSQL_DATABASE")

    @property
    def DATABASE_URL(self):
        return (
            f"mysql+pymysql://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()

def _get_env(key):
    value = os.getenv(key)
    if not value:
        raise ValueError(f"{key} is not set in .env")
    return value