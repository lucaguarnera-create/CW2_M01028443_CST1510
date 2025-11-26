#users.py #User Croud
import sqlite3
import pandas as pd

def create_user_table(conn):
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL, 
    role TEXT DEFAULT 'user' ) """) 
    conn.commit()

def add_user(conn, username, password_hash):
    cur = conn.cursor()
    sql = ("INSERT INTO users (username, password_hash) VALUES (?, ?)")
    cur.execute(sql, (username, password_hash))   
    conn.commit()

def get_users(conn):
    curr = conn.cursor()
    curr.execute("SELECT * FROM users")
    return curr.fetchall()