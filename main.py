from tkinter import *
import product
import cash
import login
import productScreen
import cashScreen
import auth
from PIL import Image,ImageTk

main = Tk()
main.state("zoomed")
main.config(bg="#141414")

# initial state of vending machine
vendingState = {
    "is_authenticated": False,
    "is_admin": "false",
    "total_cart_amoutn": 0,
    # watch for input currency
    "input_currency": 0,
    "expense_amount": 0,
    # amount_to_return = input_currency - expense_amount
    "amount_to_return": 0,
}

# this will add title
main.title("Vending Machine")

def activate(vendingState):
    '''
    create table of Auth, Product, Currency
    add and query Currency
    setup login page
    '''
    # create cash table
    product.create_productTable()

    # TODO 4 types Product
    # product.add_drink()
    # product.add_chips()
    # product.add_chocolate()
    # product.add_Biscuit()
    
    # query all Products
    # product.query_all_drinks()
    # product.query_all_chips()
    # product.query_all_chocolates()
    # product.query_all_biscuits()
    
    # update individual Product
    # product.update_drink()
    # product.update_chips()
    # product.update_chocolate()
    # product.update_biscuit()
    
    # delete individual Product
    # product.delete_drink()
    # product.delete_chips()
    # product.delete_chocolate()
    # product.delete_biscuit()

    # create cash table
    cash.create_cash_table()

    # add 4 types currenty
    """cash.add_cash(1, 'ten', 10)
    cash.add_cash(2, 'twenty', 10)
    cash.add_cash(3, 'fifty', 10)
    cash.add_cash(4, 'hundred', 10)"""

    # query all currenty
    """row = cash.query_all()
    print(row)"""
    
    # query individual Product
    # 
    # 
    
    # delete individual Product
    # 
    # 
    

    productScreen.products(main, vendingState)
    login.login(main, vendingState)
    cashScreen.cash(main, vendingState)
    auth.create_users_table()
    auth.query_all_users()

activate(vendingState)

main.mainloop()
