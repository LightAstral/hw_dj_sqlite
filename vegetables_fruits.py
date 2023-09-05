import sqlite3

conn = sqlite3.connect("db_vg_fr.sqlite3")

vegetables_fruits = conn.cursor()

vegetables_fruits.execute("""
    CREATE TABLE IF NOT EXISTS Vegetables_And_Fruits(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    color TEXT NOT NULL,
    calories REAL NOT NULL,
    description TEXT 
    );
""")

vegetables_fruits.close()