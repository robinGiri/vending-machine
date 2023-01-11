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
    
    cash_value = ''
    cash_quantity = ''
    for record in cashes:
        cash_value += str(record[1]) + "\n"
        cash_quantity += str(record[2]) + "\n"
    return cash_value, cash_quantity
