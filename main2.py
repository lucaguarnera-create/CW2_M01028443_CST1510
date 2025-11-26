import sqlite3

USER_FILE = 'DATA/users.txt'



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




conn = sqlite3.connect('DATA/telligence_platform.db')
with open(r'C:\Users\lucag\CW2_01028443_CST1510\CW2_M01028443_CST1510\DATA\user.txt', "r") as f:
    lines = f.readlines()






