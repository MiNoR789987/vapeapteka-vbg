# admin.py — админские функции для управления колесом и пользователями
from handlers import wheel
from utils import db

# Проверка, является ли пользователь админом
def is_admin(user_id, admin_ids):
    return user_id in admin_ids

# Добавляем новый приз в колесо
def add_prize(user_id, admin_ids, name, prize_type, value):
    if not is_admin(user_id, admin_ids):
        return "Ошибка: нет доступа"
    wheel.PRIZES.append({"name": name, "type": prize_type, "value": value})
    return f"Приз '{name}' добавлен в колесо!"

# Удаляем приз из колеса по имени
def remove_prize(user_id, admin_ids, name):
    if not is_admin(user_id, admin_ids):
        return "Ошибка: нет доступа"
    for prize in wheel.PRIZES:
        if prize["name"] == name:
            wheel.PRIZES.remove(prize)
            return f"Приз '{name}' удалён из колеса!"
    return "Приз не найден"

# Просмотр всех призов
def view_prizes(user_id, admin_ids):
    if not is_admin(user_id, admin_ids):
        return "Ошибка: нет доступа"
    return wheel.PRIZES