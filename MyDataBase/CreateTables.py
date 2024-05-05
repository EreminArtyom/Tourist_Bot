import sqlite3
connection = sqlite3.connect('TouristBotStatistics_new.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS rating (
rtng INTEGER PRIMARY KEY,
number INTEGER NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS visit (
location TEXT PRIMARY KEY,
city TEXT NOT NULL,
count INTEGER NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS places (
id INTEGER PRIMARY KEY,
Pic TEXT NOT NULL,
Name TEXT NOT NULL,
Address TEXT NOT NULL,
desc TEXT NOT NULL,
link TEXT NOT NULL,
sale INTEGER NOT NULL,
City TEXT NOT NULL,
type TEXT NOT NULL
)
''')
connection.commit()
connection.close()
