from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import register

def login(main):
    global state
    state = main
    
    def coke():
        my_coke.config(image=new_pic2,bg="#000000",border=0,borderwidth=0)
    image2 = Image.open("public/Coke.png")
    resized = image2.resize((60,85), Image.Resampling.LANCZOS)
    new_pic2 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic2,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=335,y=90)
    coke_btn = Button(main, image=new_pic2,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=335,y=90)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic3,bg="#000000",border=0,borderwidth=0)
    image3 = Image.open("public/Coke.png")
    resized = image3.resize((60,85), Image.Resampling.LANCZOS)
    new_pic3 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic3,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=435,y=90)
    coke_btn = Button(main, image=new_pic3,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=435,y=90)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic4,bg="#000000",border=0,borderwidth=0)
    image4 = Image.open("public/Coke.png")
    resized = image4.resize((60,85), Image.Resampling.LANCZOS)
    new_pic4 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic4,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=537,y=90)
    coke_btn = Button(main, image=new_pic4,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=537,y=90)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic5,bg="#000000",border=0,borderwidth=0)
    image5 = Image.open("public/Coke.png")
    resized = image5.resize((60,85), Image.Resampling.LANCZOS)
    new_pic5 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic5,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=635,y=90)
    coke_btn = Button(main, image=new_pic5,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=635,y=90)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)


    def coke():
        my_coke.config(image=new_pic7,bg="#000000",border=0,borderwidth=0)
    image7 = Image.open("public/Coke.png")
    resized = image7.resize((60,85), Image.Resampling.LANCZOS)
    new_pic7 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic7,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=335,y=220)
    coke_btn = Button(main, image=new_pic7,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=335,y=220)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic8,bg="#000000",border=0,borderwidth=0)
    image8 = Image.open("public/Coke.png")
    resized = image3.resize((60,85), Image.Resampling.LANCZOS)
    new_pic8 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic8,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=435,y=220)
    coke_btn = Button(main, image=new_pic8,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=435,y=220)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic9,bg="#000000",border=0,borderwidth=0)
    image9 = Image.open("public/Coke.png")
    resized = image9.resize((60,85), Image.Resampling.LANCZOS)
    new_pic9 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic9,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=537,y=220)
    coke_btn = Button(main, image=new_pic9,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=537,y=220)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic10,bg="#000000",border=0,borderwidth=0)
    image10 = Image.open("public/Coke.png")
    resized = image5.resize((60,85), Image.Resampling.LANCZOS)
    new_pic10 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic10,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=635,y=220)
    coke_btn = Button(main, image=new_pic10,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=635,y=220)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)


    def Dorritos():
        my_Dorritos.config(image=new_pic12,bg="#000000",border=0,borderwidth=0)
    image12 = Image.open("public/Dorritos.png")
    resized = image12.resize((80,85), Image.Resampling.LANCZOS)
    new_pic12 = ImageTk.PhotoImage(resized)
    Dorritos_img = Label(main, image=new_pic12,borderwidth=0,border=0,bg="#000000")
    Dorritos_img.place(x=323,y=335)
    Dorritos_btn = Button(main, image=new_pic12,command=Dorritos,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    Dorritos_btn.place(x=323,y=335)
    my_Dorritos = Label(main,image="",bg="#000000")
    my_Dorritos.place(x=450,y=630)

    def Lays():
        my_Lays.config(image=new_pic13,bg="#000000",border=0,borderwidth=0)
    image13 = Image.open("public/Lays.png")
    resized = image13.resize((120,85), Image.Resampling.LANCZOS)
    new_pic13 = ImageTk.PhotoImage(resized)
    Lays_img = Label(main, image=new_pic13,borderwidth=0,border=0,bg="#000000")
    Lays_img.place(x=410,y=335)
    Lays_btn = Button(main, image=new_pic13,command=Lays,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    Lays_btn.place(x=410,y=335)
    my_Lays = Label(main,image="",bg="#000000")
    my_Lays.place(x=450,y=630)

    def Local_Chips():
        my_Local_Chips.config(image=new_pic14,bg="#000000",border=0,borderwidth=0)
    image14 = Image.open("public/Local_Chips.png")
    resized = image14.resize((80,100), Image.Resampling.LANCZOS)
    new_pic14 = ImageTk.PhotoImage(resized)
    Local_Chips_img = Label(main, image=new_pic14,borderwidth=0,border=0,bg="#000000")
    Local_Chips_img.place(x=535,y=331)
    Local_Chips_btn = Button(main, image=new_pic14,command=Local_Chips,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    Local_Chips_btn.place(x=535,y=331)
    my_Local_Chips = Label(main,image="",bg="#000000")
    my_Local_Chips.place(x=450,y=630)

    def Uncle_Chips():
        my_Uncle_Chips.config(image=new_pic15,bg="#000000",border=0,borderwidth=0)
    image15 = Image.open("public/Uncle_Chips.png")
    resized = image15.resize((80,85), Image.Resampling.LANCZOS)
    new_pic15 = ImageTk.PhotoImage(resized)
    Uncle_Chips_img = Label(main, image=new_pic15,borderwidth=0,border=0,bg="#000000")
    Uncle_Chips_img.place(x=635,y=335)
    Uncle_Chips_btn = Button(main, image=new_pic15,command=Uncle_Chips,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    Uncle_Chips_btn.place(x=635,y=335)
    my_Uncle_Chips = Label(main,image="",bg="#000000")
    my_Uncle_Chips.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic17,bg="#000000",border=0,borderwidth=0)
    image17 = Image.open("public/Coke.png")
    resized = image17.resize((60,85), Image.Resampling.LANCZOS)
    new_pic17 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic17,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=335,y=460)
    coke_btn = Button(main, image=new_pic17,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=335,y=460)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic18,bg="#000000",border=0,borderwidth=0)
    image18 = Image.open("public/Coke.png")
    resized = image3.resize((60,85), Image.Resampling.LANCZOS)
    new_pic18 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic18,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=435,y=458)
    coke_btn = Button(main, image=new_pic18,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=435,y=458)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic19,bg="#000000",border=0,borderwidth=0)
    image19 = Image.open("public/Coke.png")
    resized = image19.resize((60,85), Image.Resampling.LANCZOS)
    new_pic19 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic19,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=537,y=458)
    coke_btn = Button(main, image=new_pic19,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=537,y=458)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)

    def coke():
        my_coke.config(image=new_pic20,bg="#000000",border=0,borderwidth=0)
    image20 = Image.open("public/Coke.png")
    resized = image5.resize((60,85), Image.Resampling.LANCZOS)
    new_pic20 = ImageTk.PhotoImage(resized)
    coke_img = Label(main, image=new_pic20,borderwidth=0,border=0,bg="#000000")
    coke_img.place(x=635,y=458)
    coke_btn = Button(main, image=new_pic20,command=coke,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    coke_btn.place(x=635,y=458)
    my_coke = Label(main,image="",bg="#000000")
    my_coke.place(x=450,y=630)
    
    drinks = Label(main, text="Drinks",bg="#000000",fg="white")
    drinks.place(x=210,y=180)

    coke = Label(main,text="Coke",bg="#000000",fg="white")
    coke.place(x=350,y=180)

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

    rafello = Label(main,text="Rafello",bg="#000000",fg="white")
    rafello.place(x=550,y=540)

    mars = Label(main,text="Mars",bg="#000000",fg="white")
    mars.place(x=650,y=540)

    def use(usee):
        username.config(state=NORMAL)
        username.delete(0, END)
    def pas(passs):
        password.config(state=NORMAL)
        password.delete(0, END)
        
    def top():

        if username.get() == "":
            messagebox.showerror("error", "Username Should Not Be Empty")
        elif password.get() == "":
            messagebox.showerror("error", "Password Should Not Be Empty")
            
        elif len(password.get()) <8:
            messagebox.showerror("error", "Wrong Password")
            
        elif "@" not in password.get():
            messagebox.showerror("error","Wrong Password")
                    
        elif  "   Username" in username.get():
            messagebox.showerror("error", "Enter Username")       
            
        elif "*******@" in password.get():
            messagebox.showerror("error", "Enter Password")   
            
        else:        
            def coke():
                my_coke.config(image=new_pic2,bg="#000000",border=0,borderwidth=0)
            image2 = Image.open("public/Coke.png")
            resized = image2.resize((60,85), Image.Resampling.LANCZOS)
            new_pic2 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic2,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=335,y=90)
            coke_btn = Button(main, image=new_pic2,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=335,y=90)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic3,bg="#000000",border=0,borderwidth=0)
            image3 = Image.open("public/Coke.png")
            resized = image3.resize((60,85), Image.Resampling.LANCZOS)
            new_pic3 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic3,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=435,y=90)
            coke_btn = Button(main, image=new_pic3,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=435,y=90)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic4,bg="#000000",border=0,borderwidth=0)
            image4 = Image.open("public/Coke.png")
            resized = image4.resize((60,85), Image.Resampling.LANCZOS)
            new_pic4 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic4,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=537,y=90)
            coke_btn = Button(main, image=new_pic4,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=537,y=90)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic5,bg="#000000",border=0,borderwidth=0)
            image5 = Image.open("public/Coke.png")
            resized = image5.resize((60,85), Image.Resampling.LANCZOS)
            new_pic5 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic5,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=635,y=90)
            coke_btn = Button(main, image=new_pic5,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=635,y=90)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)


            def coke():
                my_coke.config(image=new_pic7,bg="#000000",border=0,borderwidth=0)
            image7 = Image.open("public/Coke.png")
            resized = image7.resize((60,85), Image.Resampling.LANCZOS)
            new_pic7 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic7,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=335,y=220)
            coke_btn = Button(main, image=new_pic7,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=335,y=220)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic8,bg="#000000",border=0,borderwidth=0)
            image8 = Image.open("public/Coke.png")
            resized = image3.resize((60,85), Image.Resampling.LANCZOS)
            new_pic8 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic8,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=435,y=220)
            coke_btn = Button(main, image=new_pic8,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=435,y=220)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic9,bg="#000000",border=0,borderwidth=0)
            image9 = Image.open("public/Coke.png")
            resized = image9.resize((60,85), Image.Resampling.LANCZOS)
            new_pic9 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic9,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=537,y=220)
            coke_btn = Button(main, image=new_pic9,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=537,y=220)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic10,bg="#000000",border=0,borderwidth=0)
            image10 = Image.open("public/Coke.png")
            resized = image5.resize((60,85), Image.Resampling.LANCZOS)
            new_pic10 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic10,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=635,y=220)
            coke_btn = Button(main, image=new_pic10,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=635,y=220)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)


            def Dorritos():
                my_Dorritos.config(image=new_pic12,bg="#000000",border=0,borderwidth=0)
            image12 = Image.open("Dorritos.png")
            resized = image12.resize((80,85), Image.Resampling.LANCZOS)
            new_pic12 = ImageTk.PhotoImage(resized)
            Dorritos_img = Label(main, image=new_pic12,borderwidth=0,border=0,bg="#000000")
            Dorritos_img.place(x=323,y=335)
            Dorritos_btn = Button(main, image=new_pic12,command=Dorritos,border=0,borderwidth=0,bg="#000000")
            Dorritos_btn.place(x=323,y=335)
            my_Dorritos = Label(main,image="",bg="#000000")
            my_Dorritos.place(x=450,y=630)

            def Lays():
                my_Lays.config(image=new_pic13,bg="#000000",border=0,borderwidth=0)
            image13 = Image.open("Lays.png")
            resized = image13.resize((120,85), Image.Resampling.LANCZOS)
            new_pic13 = ImageTk.PhotoImage(resized)
            Lays_img = Label(main, image=new_pic13,borderwidth=0,border=0,bg="#000000")
            Lays_img.place(x=410,y=335)
            Lays_btn = Button(main, image=new_pic13,command=Lays,border=0,borderwidth=0,bg="#000000")
            Lays_btn.place(x=410,y=335)
            my_Lays = Label(main,image="",bg="#000000")
            my_Lays.place(x=450,y=630)

            def Local_Chips():
                my_Local_Chips.config(image=new_pic14,bg="#000000",border=0,borderwidth=0)
            image14 = Image.open("Local Chips.png")
            resized = image14.resize((80,100), Image.Resampling.LANCZOS)
            new_pic14 = ImageTk.PhotoImage(resized)
            Local_Chips_img = Label(main, image=new_pic14,borderwidth=0,border=0,bg="#000000")
            Local_Chips_img.place(x=535,y=331)
            Local_Chips_btn = Button(main, image=new_pic14,command=Local_Chips,border=0,borderwidth=0,bg="#000000")
            Local_Chips_btn.place(x=535,y=331)
            my_Local_Chips = Label(main,image="",bg="#000000")
            my_Local_Chips.place(x=450,y=630)

            def Uncle_Chips():
                my_Uncle_Chips.config(image=new_pic15,bg="#000000",border=0,borderwidth=0)
            image15 = Image.open("Uncle Chips.png")
            resized = image15.resize((80,85), Image.Resampling.LANCZOS)
            new_pic15 = ImageTk.PhotoImage(resized)
            Uncle_Chips_img = Label(main, image=new_pic15,borderwidth=0,border=0,bg="#000000")
            Uncle_Chips_img.place(x=635,y=335)
            Uncle_Chips_btn = Button(main, image=new_pic15,command=Uncle_Chips,border=0,borderwidth=0,bg="#000000")
            Uncle_Chips_btn.place(x=635,y=335)
            my_Uncle_Chips = Label(main,image="",bg="#000000")
            my_Uncle_Chips.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic17,bg="#000000",border=0,borderwidth=0)
            image17 = Image.open("public/Coke.png")
            resized = image17.resize((60,85), Image.Resampling.LANCZOS)
            new_pic17 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic17,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=335,y=460)
            coke_btn = Button(main, image=new_pic17,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=335,y=460)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic18,bg="#000000",border=0,borderwidth=0)
            image18 = Image.open("public/Coke.png")
            resized = image3.resize((60,85), Image.Resampling.LANCZOS)
            new_pic18 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic18,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=435,y=458)
            coke_btn = Button(main, image=new_pic18,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=435,y=458)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic19,bg="#000000",border=0,borderwidth=0)
            image19 = Image.open("public/Coke.png")
            resized = image19.resize((60,85), Image.Resampling.LANCZOS)
            new_pic19 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic19,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=537,y=458)
            coke_btn = Button(main, image=new_pic19,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=537,y=458)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)

            def coke():
                my_coke.config(image=new_pic20,bg="#000000",border=0,borderwidth=0)
            image20 = Image.open("public/Coke.png")
            resized = image5.resize((60,85), Image.Resampling.LANCZOS)
            new_pic20 = ImageTk.PhotoImage(resized)
            coke_img = Label(main, image=new_pic20,borderwidth=0,border=0,bg="#000000")
            coke_img.place(x=635,y=458)
            coke_btn = Button(main, image=new_pic20,command=coke,border=0,borderwidth=0,bg="#000000")
            coke_btn.place(x=635,y=458)
            my_coke = Label(main,image="",bg="#000000")
            my_coke.place(x=450,y=630)
            
            drinks = Label(main, text="Drinks",bg="#000000",fg="white")
            drinks.place(x=210,y=180)

            coke = Label(main,text="Coke",bg="#000000",fg="white")
            coke.place(x=350,y=180)

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

            rafello = Label(main,text="Rafello",bg="#000000",fg="white")
            rafello.place(x=550,y=540)

            mars = Label(main,text="Mars",bg="#000000",fg="white")
            mars.place(x=650,y=540)
            
            def cancel():
                Frame(main, width=100,height=100,bg="#000000").place(x=447,y=630)
                def coke():
                    my_coke.config(image=new_pic2,bg="#000000",border=0,borderwidth=0)
                image2 = Image.open("public/Coke.png")
                resized = image2.resize((60,85), Image.Resampling.LANCZOS)
                new_pic2 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic2,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=335,y=90)
                coke_btn = Button(main, image=new_pic2,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=335,y=90)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic3,bg="#000000",border=0,borderwidth=0)
                image3 = Image.open("public/Coke.png")
                resized = image3.resize((60,85), Image.Resampling.LANCZOS)
                new_pic3 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic3,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=435,y=90)
                coke_btn = Button(main, image=new_pic3,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=435,y=90)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic4,bg="#000000",border=0,borderwidth=0)
                image4 = Image.open("public/Coke.png")
                resized = image4.resize((60,85), Image.Resampling.LANCZOS)
                new_pic4 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic4,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=537,y=90)
                coke_btn = Button(main, image=new_pic4,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=537,y=90)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic5,bg="#000000",border=0,borderwidth=0)
                image5 = Image.open("public/Coke.png")
                resized = image5.resize((60,85), Image.Resampling.LANCZOS)
                new_pic5 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic5,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=635,y=90)
                coke_btn = Button(main, image=new_pic5,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=635,y=90)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)


                def coke():
                    my_coke.config(image=new_pic7,bg="#000000",border=0,borderwidth=0)
                image7 = Image.open("public/Coke.png")
                resized = image7.resize((60,85), Image.Resampling.LANCZOS)
                new_pic7 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic7,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=335,y=220)
                coke_btn = Button(main, image=new_pic7,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=335,y=220)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic8,bg="#000000",border=0,borderwidth=0)
                image8 = Image.open("public/Coke.png")
                resized = image3.resize((60,85), Image.Resampling.LANCZOS)
                new_pic8 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic8,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=435,y=220)
                coke_btn = Button(main, image=new_pic8,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=435,y=220)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic9,bg="#000000",border=0,borderwidth=0)
                image9 = Image.open("public/Coke.png")
                resized = image9.resize((60,85), Image.Resampling.LANCZOS)
                new_pic9 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic9,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=537,y=220)
                coke_btn = Button(main, image=new_pic9,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=537,y=220)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic10,bg="#000000",border=0,borderwidth=0)
                image10 = Image.open("public/Coke.png")
                resized = image5.resize((60,85), Image.Resampling.LANCZOS)
                new_pic10 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic10,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=635,y=220)
                coke_btn = Button(main, image=new_pic10,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=635,y=220)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)


                def Dorritos():
                    my_Dorritos.config(image=new_pic12,bg="#000000",border=0,borderwidth=0)
                image12 = Image.open("Dorritos.png")
                resized = image12.resize((80,85), Image.Resampling.LANCZOS)
                new_pic12 = ImageTk.PhotoImage(resized)
                Dorritos_img = Label(main, image=new_pic12,borderwidth=0,border=0,bg="#000000")
                Dorritos_img.place(x=323,y=335)
                Dorritos_btn = Button(main, image=new_pic12,command=Dorritos,border=0,borderwidth=0,bg="#000000")
                Dorritos_btn.place(x=323,y=335)
                my_Dorritos = Label(main,image="",bg="#000000")
                my_Dorritos.place(x=450,y=630)

                def Lays():
                    my_Lays.config(image=new_pic13,bg="#000000",border=0,borderwidth=0)
                image13 = Image.open("Lays.png")
                resized = image13.resize((120,85), Image.Resampling.LANCZOS)
                new_pic13 = ImageTk.PhotoImage(resized)
                Lays_img = Label(main, image=new_pic13,borderwidth=0,border=0,bg="#000000")
                Lays_img.place(x=410,y=335)
                Lays_btn = Button(main, image=new_pic13,command=Lays,border=0,borderwidth=0,bg="#000000")
                Lays_btn.place(x=410,y=335)
                my_Lays = Label(main,image="",bg="#000000")
                my_Lays.place(x=450,y=630)

                def Local_Chips():
                    my_Local_Chips.config(image=new_pic14,bg="#000000",border=0,borderwidth=0)
                image14 = Image.open("Local Chips.png")
                resized = image14.resize((80,100), Image.Resampling.LANCZOS)
                new_pic14 = ImageTk.PhotoImage(resized)
                Local_Chips_img = Label(main, image=new_pic14,borderwidth=0,border=0,bg="#000000")
                Local_Chips_img.place(x=535,y=331)
                Local_Chips_btn = Button(main, image=new_pic14,command=Local_Chips,border=0,borderwidth=0,bg="#000000")
                Local_Chips_btn.place(x=535,y=331)
                my_Local_Chips = Label(main,image="",bg="#000000")
                my_Local_Chips.place(x=450,y=630)

                def Uncle_Chips():
                    my_Uncle_Chips.config(image=new_pic15,bg="#000000",border=0,borderwidth=0)
                image15 = Image.open("Uncle Chips.png")
                resized = image15.resize((80,85), Image.Resampling.LANCZOS)
                new_pic15 = ImageTk.PhotoImage(resized)
                Uncle_Chips_img = Label(main, image=new_pic15,borderwidth=0,border=0,bg="#000000")
                Uncle_Chips_img.place(x=635,y=335)
                Uncle_Chips_btn = Button(main, image=new_pic15,command=Uncle_Chips,border=0,borderwidth=0,bg="#000000")
                Uncle_Chips_btn.place(x=635,y=335)
                my_Uncle_Chips = Label(main,image="",bg="#000000")
                my_Uncle_Chips.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic17,bg="#000000",border=0,borderwidth=0)
                image17 = Image.open("public/Coke.png")
                resized = image17.resize((60,85), Image.Resampling.LANCZOS)
                new_pic17 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic17,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=335,y=460)
                coke_btn = Button(main, image=new_pic17,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=335,y=460)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic18,bg="#000000",border=0,borderwidth=0)
                image18 = Image.open("public/Coke.png")
                resized = image3.resize((60,85), Image.Resampling.LANCZOS)
                new_pic18 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic18,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=435,y=458)
                coke_btn = Button(main, image=new_pic18,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=435,y=458)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic19,bg="#000000",border=0,borderwidth=0)
                image19 = Image.open("public/Coke.png")
                resized = image19.resize((60,85), Image.Resampling.LANCZOS)
                new_pic19 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic19,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=537,y=458)
                coke_btn = Button(main, image=new_pic19,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=537,y=458)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)

                def coke():
                    my_coke.config(image=new_pic20,bg="#000000",border=0,borderwidth=0)
                image20 = Image.open("public/Coke.png")
                resized = image5.resize((60,85), Image.Resampling.LANCZOS)
                new_pic20 = ImageTk.PhotoImage(resized)
                coke_img = Label(main, image=new_pic20,borderwidth=0,border=0,bg="#000000")
                coke_img.place(x=635,y=458)
                coke_btn = Button(main, image=new_pic20,command=coke,border=0,borderwidth=0,bg="#000000")
                coke_btn.place(x=635,y=458)
                my_coke = Label(main,image="",bg="#000000")
                my_coke.place(x=450,y=630)
                
                drinks = Label(main, text="Drinks",bg="#000000",fg="white")
                drinks.place(x=210,y=180)

                coke = Label(main,text="Coke",bg="#000000",fg="white")
                coke.place(x=350,y=180)

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

                rafello = Label(main,text="Rafello",bg="#000000",fg="white")
                rafello.place(x=550,y=540)

                mars = Label(main,text="Mars",bg="#000000",fg="white")
                mars.place(x=650,y=540)

                
            frame = Frame(main, width=400,height=400,bg="black",)
            frame.place(x=1100, y=30)
            button = Button(frame, text= "Logout",border=4,bg="#00FF7F",pady=2,command=login)
            button.place(x=165, y=180)
            button = Button(frame, text= "Buy Again",border=4,bg="#00FF7F",pady=2,command=cancel)
            button.place(x=155, y=250)
                


    frame = Frame(main, width=400,height=400,bg="black",)
    frame.place(x=1100, y=30)
    Label(frame,text="Sign in",font=("Arial",30,"bold"),fg="white",bg="#000000").place(x=130,y=15)
    
    username = Entry(frame, width=40)
    username.place(x=80, y=80, height=30)
    username.insert(0,"   Username")
    username.bind("<Button-1>",use)

    password = Entry(frame, width=40,show="*")
    password.place(x=80, y=130, height=30)
    password.insert(0,"*******@")
    password.bind("<Button-1>",pas)
    Frame(main, width=100,height=100,bg="#000000").place(x=447,y=630)

    button = Button(frame, text= "Sign In",border=4,bg="#00FF7F",pady=2,command=top)
    button.place(x=165, y=180)

    Label(frame, text="Don't have an account?",fg="white",bg="#000000").place(x=100, y=230)
    Button(frame, text="Sign up!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_up).place(x=230, y=230)
    
def sign_up():
    register.register(state)
