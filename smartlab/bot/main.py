from telegram import Bot, ParseMode

import os
from dotenv import load_dotenv


class MyTelegramBot:

    def __init__(self, chat_id: None) -> None:

        load_dotenv('./smartlab/bot/.env')
        self.token = os.getenv('TOKEN')
        self.chat_id = chat_id
        if self.chat_id is None:
            self.chat_id = os.getenv('CHAT_ID')

        self.bot = Bot(
            token=self.token
        )

    def send(self, text):
        self.bot.send_message(
            chat_id=self.chat_id,
            text=text,
            parse_mode=ParseMode.HTML
        )


if __name__ == "__main__":
    bot_test = MyTelegramBot(
        chat_id='-418852529'
    )
    bot_test.send('test')
