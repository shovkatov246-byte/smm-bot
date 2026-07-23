import sqlite3

db = sqlite3.connect("database.db")
sql = db.cursor()

sql.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    balance INTEGER DEFAULT 0
)
""")

db.commit()
