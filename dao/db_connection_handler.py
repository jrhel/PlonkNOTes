import sqlite3

def get_connection():
    connection = sqlite3.connect("database.db")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection

# Verifies integrity of database
def verify_database():
    user_table = "CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)"
    variety_table = "CREATE TABLE IF NOT EXISTS Variety (id INTEGER PRIMARY KEY, grape TEXT UNIQUE)"
    wine_table = "CREATE TABLE IF NOT EXISTS Wine (id INTEGER PRIMARY KEY, name TEXT, classification TEXT, producer TEXT, vintage INTEGER, type TEXT)"
    wine_variety_table = "CREATE TABLE IF NOT EXISTS Wine_Variety (id INTEGER PRIMARY KEY, wine_id INTEGER, variety_id, FOREIGN KEY (wine_id) REFERENCES Wine(id), FOREIGN KEY (variety_id) REFERENCES Variety(id))"
    database = get_connection()
    database.execute(user_table)
    database.commit()
    database.close()

def execute(statement: str, params: [str]):
    connection = get_connection()
    row_id = connection.execute(statement, params).lastrowid
    connection.commit()
    connection.close()
    return row_id

def query(statement: str, params: [str]):
    connection = get_connection()
    result = connection.execute(statement, params).fetchall()
    connection.close()
    return result