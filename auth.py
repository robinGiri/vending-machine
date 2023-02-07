import sqlite3 

def create_users_table():
    con = sqlite3.connect("vending_machine.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            password TEXT
    )
    """)
    con.commit()
    con.close()

def create_user(username, email, password):
    print(username, email, password)
    conn = sqlite3.connect('vending_machine.db')
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)""", (username, email, password))

    conn.commit()
    conn.close()

def query_all_users():
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM users") 
    cashes = c.fetchall()
    return cashes

def isLogin(username, password):
    users = query_all_users()
    for user in users:
        list1 = list(user)
        if list1[1] == username and  list1[3] == password:
            return True
        else:
            False

