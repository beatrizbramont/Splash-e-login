import sqlite3

DATABASE = "database.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_users_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_user(nome, email, senha):
    conn = get_connection()
    conn.execute(
        "INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)",
        (nome, email, senha)
    )
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    ).fetchone()
    conn.close()
    return user
