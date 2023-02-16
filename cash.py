import sqlite3 

def create_cash_table():
    '''
    @params: No Params
    creates Cash table if there is no table
    return None
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Cash (
            ID INT(50),
            Value VARCHAR(10),
            Quantity INT(10)
        )
        """)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

def add_cash(ID, Value, Quantity):
    '''
    @params: id, value, quantity
    update cash
    return None
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor()
        c.execute("INSERT INTO Cash VALUES (:ID, :Value, :Quantity)", {
                  'ID': ID,
                  'Value': Value,
                  'Quantity': Quantity,
              })

        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

def query_all_cashes():
    '''
    @params: No Params
    query add cashes
    return dict of cashes
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Cash")
        cashes = c.fetchall()
        return cashes

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

def update_cash(ID, Value, Quantity):
    '''
    @params: id, value, quantity
    update cash 
    return None
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor()

        c.execute(
            "update Cash set ID=? Value=?, Quantity=?",
            (ID, Value, Quantity))

        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

def delete_cash(ID):
    '''
    @params: id
    delete cash 
    return None
    '''

    try:
        conn = sqlite3.connect("vending_machine.db")
        c = conn.cursor()
        c.execute("delete from Cash where ID=?", (ID,))

        conn.commit()
    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

