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

cursor.execute("SELECT COUNT(*) FROM targets")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO targets (id, kalori, protein) VALUES (1, 0, 0)")
    conn.commit()


def insert_target_workout(workout):
    cursor.execute("INSERT INTO workouts (nama_workout) VALUES (?)", (workout,))
    conn.commit()

def delete_workout_by_id(workout_id):
    cursor.execute("DELETE FROM workouts WHERE id = ?", (workout_id,))
    conn.commit()

def insert_target_kalori(kalori):
    cursor.execute("UPDATE targets SET kalori = ?", (kalori,))
    conn.commit()

def insert_target_protein(protein):
    cursor.execute("UPDATE targets SET protein = ?", (protein,))
    conn.commit()

def get_target():
    cursor.execute("SELECT kalori, protein FROM targets WHERE id = 1")
    return cursor.fetchone()

def get_workouts():
    cursor.execute("SELECT id, nama_workout FROM workouts ORDER BY id")
    return cursor.fetchall()