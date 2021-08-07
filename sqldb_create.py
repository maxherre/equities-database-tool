import os
import sqlite3
from sqlite3 import Error

def create_server_connection(database_name):
    conn = None
    try:
        conn = sqlite3.connect(database_name)
        conn.execute("PRAGMA foreign_key = 1")
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table):
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as e:
        print(e)

db_name = 'nyse_database.db'

def main():
    