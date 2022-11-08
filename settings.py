import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DB_URL = os.environ.get("DB_URL")
API_TOKEN = os.environ.get("API_TOKEN")