import os
import sqlite3
import random
import string

from dotenv import load_dotenv

load_dotenv()

db_name = os.environ.get("DB_NAME")

conn = sqlite3.connect(db_name, check_same_thread=False)
cursor = conn.cursor()


def add_item(item):
    key = "".join(random.choices(string.ascii_letters, k=10))

    cursor.execute(
        "INSERT INTO items (key, item) VALUES (?, ?)",
        (key, item)
    )

    conn.commit()


def list_item():
    res = cursor.execute(
        "SELECT key, item FROM items"
    )

    return res.fetchall()