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
    """add drinks to the database"""
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
    """Read all the drinks in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Drinks") 
    drinks = c.fetchall()
    print(drinks)
    return drinks
    

def delete_drink(ID):
    """Delete a drink from the list of drinks in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Drinks where ID=:ID",{
        'ID':ID
    })
    conn.commit()

def update_drink(ID,Name,Price,Quantity):
    """Update drinks in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "UPDATE Drinks SET ID = ?,Name = ? , Price = ?, Quantity =? ",
        (ID,Name,Price,Quantity))
    conn.commit()

# Chips
def add_chips(ID,Name,Price,Quantity):
    """add chips to the database"""
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
    """Read all the chips in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Chips") 
    chips = c.fetchall()
    print(chips)
    return chips
    

def delete_chips(ID):
    """Delete chips from the list of chips in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Chips WHERE ID =:ID",
    {
        'ID':ID
    }
    )
    conn.commit()

def update_chips(ID,Name,Price,Quantity):
    """Update any chips in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Chips set ID=?, Name=?, Price=?, Quantity=?",
        (ID,Name,Price,Quantity))
    conn.commit()

# chocolate
def add_chocolate(ID,Name,Price,Quantity):
    """add chocolate to the database"""
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
    """Read all the chocolates in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Chocolates") 
    chocolates = c.fetchall()
    print(chocolates)
    return chocolates
    

def delete_chocolate(ID):
    """Delete a chocolate from the list of chocolates in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Chocolates WHERE ID= :ID",
    {
        'ID':ID
    })
    conn.commit()

def update_chocolate(ID,Name,Price,Quantity):
    """Update any chocolate in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Chocolates set ID=?,Name=?, Price=?, Quantity=?",
        (ID,Name,Price,Quantity))
    conn.commit()

# Biscuits
def add_Biscuit(ID,Name,Price,Quantity):
    """add biscuit to the database"""
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
    """Read all the biscuits in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 
    
    c.execute("SELECT * FROM Biscuits") 
    biscuits = c.fetchall()
    print(biscuits)
    return biscuits
    

def delete_biscuit(ID):
    """Delete a biscuit from the list of biscuits in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute("DELETE from Biscuits WHERE ID= :ID",
    {
        'ID':ID
    })
    conn.commit()

def update_biscuit(ID,Name,Price,Quantity):
    """Update any biscuit in the database"""
    conn = sqlite3.connect("vending_machine.db")
    c = conn.cursor() 

    c.execute(
        "update Biscuits set ID=?, Name=?, Price=?, Quantity=?",
        (ID,Name,Price,Quantity))
    conn.commit()
