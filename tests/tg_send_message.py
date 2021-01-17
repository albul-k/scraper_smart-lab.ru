import os, sys
from dotenv import load_dotenv
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from flask_app.src.tg import TelegramBot


load_dotenv('./flask_app/.env')

bot_test = TelegramBot(
    token=os.getenv('TG_TOKEN'),
    chat_id=os.getenv('TEST_CHAT_ID'),
)
bot_test.send('test')