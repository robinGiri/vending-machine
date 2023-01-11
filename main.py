from tkinter import *
import product
import cash
import login
from PIL import Image,ImageTk

main = Tk()
main.state("zoomed")
main.config(bg="#000000")

# this will add title
main.title("Vending Machine")

# first 2 gr
image    = Image.open("public/Drinks.png")
resized = image .resize((100,85), Image.Resampling.LANCZOS)
new_pic  = ImageTk.PhotoImage(resized)
my_label = Label(main, image=new_pic    ,borderwidth=0,border=0,bg="#000000")
my_label.place(x=180,y=90)

image    = Image.open("public/Drinks.png")
resized = image .resize((100,85), Image.Resampling.LANCZOS)
new_pic6  = ImageTk.PhotoImage(resized)
my_label = Label(main, image=new_pic6    ,borderwidth=0,border=0,bg="#000000")
my_label.place(x=180,y=220)

image    = Image.open("public/Chips.png")
resized = image.resize((100,85), Image.Resampling.LANCZOS)
new_pic11  = ImageTk.PhotoImage(resized)
my_label = Label(main, image=new_pic11    ,borderwidth=0,border=0,bg="#000000")
my_label.place(x=180,y=335)

image    = Image.open("public/Drinks.png")
resized = image.resize((100,85), Image.Resampling.LANCZOS)
new_pic16  = ImageTk.PhotoImage(resized)
my_label = Label(main, image=new_pic16    ,borderwidth=0,border=0,bg="#000000")
my_label.place(x=180,y=465)

def activate():
    '''
    create table of Auth, Product, Currency
    add and query Currency
    setup login page
    '''
    # create cash table
    product.create_productTable()

    # TODO 4 types Product
    # 
    # 
    # 
    # 
    
    # query all Products
    # 
    # 
    
    # query individual Product
    # 
    # 
    
    # delete individual Product
    # 
    # 

    # create cash table
    cash.create_cash_table()

    # add 4 types currenty
    cash.add_cash(1, 'ten', 10)
    cash.add_cash(2, 'twenty', 10)
    cash.add_cash(3, 'fifty', 10)
    cash.add_cash(4, 'hundred', 10)

    # query all currenty
    value, quantity = cash.query_all()
    print(value, quantity)
    
    # query individual Product
    # 
    # 
    
    # delete individual Product
    # 
    # 

    login.login(main)

activate()

main.mainloop()
