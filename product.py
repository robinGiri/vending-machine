import sqlite3 

def create_productTable():
    con = sqlite3.connect("vending_machine.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Drinks (
        ID INT(50),
        Name VARCHAR(10),
        Price INT(10),
        Quantity INT(10)
    )
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS Biscuits(
        ID INT(50),
        Name VARCHAR(10),
        Price INT(10),
        Quantity INT(10)
    )
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS Chips(
        ID INT(50),
        Name VARCHAR(10),
        Price INT(10),
        Quantity INT(10)
    )
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS Chocolates(
        ID INT(50),
        Name VARCHAR(10),
        Price INT(10),
        Quantity INT(10)
    )
    """)
    con.commit()
    con.close()