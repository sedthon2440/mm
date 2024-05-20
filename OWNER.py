import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["NUNUU"]
OWNER_NAME = " 𝗥͜𝗼͡𝗪͡𝗲͜𝗦 "
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/veevvw"
GROUP = "https://t.me/sedthon_help"
VID_SO = "https://telegra.ph/file/de2bd04e32925298c13eb.jpg"
PHOTO = "https://telegra.ph/file/de2bd04e32925298c13eb.jpg"
LOGS = "jabababbab"
