import sqlite3 

def create_productTable():
    conn = sqlite3.connect("vending_machine.db")
    cur = conn.cursor()
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
    conn.commit()
    conn.close()

def add_drink(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Drinks VALUES (:ID, :Name, :Price, :Quantity)",{
                  'ID': ID,
                  'Name': Name,
                  'Price': Price,
                  'Quantity':Quantity
              })
    conn.commit()


def query_all_drinks():
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Drinks") 
    drinks = c.fetchall()
    print(drinks)
    return drinks
    

def delete_drink(Name):
    print(type(Name))
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Drinks WHERE Name = ?",(Name))
    c.commit()

def update_drink(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Drinks set ID=? Name=?, Price=?, Quantity=?",
        (ID,Name,Price,Quantity))
    c.commit()

# Chips
def add_chip(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Chips VALUES (:ID, :Name, :Price, :Quantity)",{
                  'ID': ID,
                  'Name': Name,
                  'Price': Price,
                  'Quantity':Quantity
              })
    conn.commit()


def query_all_chips():
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Chips") 
    chips = c.fetchall()
    return chips
    

def delete_chips(Name):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Chips WHERE Name = ?",(Name))
    c.commit()

def update_chip(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Chips set ID=? Name=?, Price=?, Quantity=?",
        (ID,Name,Price,Quantity))
    c.commit()

# chocolate
def add_chocolate(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Chocolates VALUES (:ID, :Name, :Price, :Quantity)",{
                  'ID': ID,
                  'Name': Name,
                  'Price': Price,
                  'Quantity':Quantity
              })
    conn.commit()


def query_all_chocolates():
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Chocolates") 
    chocolates = c.fetchall()
    return chocolates
    

def delete_chocolate(Name):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Chocolates WHERE Name = ?",(Name))
    c.commit()

def update_chocolate(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Chocolates set ID=? Name=?, Price=?, Quantity=?",
        (ID,Name,Price,Quantity))
    c.commit()

# Biscuits
def add_Biscuit(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Biscuits VALUES (:ID, :Name, :Price, :Quantity)",{
                  'ID': ID,
                  'Name': Name,
                  'Price': Price,
                  'Quantity':Quantity
              })
    conn.commit()


def query_all_biscuits():
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Biscuits") 
    biscuits = c.fetchall()
    return biscuits
    

def delete_biscuit(Name):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Biscuits WHERE Name = ?",(Name))
    c.commit()

def update_biscuit(ID,Name,Price,Quantity):
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Biscuits set ID=? Name=?, Price=?, Quantity=?",
        (ID,Name,Price,Quantity))
    c.commit()
