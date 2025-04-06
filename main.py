import requests
import datetime
import time
import config
from keep_alive import keep_alive

def get_gold_price():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {"x-access-token": config.GOLD_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    usd_per_ounce = data["price"]
    qar_per_gram = (usd_per_ounce / 31.1) * config.USD_TO_QAR
    return round(qar_per_gram, 2)

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage"
    payload = {"chat_id": config.CHAT_ID, "text": text}
    requests.post(url, data=payload)

def main():
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 or now.hour == 17:
            price = get_gold_price()
            send_telegram_message(f"سعر غرام الذهب الآن: {price} ريال قطري")
            time.sleep(3600)
        time.sleep(30)

keep_alive()
main()