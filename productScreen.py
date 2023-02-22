from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import product

def products(main, vendingState):
    '''
    @params: main and vending state are params
    we are making main items clickable
    after clicking delete quantity from DB
    and reduce input currency
    '''
    def update_vending_expense_amount(amount):
        '''
        updated expense_amount and amount_to_return of vending state
        shows expense_amount and amount_to_return in UI
        argument: 
            - amount: amount of product selected
        '''

        vendingState["expense_amount"] += amount
        vendingState["amount_to_return"]=vendingState["input_currency"]-vendingState["expense_amount"]
        first = Frame(good_frame, bg="#6A6161",height=50,width=560)
        first.place(x=1,y=1)
        Label(first, text="Your total amount is Rs. {}".format(vendingState["expense_amount"]),fg="#00FF7F", bg="#6A6161",font=5).place(x=1,y=5)
        Label(first, text="Your remaning amount is Rs. {}".format(vendingState["amount_to_return"]),fg="#00FF7F", bg="#6A6161",font=5).place(x=1,y=20) 
        
    def checkAuthAndCurrency(limitOfSelectedItem, itemType):
        '''
        check if user is is_authenticated, alredy selected same item,  haven't input cash
        argument: 
            - limitOfSelectedItem: if user has select more then one type of item
            - itemType: which type of product is selected
        '''

        if vendingState["is_authenticated"] == False:
            messagebox.showerror("error", "Please Login First")
            return False
        if limitOfSelectedItem < 1:
            messagebox.showerror("error", "Sorry, We don't allow buying more than one {}".format(itemType))
            return False
        if vendingState["input_currency"] == 0:
            messagebox.showerror("error", "Please Load Cash First")
            return False
        return True
      
    def checkWeHaveEnoughtDrinks(noOfItem, itemType, itemAmount):
        '''
        check if selected product in databse and sents message
        check if use has enough balance or not, if not send error
        argument: 
            - noOfItem: selected product in databse
            - itemType: which type of product is selected
        '''
        
        if  noOfItem < 1:
            messagebox.showerror("error", "Sorry, We are out of {}".format(itemType))
            return False
        if vendingState["input_currency"]-itemAmount < 0:
            messagebox.showerror("error", "You Don't Have Enough Balance To  Buy, Load cash First")
            return False
        return True

    goods = Frame(main, width=600,height=570,bg="#000000")
    goods.place(x=135,y=40)

    good_frame = Frame(main, width=560,height=50,bg="#6A6161")
    good_frame.place(x=155,y=547)

    first = Frame(good_frame, bg="#6A6161",height=100,width=147)
    first.place(x=1,y=45)
  
    item = Frame(main, width=600,height=130,bg="#000000")
    item.place(x=135,y=640)

    item1 = Frame(item, width=100,height=110,bg="#000000")
    item1.place(x=20,y=10)

    item2 = Frame(item, width=100,height=110,bg="#000000")
    item2.place(x=170,y=10)

    item3 = Frame(item, width=100,height=110,bg="#000000")
    item3.place(x=320,y=10)

    item4 = Frame(item, width=100,height=110,bg="#000000")
    item4.place(x=470,y=10)

    # clickable individual products
    def coke():
        if checkAuthAndCurrency(vendingState["no_of_drink_bought"], 'Drink'):
            drinks = product.query_all_drinks()         
            for drink in drinks:
                my_drink = list(drink)
                if "Coke" == my_drink[1]:
                    if checkWeHaveEnoughtDrinks(my_drink[3], "Coke", my_drink[2]):
                        vendingState["no_of_drink_bought"] -= 1
                        update_vending_expense_amount(my_drink[2])
                        product.update_drink(my_drink[0], my_drink[1], my_drink[2], my_drink[3]-1)
                        my_coke.config(image=new_pic2,bg="#000000",border=0,borderwidth=0)
                        my_coke = Label(item1,image="",bg="#000000")
                        my_coke.place(x=10,y=10)
    image2 = Image.open("public/Coke.png")
    resized = image2.resize((60,85), Image.Resampling.LANCZOS)
    new_pic2 = ImageTk.PhotoImage(resized)
    coke_img = Label(goods, image=new_pic2,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=50,y=20)
    coke_btn = Button(goods, image=new_pic2,command=coke,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    coke_btn.place(x=50,y=20)

    def Fanta():
        if checkAuthAndCurrency(vendingState["no_of_drink_bought"], 'Drink'):
            drinks = product.query_all_drinks()         
            for drink in drinks:
                my_drink = list(drink)
                if "Fanta" == my_drink[1]:
                    if checkWeHaveEnoughtDrinks(my_drink[3], "Fanta", my_drink[2]):
                        vendingState["no_of_drink_bought"] -= 1
                        update_vending_expense_amount(my_drink[2])
                        product.update_drink(my_drink[0], my_drink[1], my_drink[2], my_drink[3]-1)
                        my_Fanta.config(image=new_pic3,bg="#000000",border=0,borderwidth=0)
                        my_Fanta = Label(item1,image="",bg="#000000")
                        my_Fanta.place(x=10,y=10)
    image3 = Image.open("public/Fanta.png")
    resized = image3.resize((60,85), Image.Resampling.LANCZOS)
    new_pic3 = ImageTk.PhotoImage(resized)
    Fanta_img = Label(goods, image=new_pic3,borderwidth=0,border=0,bg="#000000")
    Fanta_img.place(x=200,y=20)
    Fanta_btn = Button(goods, image=new_pic3,command=Fanta,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Fanta_btn.place(x=200,y=20)

    def Sprite():
        if checkAuthAndCurrency(vendingState["no_of_drink_bought"], 'Drink'):
            drinks = product.query_all_drinks()         
            for drink in drinks:
                my_drink = list(drink)
                if "Sprite" == my_drink[1]:
                    if checkWeHaveEnoughtDrinks(my_drink[3], "Sprite", my_drink[2]):
                        vendingState["no_of_drink_bought"] -= 1
                        update_vending_expense_amount(my_drink[2])
                        product.update_drink(my_drink[0], my_drink[1], my_drink[2], my_drink[3]-1)
                        my_Sprite.config(image=new_pic4,bg="#000000",border=0,borderwidth=0)
                        my_Sprite = Label(item1,image="",bg="#000000")
                        my_Sprite.place(x=10,y=10)

    image4 = Image.open("public/Sprite.png")
    resized = image4.resize((130,90), Image.Resampling.LANCZOS)
    new_pic4 = ImageTk.PhotoImage(resized)
    Sprite_img = Label(goods, image=new_pic4,borderwidth=0,border=0,bg="#000000")
    Sprite_img.place(x=300,y=20)
    Sprite_btn = Button(goods, image=new_pic4,command=Sprite,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Sprite_btn.place(x=300,y=20)

    def Pepsi():
        if checkAuthAndCurrency(vendingState["no_of_drink_bought"], 'Drink'):
            drinks = product.query_all_drinks()         
            for drink in drinks:
                my_drink = list(drink)
                if "Pepsi" == my_drink[1]:
                    if checkWeHaveEnoughtDrinks(my_drink[3], "Pepsi", my_drink[2]):
                        vendingState["no_of_drink_bought"] -= 1
                        update_vending_expense_amount(my_drink[2])
                        product.update_drink(my_drink[0], my_drink[1], my_drink[2], my_drink[3]-1)
                        my_Pepsi.config(image=new_pic5,bg="#000000",border=0,borderwidth=0)
                        my_Pepsi = Label(item1,image="",bg="#000000")
                        my_Pepsi.place(x=10,y=10)

    image5 = Image.open("public/Pepsi.png")
    resized = image5.resize((90,85), Image.Resampling.LANCZOS)
    new_pic5 = ImageTk.PhotoImage(resized)
    Pepsi_img = Label(goods, image=new_pic5,borderwidth=0,border=0,bg="#000000")
    Pepsi_img.place(x=470,y=20)
    Pepsi_btn = Button(goods, image=new_pic5,command=Pepsi,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Pepsi_btn.place(x=470,y=20)


    def Bonbon():
        if checkAuthAndCurrency(vendingState["no_of_biscut_bought"], 'biscuit'):
            biscuits = product.query_all_biscuits()         
            for biscuit in biscuits:
                my_biscuit = list(biscuit)
                if "Bourbon" == my_biscuit[1]:
                    if checkWeHaveEnoughtDrinks(my_biscuit[3], "Bourbon", my_biscuit[2]):
                        vendingState["no_of_biscut_bought"] -= 1
                        update_vending_expense_amount(my_biscuit[2])
                        product.update_biscuit(my_biscuit[0], my_biscuit[1], my_biscuit[2], my_biscuit[3]-1)
                        my_Bonbon.config(image=new_pic7,bg="#000000",border=0,borderwidth=0)
                        my_Bonbon = Label(item2,image="",bg="#000000")
                        my_Bonbon.place(x=10,y=10)

    image7 = Image.open("public/Bornbon.png")
    resized = image7.resize((80,85), Image.Resampling.LANCZOS)
    new_pic7 = ImageTk.PhotoImage(resized)
    Bonbon_img = Label(goods, image=new_pic7,borderwidth=0,border=0,bg="#000000")
    Bonbon_img.place(x=40,y=145)
    Bonbon_btn = Button(goods, image=new_pic7,command=Bonbon,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Bonbon_btn.place(x=40,y=145)

    def Oreo():
        if checkAuthAndCurrency(vendingState["no_of_biscut_bought"], 'biscuit'):
            biscuits = product.query_all_biscuits()         
            for biscuit in biscuits:
                my_biscuit = list(biscuit)
                if "Oreo" == my_biscuit[1]:
                    if checkWeHaveEnoughtDrinks(my_biscuit[3], "Oreo",  my_biscuit[2]):
                        vendingState["no_of_biscut_bought"] -= 1
                        update_vending_expense_amount(my_biscuit[2])
                        product.update_biscuit(my_biscuit[0], my_biscuit[1], my_biscuit[2], my_biscuit[3]-1)
                        my_Oreo.config(image=new_pic8,bg="#000000",border=0,borderwidth=0)
                        my_Oreo = Label(item2,image="",bg="#000000")
                        my_Oreo.place(x=10,y=10)

    image8 = Image.open("public/Oreo.png")
    resized = image8.resize((120,85), Image.Resampling.LANCZOS)
    new_pic8 = ImageTk.PhotoImage(resized)
    Oreo_img = Label(goods, image=new_pic8,borderwidth=0,border=0,bg="#000000")
    Oreo_img.place(x=170,y=145)
    Oreo_btn = Button(goods, image=new_pic8,command=Oreo,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Oreo_btn.place(x=170,y=145)

    def Digestive():
        if checkAuthAndCurrency(vendingState["no_of_biscut_bought"], 'biscuit'):
            biscuits = product.query_all_biscuits()         
            for biscuit in biscuits:
                my_biscuit = list(biscuit)
                if "Digestive" == my_biscuit[1]:
                    if checkWeHaveEnoughtDrinks(my_biscuit[3], "Digestive",  my_biscuit[2]):
                        vendingState["no_of_biscut_bought"] -= 1
                        update_vending_expense_amount(my_biscuit[2])
                        product.update_biscuit(my_biscuit[0], my_biscuit[1], my_biscuit[2], my_biscuit[3]-1)
                        my_Digestive.config(image=new_pic9,bg="#000000",border=0,borderwidth=0)
                        my_Digestive = Label(item2,image="",bg="#000000")
                        my_Digestive.place(x=10,y=10)
    image9 = Image.open("public/Digestive.png")
    resized = image9.resize((100,85), Image.Resampling.LANCZOS)
    new_pic9 = ImageTk.PhotoImage(resized)
    Digestive_img = Label(goods, image=new_pic9,borderwidth=0,border=0,bg="#000000")
    Digestive_img.place(x=318,y=145)
    Digestive_btn = Button(goods, image=new_pic9,command=Digestive,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Digestive_btn.place(x=318,y=145)

    def Hide_And_Seek():
        if checkAuthAndCurrency(vendingState["no_of_biscut_bought"], 'biscuit'):
            biscuits = product.query_all_biscuits()         
            for biscuit in biscuits:
                my_biscuit = list(biscuit)
                if "Hide_And_Seek" == my_biscuit[1]:
                    if checkWeHaveEnoughtDrinks(my_biscuit[3], "Hide_And_Seek",  my_biscuit[2]):
                        vendingState["no_of_biscut_bought"] -= 1
                        update_vending_expense_amount(my_biscuit[2])
                        product.update_biscuit(my_biscuit[0], my_biscuit[1], my_biscuit[2], my_biscuit[3]-1)
                        my_Hide_And_Seek.config(image=new_pic10,bg="#000000",border=0,borderwidth=0)
                        my_Hide_And_Seek = Label(item2,image="",bg="#000000")
                        my_Hide_And_Seek.place(x=10,y=10)
    image10 = Image.open("public/Hide_And_Seek.png")
    resized = image10.resize((100,85), Image.Resampling.LANCZOS)
    new_pic10 = ImageTk.PhotoImage(resized)
    Hide_And_Seek_img = Label(goods, image=new_pic10,borderwidth=0,border=0,bg="#000000")
    Hide_And_Seek_img.place(x=470,y=145)
    Hide_And_Seek_btn = Button(goods, image=new_pic10,command=Hide_And_Seek,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Hide_And_Seek_btn.place(x=470,y=145)

    def Dorritos():
        if checkAuthAndCurrency(vendingState["no_of_chips_bought"], 'Chips'):
            chips = product.query_all_chips()         
            for chip in chips:
                my_chip = list(chip)
                if "Dorritos" == my_chip[1]:
                    if checkWeHaveEnoughtDrinks(my_chip[3], "Dorritos",  my_chip[2]):
                        vendingState["no_of_chips_bought"] -= 1
                        update_vending_expense_amount(my_chip[2])
                        product.update_biscuit(my_chip[0], my_chip[1], my_chip[2], my_chip[3]-1)
                        Dorritos_btn.config(image=new_pic12,bg="#000000",border=0,borderwidth=0)
                        Dorritos_btn = Label(item2,image="",bg="#000000")
                        Dorritos_btn.place(x=10,y=10)
    image12 = Image.open("public/Dorritos.png")
    resized = image12.resize((80,85), Image.Resampling.LANCZOS)
    new_pic12 = ImageTk.PhotoImage(resized)
    Dorritos_img = Label(goods, image=new_pic12,borderwidth=0,border=0,bg="#000000")
    Dorritos_img.place(x=40,y=270)
    Dorritos_btn = Button(goods, image=new_pic12,command=Dorritos,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Dorritos_btn.place(x=40,y=270)

    def Lays():
        if checkAuthAndCurrency(vendingState["no_of_chips_bought"], 'Chips'):
            chips = product.query_all_chips()         
            for chip in chips:
                my_chip = list(chip)
                if "Lays" == my_chip[1]:
                    if checkWeHaveEnoughtDrinks(my_chip[3], "Lays",  my_chip[2]):
                        vendingState["no_of_chips_bought"] -= 1
                        update_vending_expense_amount(my_chip[2])
                        product.update_chips(my_chip[0], my_chip[1], my_chip[2], my_chip[3]-1)
                        my_Lays.config(image=new_pic13,bg="#000000",border=0,borderwidth=0)
                        my_Lays = Label(item3,image="",bg="#000000")
                        my_Lays.place(x=1,y=10)
    image13 = Image.open("public/Lays.png")
    resized = image13.resize((120,85), Image.Resampling.LANCZOS)
    new_pic13 = ImageTk.PhotoImage(resized)
    Lays_img = Label(goods, image=new_pic13,borderwidth=0,border=0,bg="#000000")
    Lays_img.place(x=170,y=270)
    Lays_btn = Button(goods, image=new_pic13,command=Lays,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Lays_btn.place(x=170,y=270)
    my_Lays = Label(item3,image="",bg="#000000")
    my_Lays.place(x=1,y=10)

    def Local_Chips():
        if checkAuthAndCurrency(vendingState["no_of_chips_bought"], 'Chips'):
            chips = product.query_all_chips()         
            for chip in chips:
                my_chip = list(chip)
                if "Local_Chips" == my_chip[1]:
                    if checkWeHaveEnoughtDrinks(my_chip[3], "Local_Chips",  my_chip[2]):
                        vendingState["no_of_chips_bought"] -= 1
                        update_vending_expense_amount(my_chip[2])
                        product.update_chips(my_chip[0], my_chip[1], my_chip[2], my_chip[3]-1)
                        my_Local_Chips.config(image=new_pic14,bg="#000000",border=0,borderwidth=0)
                        my_Local_Chips = Label(item3,image="",bg="#000000")
                        my_Local_Chips.place(x=1,y=10)

    image14 = Image.open("public/Local_Chips.png")
    resized = image14.resize((80,100), Image.Resampling.LANCZOS)
    new_pic14 = ImageTk.PhotoImage(resized)
    Local_Chips_img = Label(goods, image=new_pic14,borderwidth=0,border=0,bg="#000000")
    Local_Chips_img.place(x=325,y=270)
    Local_Chips_btn = Button(goods, image=new_pic14,command=Local_Chips,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Local_Chips_btn.place(x=325,y=270)

    def Uncle_Chips():
        if checkAuthAndCurrency(vendingState["no_of_chips_bought"], 'Chips'):
            chips = product.query_all_chips()         
            for chip in chips:
                my_chip = list(chip)
                if "Uncle_Chips" == my_chip[1]:
                    if checkWeHaveEnoughtDrinks(my_chip[3], "Uncle_Chips", my_chip[2]):
                        vendingState["no_of_chips_bought"] -= 1
                        update_vending_expense_amount(my_chip[2])
                        product.update_chips(my_chip[0], my_chip[1], my_chip[2], my_chip[3]-1)
                        my_Uncle_Chips.config(image=new_pic15,bg="#000000",border=0,borderwidth=0)
                        my_Uncle_Chips = Label(item3,image="",bg="#000000")
                        my_Uncle_Chips.place(x=1,y=10)

    image15 = Image.open("public/Uncle_Chips.png")
    resized = image15.resize((80,85), Image.Resampling.LANCZOS)
    new_pic15 = ImageTk.PhotoImage(resized)
    Uncle_Chips_img = Label(goods, image=new_pic15,borderwidth=0,border=0,bg="#000000")
    Uncle_Chips_img.place(x=475,y=270)
    Uncle_Chips_btn = Button(goods, image=new_pic15,command=Uncle_Chips,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Uncle_Chips_btn.place(x=475,y=270)

    def Snickers():
        if checkAuthAndCurrency(vendingState["no_of_chocolate_bought"], 'Chocolate'):
            chocolates = product.query_all_chocolates()         
            for chocolate in chocolates:
                my_chocolate = list(chocolate)
                if "Snickers" == my_chocolate[1]:
                    if checkWeHaveEnoughtDrinks(my_chocolate[3], "Snickers",  my_chocolate[2]):
                        vendingState["no_of_chocolate_bought"] -= 1
                        update_vending_expense_amount(my_chocolate[2])
                        product.update_chips(my_chocolate[0], my_chocolate[1], my_chocolate[2], my_chocolate[3]-1)
                        my_Snickers.config(image=new_pic17,bg="#000000",border=0,borderwidth=0)
                        my_Snickers = Label(item4,image="",bg="#000000")
                        my_Snickers.place(x=1,y=10)

    image17 = Image.open("public/Snickers.png")
    resized = image17.resize((120,85), Image.Resampling.LANCZOS)
    new_pic17 = ImageTk.PhotoImage(resized)
    Snickers_img = Label(goods, image=new_pic17,borderwidth=0,border=0,bg="#000000")
    Snickers_img.place(x=22,y=395)
    Snickers_btn = Button(goods, image=new_pic17,command=Snickers,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Snickers_btn.place(x=22,y=395)

    def Twix():
        if checkAuthAndCurrency(vendingState["no_of_chocolate_bought"], 'Chocolate'):
            chocolates = product.query_all_chocolates()         
            for chocolate in chocolates:
                my_chocolate = list(chocolate)
                if "Twix" == my_chocolate[1]:
                    if checkWeHaveEnoughtDrinks(my_chocolate[3], "Twix", my_chocolate[2]):
                        vendingState["no_of_chocolate_bought"] -= 1
                        update_vending_expense_amount(my_chocolate[2])
                        product.update_chips(my_chocolate[0], my_chocolate[1], my_chocolate[2], my_chocolate[3]-1)
                        my_Twix.config(image=new_pic18,bg="#000000",border=0,borderwidth=0)
                        my_Twix = Label(item4,image="",bg="#000000")
                        my_Twix.place(x=1,y=10)

    image18 = Image.open("public/Twix.png")
    resized = image18.resize((120,85), Image.Resampling.LANCZOS)
    new_pic18 = ImageTk.PhotoImage(resized)
    Twix_img = Label(goods, image=new_pic18,borderwidth=0,border=0,bg="#000000")
    Twix_img.place(x=170,y=395)
    Twix_btn = Button(goods, image=new_pic18,command=Twix,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Twix_btn.place(x=170,y=395)

    def Rafello():
        if checkAuthAndCurrency(vendingState["no_of_chocolate_bought"], 'Chocolate'):
            chocolates = product.query_all_chocolates()         
            for chocolate in chocolates:
                my_chocolate = list(chocolate)
                if "Rafello" == my_chocolate[1]:
                    if checkWeHaveEnoughtDrinks(my_chocolate[3], "Rafello", my_chocolate[2]):
                        vendingState["no_of_chocolate_bought"] -= 1
                        update_vending_expense_amount(my_chocolate[2])
                        product.update_chips(my_chocolate[0], my_chocolate[1], my_chocolate[2], my_chocolate[3]-1)
                        my_Rafello.config(image=new_pic19,bg="#000000",border=0,borderwidth=0)
                        my_Rafello = Label(item4,image="",bg="#000000")
                        my_Rafello.place(x=1,y=10)

    image19 = Image.open("public/Rafello.png")
    resized = image19.resize((120,85), Image.Resampling.LANCZOS)
    new_pic19 = ImageTk.PhotoImage(resized)
    Rafello_img = Label(goods, image=new_pic19,borderwidth=0,border=0,bg="#000000")
    Rafello_img.place(x=305,y=395)
    Rafello_btn = Button(goods, image=new_pic19,command=Rafello,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Rafello_btn.place(x=305,y=395)

    def Mars():
        if checkAuthAndCurrency(vendingState["no_of_chocolate_bought"], 'Chocolate'):
            chocolates = product.query_all_chocolates()         
            for chocolate in chocolates:
                my_chocolate = list(chocolate)
                if "Mars" == my_chocolate[1]:
                    if checkWeHaveEnoughtDrinks(my_chocolate[3], "Mars", my_chocolate[2]):
                        vendingState["no_of_chocolate_bought"] -= 1
                        update_vending_expense_amount(my_chocolate[2])
                        product.update_chips(my_chocolate[0], my_chocolate[1], my_chocolate[2], my_chocolate[3]-1)
                        my_Mars.config(image=new_pic20,bg="#000000",border=0,borderwidth=0)
                        my_Mars = Label(item4,image="",bg="#000000")
                        my_Mars.place(x=1,y=10)

    image20 = Image.open("public/Mars.png")
    resized = image20.resize((128,85), Image.Resampling.LANCZOS)
    new_pic20 = ImageTk.PhotoImage(resized)
    Mars_img = Label(goods, image=new_pic20,borderwidth=0,border=0,bg="#000000")
    Mars_img.place(x=440,y=395)
    Mars_btn = Button(goods, image=new_pic20,command=Mars,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Mars_btn.place(x=440,y=395)
    
    cokee = Label(goods,text="Coke",bg="#000000",fg="white")
    cokee.place(x=63,y=110)

    fanta = Label(goods,text="Fanta",bg="#000000",fg="white")
    fanta.place(x=215,y=110)

    sprite = Label(goods,text="Sprite",bg="#000000",fg="white")
    sprite.place(x=345,y=110)

    pepsi = Label(goods,text="Pepsi",bg="#000000",fg="white")
    pepsi.place(x=500,y=110)

    bonbon = Label(goods,text="Bourbon",bg="#000000",fg="white")
    bonbon.place(x=58,y=235)

    oreo = Label(goods,text="Oreo",bg="#000000",fg="white")
    oreo.place(x=215,y=235)

    digestive = Label(goods,text="Digestive",bg="#000000",fg="white")
    digestive.place(x=340,y=235)

    hide_and_Seek = Label(goods,text="Hide and Seek",bg="#000000",fg="white")
    hide_and_Seek.place(x=480,y=235)

    dorritos = Label(goods,text="Dorritos",bg="#000000",fg="white")
    dorritos.place(x=58,y=360)

    lays = Label(goods,text="Lays",bg="#000000",fg="white")
    lays.place(x=215,y=360)

    local_chips = Label(goods,text="Local Chips",bg="#000000",fg="white")
    local_chips.place(x=335,y=360)

    uncle_chips = Label(goods,text="Uncle Chips",bg="#000000",fg="white")
    uncle_chips.place(x=480,y=360)

    snickers = Label(goods,text="Snickers",bg="#000000",fg="white")
    snickers.place(x=57,y=485)

    twix = Label(goods,text="Twix",bg="#000000",fg="white")
    twix.place(x=215,y=485)

    rafello = Label(goods,text="Rafello",bg="#000000",fg="white")
    rafello.place(x=345,y=485)

    mars = Label(goods,text="Mars",bg="#000000",fg="white")
    mars.place(x=496,y=485)
