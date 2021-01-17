from telegram import Bot, ParseMode

class TelegramBot:

    def __init__(self, token: None, chat_id: None) -> None:
        self.chat_id = chat_id
        self.bot = Bot(
            token=token
        )

    def send(self, text):
        self.bot.send_message(
            chat_id=self.chat_id,
            text=text,
            parse_mode=ParseMode.HTML,
        )