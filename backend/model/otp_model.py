import sqlite3
from datetime import datetime

DATABASE = "database.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_otp_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS otp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            code TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            used INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    conn.close()

def create_otp(user_id, code, expires_at):
    conn = get_connection()
    conn.execute(
        "INSERT INTO otp (user_id, code, expires_at) VALUES (?, ?, ?)",
        (user_id, code, expires_at)
    )
    conn.commit()
    conn.close()

def get_valid_otp(user_id, code):
    conn = get_connection()
    otp = conn.execute(
        "SELECT * FROM otp WHERE user_id=? AND code=? AND used=0",
        (user_id, code)
    ).fetchone()
    conn.close()
    return otp

def mark_otp_as_used(otp_id):
    conn = get_connection()
    conn.execute("UPDATE otp SET used=1 WHERE id=?", (otp_id,))
    conn.commit()
    conn.close()
