# db.py

USERS = {}  # {user_id: {username, balance, coupons}}

def add_user(user_id, username):
    if user_id not in USERS:
        USERS[user_id] = {"username": username, "balance": 0, "coupons": []}

def get_user_info(user_id):
    return USERS.get(user_id, {})

def add_coupon(user_id, code, value):
    add_user(user_id, "Unknown")
    USERS[user_id]["coupons"].append({"code": code, "value": value})
