#users.py #User Croud
import sqlite3
import pandas as pd



def add_user(conn, username, password_hash):
    cur = conn.cursor()
    sql = ("INSERT INTO users (username, password_hash) VALUES (?, ?)")
    cur.execute(sql, (username, password_hash))   
    conn.commit()

def get_users(conn):
    curr = conn.cursor()
    curr.execute("SELECT * FROM users")
    return curr.fetchall()