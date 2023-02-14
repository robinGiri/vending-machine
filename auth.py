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

def delete_user(ID):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from users WHERE ID =:ID",
    {
        'ID':ID
    }
    )
    conn.commit()

def isLogin(username, password):
    users = query_all_users()
    for user in users:
        list1 = list(user)
        if list1[1] == username and  list1[3] == password:
            # check if email list1[1] note.txt username == admin_<name> , return (True,True), else 
            if "admin_robin" == username or "admin_abhisek" == username or "admin_anukul" == username or "admin_dilasha" == username :
                return True, True
            else:
                return True, False
        else:
            False, False

