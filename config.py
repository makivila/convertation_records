from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SERVER_ONE = "server_one/"
    SERVER_TWO = "server_two/"

    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")
