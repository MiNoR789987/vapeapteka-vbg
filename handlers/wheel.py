# wheel.py
import random
from config import PRIZES

def spin_wheel():
    """Случайный выбор приза по шансам"""
    total = sum(prize["chance"] for prize in PRIZES)
    pick = random.randint(1, total)
    current = 0
    for prize in PRIZES:
        current += prize["chance"]
        if pick <= current:
            return prize
    return PRIZES[0]  # запасной вариант
