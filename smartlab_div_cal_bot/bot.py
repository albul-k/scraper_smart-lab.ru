from telegram import Bot, ParseMode

import os
# import html
from dotenv import load_dotenv

load_dotenv('.env')

text = '<b>Hello World!</b>'

bot = Bot(token=os.getenv('TOKEN'))
bot.send_message(
    chat_id=os.getenv('DEVELOPER_CHAT_ID'),
    text=text,
    parse_mode=ParseMode.HTML
)
