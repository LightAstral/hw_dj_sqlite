import sqlite3

conn = sqlite3.connect("db.sqlite3")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_depart TEXT UNIQUE NOT NULL,
    phone TEXT
    
  );
""")
# cursor.execute("DROP TABLE IF EXISTS Department")
# cursor.execute("""
# ALTER TABLE Department ADD count INTEGER
#
# """)


conn.close()