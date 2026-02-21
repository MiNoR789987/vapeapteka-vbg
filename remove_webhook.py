# remove_webhook.py
import requests
from config import BOT_TOKEN

url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
response = requests.get(url)
print(response.json())  # Должно вывести {"ok":true,...}
