import os, sys
from flask import Flask, request, make_response, jsonify
from dotenv import load_dotenv
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from flask_app.src.tg import TelegramBot


load_dotenv('./flask_app/.env')
API_TOKEN = os.getenv('API_TOKEN')
TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

app = Flask(__name__)

@app.route("/send", methods="POST")
def send_message():

    if request.json.get('api_token') == API_TOKEN:
        
        message = request.json.get('message')
        bot = TelegramBot(
            token=TG_TOKEN,
            chat_id=CHAT_ID,
        )
        bot.send(message)

        return make_response(jsonify({"success": True}), 200)
    else:
        return make_response(jsonify({"error": "Wrong api token", "success": False}), 400)

if __name__ == "__main__":
    app.run()