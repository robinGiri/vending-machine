from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import product

def products(main, vendingState):
    '''
    @params: main and vanding state are params
    we are making main items clickable
    after clicking delete quantity from DB
    and reduce input currency
    '''

    def withdrawProduct(productType, itemType):
        if vendingState["is_authenticated"] == False :
            messagebox.showerror("error", "Please Login First")
            return
        '''
        @param: ptoductType
        reduce currency from vending store
        delete product from DB
        '''
        if productType == "Drinks":
            drinks = product.query_all_drinks()
            for drink in drinks:
                if itemType == drink[1]:
                    product.update_drink(drink[0], drink[1], drink[2], drink[3]-1)
                    vendingState["input_currency"]=- drink[2]
        if productType == "Chips":
            drinks = product.query_all_chips()
            for chips in chips:
                if itemType == chips[1]:
                    product.update_chips(chips[0], chips[1], chips[2], chips[3]-1)
                    vendingState["input_currency"]=- chips[2]
        

    goods = Frame(main, width=600,height=570,bg="#000000")
    goods.place(x=135,y=40)

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

    # product side bare which are unclickable
    def drinks_collection():
        my_drinks_collection.config(image=new_pic1,bg="#000000",border=0,borderwidth=0)
    image1 = Image.open("public/Drinks.png")
    resized = image1.resize((100,85), Image.Resampling.LANCZOS)
    new_pic1 = ImageTk.PhotoImage(resized)
    drinks_collection_img = Label(goods, image=new_pic1,borderwidth=0,border=0,bg="#000000")
    drinks_collection_img.place(x=30,y=52)
    drinks_collection_btn = Button(goods, image=new_pic1,command=drinks_collection,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    drinks_collection_btn.place(x=30,y=52)
    my_drinks_collection = Label(item1,image="",bg="#000000")

    
    def biscuits_collection():
        my_biscuits_collection.config(image=new_pic6,bg="#000000",border=0,borderwidth=0)
    image6 = Image.open("public/Drinks.png")
    resized = image6.resize((100,85), Image.Resampling.LANCZOS)
    new_pic6 = ImageTk.PhotoImage(resized)
    biscuits_collection_img = Label(goods, image=new_pic6,borderwidth=0,border=0,bg="#000000")
    biscuits_collection_img.place(x=30,y=172)
    biscuits_collection_btn = Button(goods, image=new_pic6,command=biscuits_collection,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    biscuits_collection_btn.place(x=30,y=172)
    my_biscuits_collection = Label(item2,image="",bg="#000000")
    
 
    def Chips_collection():
        my_chips_collection.config(image=new_pic11,bg="#000000",border=0,borderwidth=0)
    image11 = Image.open("public/Chips.png")
    resized = image11.resize((100,85), Image.Resampling.LANCZOS)
    new_pic11 = ImageTk.PhotoImage(resized)
    chips_collection_img = Label(goods, image=new_pic11,borderwidth=0,border=0,bg="#000000")
    chips_collection_img.place(x=30,y=292)
    chips_collection_btn = Button(goods, image=new_pic11,command=Chips_collection,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    chips_collection_btn.place(x=30,y=292)
    my_chips_collection = Label(item2,image="",bg="#000000")
    
    
    def Chocolates_collections():
        my_chocolates.config(image=new_pic16,bg="#000000",border=0,borderwidth=0)
    image16 = Image.open("public/Chips.png")
    resized = image16.resize((100,85), Image.Resampling.LANCZOS)
    new_pic16 = ImageTk.PhotoImage(resized)
    chocolates_img = Label(goods, image=new_pic16,borderwidth=0,border=0,bg="#000000")
    chocolates_img.place(x=30,y=412)
    chocolates_btn = Button(goods, image=new_pic16,command=Chocolates_collections,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    chocolates_btn.place(x=30,y=412)
    my_chocolates = Label(item2,image="",bg="#000000")


    # clickable individual products
    def coke():
        withdrawProduct("Drinks", "Coke")
        my_coke.config(image=new_pic2,bg="#000000",border=0,borderwidth=0)
    image2 = Image.open("public/Coke.png")
    resized = image2.resize((60,85), Image.Resampling.LANCZOS)
    new_pic2 = ImageTk.PhotoImage(resized)
    coke_img = Label(goods, image=new_pic2,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=185,y=50)
    coke_btn = Button(goods, image=new_pic2,command=coke,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    coke_btn.place(x=185,y=50)
    my_coke = Label(item1,image="",bg="#000000")
    my_coke.place(x=10,y=10)

    def Fanta():
        withdrawProduct("Drinks", "Fanta")
        my_Fanta.config(image=new_pic3,bg="#000000",border=0,borderwidth=0)
    image3 = Image.open("public/Fanta.png")
    resized = image3.resize((60,85), Image.Resampling.LANCZOS)
    new_pic3 = ImageTk.PhotoImage(resized)
    Fanta_img = Label(goods, image=new_pic3,borderwidth=0,border=0,bg="#000000")
    Fanta_img.place(x=285,y=50)
    Fanta_btn = Button(goods, image=new_pic3,command=Fanta,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Fanta_btn.place(x=285,y=50)
    my_Fanta = Label(item1,image="",bg="#000000")
    my_Fanta.place(x=10,y=10)

    def Sprite():
        withdrawProduct("Drinks", "Sprite")
        my_Sprite.config(image=new_pic4,bg="#000000",border=0,borderwidth=0)
    image4 = Image.open("public/Sprite.png")
    resized = image4.resize((130,90), Image.Resampling.LANCZOS)
    new_pic4 = ImageTk.PhotoImage(resized)
    Sprite_img = Label(goods, image=new_pic4,borderwidth=0,border=0,bg="#000000")
    Sprite_img.place(x=352,y=50)
    Sprite_btn = Button(goods, image=new_pic4,command=Sprite,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Sprite_btn.place(x=352,y=50)
    my_Sprite = Label(item1,image="",bg="#000000")
    my_Sprite.place(x=10,y=10)

    def Pepsi():
        withdrawProduct("Drinks", "Pepsi")
        my_Pepsi.config(image=new_pic5,bg="#000000",border=0,borderwidth=0)
    image5 = Image.open("public/Pepsi.png")
    resized = image5.resize((90,85), Image.Resampling.LANCZOS)
    new_pic5 = ImageTk.PhotoImage(resized)
    Pepsi_img = Label(goods, image=new_pic5,borderwidth=0,border=0,bg="#000000")
    Pepsi_img.place(x=470,y=50)
    Pepsi_btn = Button(goods, image=new_pic5,command=Pepsi,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Pepsi_btn.place(x=470,y=50)
    my_Pepsi = Label(item1,image="",bg="#000000")
    my_Pepsi.place(x=10,y=10)


    def Bonbon():
        my_Bonbon.config(image=new_pic7,bg="#000000",border=0,borderwidth=0)
    image7 = Image.open("public/Coke.png")
    resized = image7.resize((60,85), Image.Resampling.LANCZOS)
    new_pic7 = ImageTk.PhotoImage(resized)
    Bonbon_img = Label(goods, image=new_pic7,borderwidth=0,border=0,bg="#000000")
    Bonbon_img.place(x=185,y=170)
    Bonbon_btn = Button(goods, image=new_pic7,command=Bonbon,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Bonbon_btn.place(x=185,y=170)
    my_Bonbon = Label(item2,image="",bg="#000000")
    my_Bonbon.place(x=10,y=10)

    def Oreo():
        my_Oreo.config(image=new_pic8,bg="#000000",border=0,borderwidth=0)
    image8 = Image.open("public/Coke.png")
    resized = image3.resize((60,85), Image.Resampling.LANCZOS)
    new_pic8 = ImageTk.PhotoImage(resized)
    Oreo_img = Label(goods, image=new_pic8,borderwidth=0,border=0,bg="#000000")
    Oreo_img.place(x=285,y=170)
    Oreo_btn = Button(goods, image=new_pic8,command=Oreo,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Oreo_btn.place(x=285,y=170)
    my_Oreo = Label(item2,image="",bg="#000000")
    my_Oreo.place(x=10,y=10)

    def Digestive():
        my_Digestive.config(image=new_pic9,bg="#000000",border=0,borderwidth=0)
    image9 = Image.open("public/Coke.png")
    resized = image9.resize((60,85), Image.Resampling.LANCZOS)
    new_pic9 = ImageTk.PhotoImage(resized)
    Digestive_img = Label(goods, image=new_pic9,borderwidth=0,border=0,bg="#000000")
    Digestive_img.place(x=385,y=170)
    Digestive_btn = Button(goods, image=new_pic9,command=Digestive,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Digestive_btn.place(x=385,y=170)
    my_Digestive = Label(item2,image="",bg="#000000")
    my_Digestive.place(x=10,y=10)

    def Hide_And_Sick():
        my_Hide_And_Sick.config(image=new_pic10,bg="#000000",border=0,borderwidth=0)
    image10 = Image.open("public/Coke.png")
    resized = image5.resize((60,85), Image.Resampling.LANCZOS)
    new_pic10 = ImageTk.PhotoImage(resized)
    Hide_And_Sick_img = Label(goods, image=new_pic10,borderwidth=0,border=0,bg="#000000")
    Hide_And_Sick_img.place(x=485,y=170)
    Hide_And_Sick_btn = Button(goods, image=new_pic10,command=Hide_And_Sick,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Hide_And_Sick_btn.place(x=485,y=170)
    my_Hide_And_Sick = Label(item2,image="",bg="#000000")
    my_Hide_And_Sick.place(x=10,y=10)


    def Dorritos():
        my_Dorritos.config(image=new_pic12,bg="#000000",border=0,borderwidth=0)
    image12 = Image.open("public/Dorritos.png")
    resized = image12.resize((80,85), Image.Resampling.LANCZOS)
    new_pic12 = ImageTk.PhotoImage(resized)
    Dorritos_img = Label(goods, image=new_pic12,borderwidth=0,border=0,bg="#000000")
    Dorritos_img.place(x=175,y=290)
    Dorritos_btn = Button(goods, image=new_pic12,command=Dorritos,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Dorritos_btn.place(x=175,y=290)
    my_Dorritos = Label(item3,image="",bg="#000000")
    my_Dorritos.place(x=10,y=10)

    def Lays():
        my_Lays.config(image=new_pic13,bg="#000000",border=0,borderwidth=0)
    image13 = Image.open("public/Lays.png")
    resized = image13.resize((120,85), Image.Resampling.LANCZOS)
    new_pic13 = ImageTk.PhotoImage(resized)
    Lays_img = Label(goods, image=new_pic13,borderwidth=0,border=0,bg="#000000")
    Lays_img.place(x=255,y=290)
    Lays_btn = Button(goods, image=new_pic13,command=Lays,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Lays_btn.place(x=255,y=290)
    my_Lays = Label(item3,image="",bg="#000000")
    my_Lays.place(x=1,y=10)

    def Local_Chips():
        my_Local_Chips.config(image=new_pic14,bg="#000000",border=0,borderwidth=0)
    image14 = Image.open("public/Local_Chips.png")
    resized = image14.resize((80,100), Image.Resampling.LANCZOS)
    new_pic14 = ImageTk.PhotoImage(resized)
    Local_Chips_img = Label(goods, image=new_pic14,borderwidth=0,border=0,bg="#000000")
    Local_Chips_img.place(x=385,y=285)
    Local_Chips_btn = Button(goods, image=new_pic14,command=Local_Chips,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Local_Chips_btn.place(x=385,y=285)
    my_Local_Chips = Label(item3,image="",bg="#000000")
    my_Local_Chips.place(x=10,y=10)

    def Uncle_Chips():
        my_Uncle_Chips.config(image=new_pic15,bg="#000000",border=0,borderwidth=0)
    image15 = Image.open("public/Uncle_Chips.png")
    resized = image15.resize((80,85), Image.Resampling.LANCZOS)
    new_pic15 = ImageTk.PhotoImage(resized)
    Uncle_Chips_img = Label(goods, image=new_pic15,borderwidth=0,border=0,bg="#000000")
    Uncle_Chips_img.place(x=480,y=290)
    Uncle_Chips_btn = Button(goods, image=new_pic15,command=Uncle_Chips,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Uncle_Chips_btn.place(x=480,y=290)
    my_Uncle_Chips = Label(item3,image="",bg="#000000")
    my_Uncle_Chips.place(x=10,y=10)

    def Snickers():
        my_Snickers.config(image=new_pic17,bg="#000000",border=0,borderwidth=0)
    image17 = Image.open("public/Coke.png")
    resized = image17.resize((60,85), Image.Resampling.LANCZOS)
    new_pic17 = ImageTk.PhotoImage(resized)
    Snickers_img = Label(goods, image=new_pic17,borderwidth=0,border=0,bg="#000000")
    Snickers_img.place(x=185,y=410)
    Snickers_btn = Button(goods, image=new_pic17,command=Snickers,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Snickers_btn.place(x=185,y=410)
    my_Snickers = Label(item4,image="",bg="#000000")
    my_Snickers.place(x=10,y=10)

    def Twix():
        my_Twix.config(image=new_pic18,bg="#000000",border=0,borderwidth=0)
    image18 = Image.open("public/Coke.png")
    resized = image3.resize((60,85), Image.Resampling.LANCZOS)
    new_pic18 = ImageTk.PhotoImage(resized)
    Twix_img = Label(goods, image=new_pic18,borderwidth=0,border=0,bg="#000000")
    Twix_img.place(x=285,y=410)
    Twix_btn = Button(goods, image=new_pic18,command=Twix,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Twix_btn.place(x=285,y=410)
    my_Twix = Label(item4,image="",bg="#000000")
    my_Twix.place(x=10,y=10)

    def Rafello():
        my_Rafello.config(image=new_pic19,bg="#000000",border=0,borderwidth=0)
    image19 = Image.open("public/Coke.png")
    resized = image19.resize((60,85), Image.Resampling.LANCZOS)
    new_pic19 = ImageTk.PhotoImage(resized)
    Rafello_img = Label(goods, image=new_pic19,borderwidth=0,border=0,bg="#000000")
    Rafello_img.place(x=385,y=410)
    Rafello_btn = Button(goods, image=new_pic19,command=Rafello,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Rafello_btn.place(x=385,y=410)
    my_Rafello = Label(item4,image="",bg="#000000")
    my_Rafello.place(x=10,y=10)

    def Mars():
        my_Mars.config(image=new_pic20,bg="#000000",border=0,borderwidth=0)
    image20 = Image.open("public/Coke.png")
    resized = image5.resize((60,85), Image.Resampling.LANCZOS)
    new_pic20 = ImageTk.PhotoImage(resized)
    Mars_img = Label(goods, image=new_pic20,borderwidth=0,border=0,bg="#000000")
    Mars_img.place(x=485,y=410)
    Mars_btn = Button(goods, image=new_pic20,command=Mars,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Mars_btn.place(x=485,y=410)
    my_Mars = Label(item4,image="",bg="#000000")
    my_Mars.place(x=10,y=10)

    Drinks = Label(goods, text="Drinks",bg="#000000",fg="white")
    Drinks.place(x=60,y=140)

    cokee = Label(goods,text="Coke",bg="#000000",fg="white")
    cokee.place(x=200,y=140)

    fanta = Label(goods,text="Fanta",bg="#000000",fg="white")
    fanta.place(x=300,y=140)

    sprite = Label(goods,text="Sprite",bg="#000000",fg="white")
    sprite.place(x=400,y=140)

    pepsi = Label(goods,text="Pepsi",bg="#000000",fg="white")
    pepsi.place(x=500,y=140)

    biscuits = Label(goods, text="Biscuits",bg="#000000",fg="white")
    biscuits.place(x=60,y=260)

    bonbon = Label(goods,text="Bonbon",bg="#000000",fg="white")
    bonbon.place(x=193,y=260)

    oreo = Label(goods,text="Oreo",bg="#000000",fg="white")
    oreo.place(x=300,y=260)

    digestive = Label(goods,text="Digestive",bg="#000000",fg="white")
    digestive.place(x=390,y=260)

    hide_and_sick = Label(goods,text="Hide and Sick",bg="#000000",fg="white")
    hide_and_sick.place(x=480,y=260)

    chips = Label(goods, text="Chips",bg="#000000",fg="white")
    chips.place(x=60,y=380)

    dorritos = Label(goods,text="Dorritos",bg="#000000",fg="white")
    dorritos.place(x=193,y=380)

    lays = Label(goods,text="Lays",bg="#000000",fg="white")
    lays.place(x=300,y=380)

    local_chips = Label(goods,text="Local Chips",bg="#000000",fg="white")
    local_chips.place(x=390,y=380)

    uncle_chips = Label(goods,text="Uncle Chips",bg="#000000",fg="white")
    uncle_chips.place(x=490,y=380)

    chocolates = Label(goods, text="Chocolates",bg="#000000",fg="white")
    chocolates.place(x=50,y=500)

    snickers = Label(goods,text="Snickers",bg="#000000",fg="white")
    snickers.place(x=190,y=500)

    twix = Label(goods,text="Twix",bg="#000000",fg="white")
    twix.place(x=300,y=500)

    rafello = Label(goods,text="Rafello",bg="#000000",fg="white")
    rafello.place(x=395,y=500)

    mars = Label(goods,text="Mars",bg="#000000",fg="white")
    mars.place(x=502,y=500)
