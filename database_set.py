import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS targets (
    id INTEGER PRIMARY KEY,
    kalori INTEGER NOT NULL,
    protein INTEGER NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_workout TEXT NOT NULL
)
""")

conn.commit()