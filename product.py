import sqlite3 

def create_productTable():
    '''
    @params: no params
    create new table in database
    don't create the table again if already exists 
    '''

    try:
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
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def add_drink(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    insert value to table Drinks 
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO Drinks VALUES (:ID, :Name, :Price, :Quantity)",{
                    'ID': ID,
                    'Name': Name,
                    'Price': Price,
                    'Quantity':Quantity
                })
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def query_all_drinks():
    '''
    @params: no params
    request for list of drinks 
    returns list of drinks
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 
        
        c.execute("SELECT * FROM Drinks") 
        drinks = c.fetchall()
        return drinks
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  
    

def delete_drink(ID):
    '''
    @params: ID
    deletes the drink that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute("DELETE from Drinks where ID=:ID",{
            'ID':ID
        })
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def update_drink(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    updates values of drink that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute(
            "UPDATE Drinks SET ID = ?,Name = ? , Price = ?, Quantity =? ",
            (ID,Name,Price,Quantity))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


# Chips
def add_chips(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    insert value to table Chips 
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO Chips VALUES (:ID, :Name, :Price, :Quantity)",{
                    'ID': ID,
                    'Name': Name,
                    'Price': Price,
                    'Quantity':Quantity
                })
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def query_all_chips():
    '''
    @params: no params
    request for list of chips 
    returns list of chips
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 
        
        c.execute("SELECT * FROM Chips") 
        chips = c.fetchall()
        return chips
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def delete_chips(ID):
    '''
    @params: ID
    deletes the chips that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute("DELETE from Chips WHERE ID =:ID",
        {
            'ID':ID
        }
        )
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def update_chips(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    updates values of chips that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute(
            "update Chips set ID=?, Name=?, Price=?, Quantity=?",
            (ID,Name,Price,Quantity))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


# Chocolates
def add_chocolate(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    insert value to table Chocolates 
    '''

    try: 
        conn = sqlite3.connect("vending_machine.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO Chocolates VALUES (:ID, :Name, :Price, :Quantity)",{
                    'ID': ID,
                    'Name': Name,
                    'Price': Price,
                    'Quantity':Quantity
                })
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def query_all_chocolates():
    '''
    @params: no params
    request for list of chocolates 
    returns list of chocolates
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 
        
        c.execute("SELECT * FROM Chocolates") 
        chocolates = c.fetchall()
        return chocolates
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  
    

def delete_chocolate(ID):
    '''
    @params: ID
    deletes the chocolate that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute("DELETE from Chocolates WHERE ID= :ID",
        {
            'ID':ID
        })
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def update_chocolate(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    updates values of chocolate that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute(
            "update Chocolates set ID=?,Name=?, Price=?, Quantity=?",
            (ID,Name,Price,Quantity))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


# Biscuits
def add_Biscuit(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    insert value to table Biscuits
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO Biscuits VALUES (:ID, :Name, :Price, :Quantity)",{
                    'ID': ID,
                    'Name': Name,
                    'Price': Price,
                    'Quantity':Quantity
                })
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def query_all_biscuits():
    '''
    @params: no params
    request for list of biscuits 
    returns list of biscuits
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 
        
        c.execute("SELECT * FROM Biscuits") 
        biscuits = c.fetchall()
        return biscuits
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  
    

def delete_biscuit(ID):
    '''
    @params: ID
    deletes the biscuit that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute("DELETE from Biscuits WHERE ID= :ID",
        {
            'ID':ID
        })
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  


def update_biscuit(ID,Name,Price,Quantity):
    '''
    @params: ID, Name, Price, Quantity
    updates values of biscuit that has been selected
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor() 

        c.execute(
            "update Biscuits set ID=?, Name=?, Price=?, Quantity=?",
            (ID,Name,Price,Quantity))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()  
        