import os

from heroku3 import from_key
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "6"))
API_HASH = os.environ.get("API_HASH", "ff8ee60e4b9f66552ee0546e47c5565b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
ARQ_API_KEY = "BMVCMF-YGSKKU-QEBOVE-NNETKU-ARQ" 
LANGUAGE = "en" "hi"
ARQ_API_BASE_URL = "https://thearq.tech"

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
