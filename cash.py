import sqlite3 

def create_cash_table():
    con = sqlite3.connect("vending_machine.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Cash (
        ID INT(50),
        Value VARCHAR(10),
        Quantity INT(10)
    )
    """)
    con.commit()
    con.close()

def add_cash(ID, Value, Quantity):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor()
    c.execute("INSERT INTO Cash VALUES (:ID, :Value, :Quantity)",{
                  'ID': ID,
                  'Value': Value,
                  'Quantity': Quantity,
              })

    conn.commit()
    conn.close()

def query_all():
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Cash") 
    cashes = c.fetchall()

    return cashes

def remove(ID):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("delete from Cash where ID=?", (ID,))
    c.commit()

def update(ID, Value, Quantity):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Cash set ID=? Value=?, Quantity=?",
        (ID, Value, Quantity))
    c.commit()
