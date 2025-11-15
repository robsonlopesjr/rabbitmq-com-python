import requests

from .telegram_credentials import credentials

def send_telegram_message(message: str) -> None:
    token = credentials.TELEGRAM_TOKEN
    chat_id = credentials.CHAT_ID

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)

