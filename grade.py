import sqlite3

conn = sqlite3.connect("db_grade.sqlite3")

grade = conn.cursor()

grade.execute("""
    CREATE TABLE IF NOT EXISTS StudentGrades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        city TEXT NOT NULL,
        country TEXT NOT NULL,
        birthdate DATE NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        group_name TEXT NOT NULL,
        average_grade REAL NOT NULL,
        min_subject TEXT NOT NULL,
        max_subject TEXT NOT NULL
    );
""")

grade.close()