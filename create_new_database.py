import sqlite3

conn=sqlite3.connect("UPDB.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
password TEXT NOT NULL);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bank(
userID INTEGER NOT NULL,
website VARCHAR(20) NOT NULL,
website_password TEXT NOT NULL,
url TEXT NOT NULL);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS link(
url TEXT NOT NULL,
xpath TEXT NOT NULL);
''')

conn.commit()
conn.close()
