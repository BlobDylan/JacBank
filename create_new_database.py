import sqlite3

"""This is where the tables in the database are made in the case that they are not yet made."""


conn = sqlite3.connect("UPDB.db")
cursor = conn.cursor()

"""Table for the users of JacBank"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL);
''')

"""Table for the websites and passwords of JacBank"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS bank(
userID INTEGER NOT NULL,
website VARCHAR(20) NOT NULL,
website_password TEXT NOT NULL,
url TEXT NOT NULL);
''')

"""Table for the xpaths and urls"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS link(
url TEXT NOT NULL,
xpath TEXT NOT NULL);
''')

conn.commit()
conn.close()
