import os

from dotenv import load_dotenv

class Credentials:
    def __init__(self):
        load_dotenv()
        self.TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
        self.CHAT_ID = os.getenv("CHAT_ID")

credentials = Credentials()
