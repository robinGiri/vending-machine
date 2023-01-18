from tkinter import *
import seed
from PIL import Image,ImageTk


def products(main, vendingState):
    print(vendingState)
    
    def delete():
        my_coke.place_forget()
        
        
    
    productList = seed.productList
    # TODO call product list and 
    # productList = beautiful changes :)
  

    goods = Frame(main, width=600,height=570,bg="#000000")
    goods.place(x=220,y=40)

    item = Frame(main, width=600,height=130,bg="#000000")
    item.place(x=220,y=640)

    item1 = Frame(item, width=100,height=110,bg="#000000")
    item1.place(x=20,y=10)

    item2 = Frame(item, width=100,height=110,bg="#000000")
    item2.place(x=170,y=10)

    item3 = Frame(item, width=100,height=110,bg="#000000")
    item3.place(x=320,y=10)


    item4 = Frame(item, width=100,height=110,bg="#000000")
    item4.place(x=470,y=10)
    
    def drinkk():
        my_drinkk.config(image=new_pic1,bg="#000000",border=0,borderwidth=0)
    image1 = Image.open("public/Drinks.png")
    resized = image1.resize((100,85), Image.Resampling.LANCZOS)
    new_pic1 = ImageTk.PhotoImage(resized)
    drinkk_img = Label(goods, image=new_pic1,borderwidth=0,border=0,bg="#000000")
    drinkk_img.place(x=30,y=52)
    drinkk_btn = Button(goods, image=new_pic1,command=drinkk,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    drinkk_btn.place(x=30,y=52)
    my_drinkk = Label(item1,image="",bg="#000000")

    
    def biscuitss():
        my_biscuitss.config(image=new_pic6,bg="#000000",border=0,borderwidth=0)
    image6 = Image.open("public/Drinks.png")
    resized = image6.resize((100,85), Image.Resampling.LANCZOS)
    new_pic6 = ImageTk.PhotoImage(resized)
    biscuitss_img = Label(goods, image=new_pic6,borderwidth=0,border=0,bg="#000000")
    biscuitss_img.place(x=30,y=172)
    biscuitss_btn = Button(goods, image=new_pic6,command=biscuitss,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    biscuitss_btn.place(x=30,y=172)
    my_biscuitss = Label(item2,image="",bg="#000000")
    
    
        
    def Chipss():
        my_chipss.config(image=new_pic11,bg="#000000",border=0,borderwidth=0)
    image11 = Image.open("public/Chips.png")
    resized = image11.resize((100,85), Image.Resampling.LANCZOS)
    new_pic11 = ImageTk.PhotoImage(resized)
    chipss_img = Label(goods, image=new_pic11,borderwidth=0,border=0,bg="#000000")
    chipss_img.place(x=30,y=292)
    chipss_btn = Button(goods, image=new_pic11,command=Chipss,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    chipss_btn.place(x=30,y=292)
    my_chipss = Label(item2,image="",bg="#000000")
    
    
    def Chocolatess():
        my_chocolates.config(image=new_pic16,bg="#000000",border=0,borderwidth=0)
    image16 = Image.open("public/Chips.png")
    resized = image16.resize((100,85), Image.Resampling.LANCZOS)
    new_pic16 = ImageTk.PhotoImage(resized)
    chocolates_img = Label(goods, image=new_pic16,borderwidth=0,border=0,bg="#000000")
    chocolates_img.place(x=30,y=412)
    chocolates_btn = Button(goods, image=new_pic16,command=Chocolatess,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    chocolates_btn.place(x=30,y=412)
    my_chocolates = Label(item2,image="",bg="#000000")

    
    
    def coke():
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
    
    
    """
    # TODO call rest in simlar patter 
    def name(start, end, name ):
        name_lable = Label(main, bg="#000000",fg="white")
        name_lable.config(text=name)
        name_lable.place(x=start,y=end)
    
    def price(start, end, name ):
        price_lable = Label(main, bg="#000000",fg="white")
        price_lable.config(text="Price: {}".format(name))
        price_lable.place(x=start,y=end)
    
    def quantity(start, end, name ):
        quantity_lable = Label(main, bg="#000000",fg="white")
        quantity_lable.config(text="Quantity: {}".format(name))
        quantity_lable.place(x=start,y=end)

    fanta = Label(main,text="Fanta",bg="#000000",fg="white")
    fanta.place(x=450,y=180)

    sprite = Label(main,text="Sprite",bg="#000000",fg="white")
    sprite.place(x=550,y=180)

    slice = Label(main,text="Slice",bg="#000000",fg="white")
    slice.place(x=650,y=180)

    biscuits = Label(main, text="Biscuits",bg="#000000",fg="white")
    biscuits.place(x=210,y=300)

    bonbon = Label(main,text="Bonbon",bg="#000000",fg="white")
    bonbon.place(x=340,y=300)

    oreo = Label(main,text="Oreo",bg="#000000",fg="white")
    oreo.place(x=450,y=300)

    digestive = Label(main,text="Digestive",bg="#000000",fg="white")
    digestive.place(x=540,y=300)

    hide_and_sick = Label(main,text="Hide and Sick",bg="#000000",fg="white")
    hide_and_sick.place(x=630,y=300)

    chips = Label(main, text="Chips",bg="#000000",fg="white")
    chips.place(x=210,y=420)

    dorritos = Label(main,text="Dorritos",bg="#000000",fg="white")
    dorritos.place(x=340,y=420)

    lays = Label(main,text="Lays",bg="#000000",fg="white")
    lays.place(x=450,y=420)

    local_chips = Label(main,text="Local Chips",bg="#000000",fg="white")
    local_chips.place(x=540,y=420)

    uncle_chips = Label(main,text="Uncle Chips",bg="#000000",fg="white")
    uncle_chips.place(x=640,y=420)

    chocolates = Label(main, text="Chocolates",bg="#000000",fg="white")
    chocolates.place(x=195,y=540)

    snickers = Label(main,text="Snickers",bg="#000000",fg="white")
    snickers.place(x=340,y=540)

    twix = Label(main,text="Twix",bg="#000000",fg="white")
    twix.place(x=450,y=540)


    name(550, 540, productList['Chocolates']['Rafaello']["name"])
    price(550, 560, productList['Chocolates']['Rafaello']["price"])
    quantity(550, 580, productList['Chocolates']['Rafaello']["quantity"])

    name(650, 540, productList['Chocolates']['Mars']["name"])
    price(640, 560, productList['Chocolates']['Mars']["price"])
    quantity(640, 580, productList['Chocolates']['Mars']["quantity"])

    """