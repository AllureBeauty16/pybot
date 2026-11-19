import sqlite3
import os

from dotenv import load_dotenv

load_dotenv()

db_name = os.environ.get("DB_NAME")

conn = sqlite3.connect(db_name)
cursor = conn.cursor()


def init():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            key TEXT,
            item TEXT
        )
    """)
    conn.commit()


if __name__ == "__main__":
    init()