from tkinter import *
import cash
import auth
import product
import cashScreen
import loginScreen
import productScreen

main = Tk()
main.state("zoomed")
main.config(bg="#141414")

'''Added vending icon'''
photo = PhotoImage(file = "public/vending.png")
main.iconphoto(False, photo)
'''
initial state of vending machine where
1. authenticated is false initially and gets updated from login screen 
2. admin is false initially and gets updated from login screen if he or she is admin
3. input currency is 0 initially but gets updated from cash page once click and loded
4. expence amount is 0 initially but gets updated from product page once user starts buying
5. amount to return is 0 initially but gets updated from product page once user starts buying and decresed from loded cash
'''

vendingState = {
    "is_authenticated": False,
    "is_admin": False,
    "input_currency": 0,
    "expense_amount": 0,
    "amount_to_return": 0,
    "no_of_drink_bought": 1,
    "no_of_chocolate_bought": 1,
    "no_of_chips_bought": 1,
    "no_of_biscut_bought": 1,
}

# this will add title
main.title("Vending Machine")

def activate(vendingState):
    '''
    @params: vendingState which holdes state of our application
    create table of Auth, Product, Cash
    adds product screen, login screen, cash screen
    '''

    # if not exist create Cash table, Auth table, product table
    auth.create_users_table()
    product.create_productTable()
    cash.create_cash_table()

    # loads product screen, login screen, cash screen
    productScreen.products(main, vendingState)
    loginScreen.login(main, vendingState)
    cashScreen.cash(main, vendingState)

activate(vendingState)

main.mainloop()
