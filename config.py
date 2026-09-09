import os
from typing import List

API_ID = os.environ.get("API_ID", "38751960")
API_HASH = os.environ.get("API_HASH", "4e8f828046a30ec70899b523bd763fa9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8986887008:AAFtwQe1G0ldF0BzvBsIwtFB3UyI2OQaf3g")
PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg")).split()
ADMIN = int(os.environ.get("ADMIN", "7754709357"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004422224007"))
DB_URI = os.environ.get("DB_URI", "mongodb+srv://tgjiro441_db_user:Tgjirosamkun@cluster0.9reqco1.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "stylish_font_bot")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
