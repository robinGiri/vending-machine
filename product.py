from main import con
from main import cur

cur.execute("""CREATE TABLE Drinks (
    ID INT(50),
    Name VARCHAR(10),
    Price INT(10),
    Quantity INT(10)
)
""")
cur.execute("""CREATE TABLE Biscuits(
    ID INT(50),
    Name VARCHAR(10),
    Price INT(10),
    Quantity INT(10)
)
""")
cur.execute("""CREATE TABLE Chips(
    ID INT(50),
    Name VARCHAR(10),
    Price INT(10),
    Quantity INT(10)
)
""")
cur.execute("""CREATE TABLE Chocolates(
    ID INT(50),
    Name VARCHAR(10),
    Price INT(10),
    Quantity INT(10)
)
""")
con.commit()
con.close()