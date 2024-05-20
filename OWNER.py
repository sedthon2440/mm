import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["R7_OX"]
OWNER_NAME = " 𝗥͜𝗼͡𝗪͡𝗲͜𝗦 "
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/RQ_SF"
GROUP = "https://t.me/R3_QX"
VID_SO = "https://telegra.ph/file/bf1273e084a0fb135ab5a.jpg"
PHOTO = "https://telegra.ph/file/bf1273e084a0fb135ab5a.jpg"
LOGS = "jabababbab"
