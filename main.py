import asyncio
import json
import random
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
import uvicorn

BOT_TOKEN = "ТВОЙ_ТОКЕН"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

DB_FILE = "database.json"

def load_db():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

app = FastAPI()
app.mount("/webapp", StaticFiles(directory="webapp"), name="webapp")

@app.get("/")
def index():
    return FileResponse("webapp/index.html")

@app.get("/prizes")
def get_prizes():
    db = load_db()
    return db["prizes"]

@app.post("/spin")
def spin():
    db = load_db()
    weighted = []
    for p in db["prizes"]:
        weighted.extend([p] * p["chance"])
    prize = random.choice(weighted)
    prize["drops"] += 1
    save_db(db)
    return prize

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Открыть колесо:",
        reply_markup={
            "inline_keyboard":[[
                {
                    "text":"🎡 Открыть",
                    "web_app":{"url":"https://ТВОЙ-САЙТ"}
                }
            ]]
        }
    )

async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.create_task(start_bot())
    uvicorn.run(app, host="0.0.0.0", port=8000)
