import os
from dotenv import load_dotenv

load_dotenv("env/.env")

def get_env(key):
    return os.getenv(key)
