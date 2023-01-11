from tkinter import *
import seed
import product
import sqlite3 
from tkinter import messagebox

main = Tk()
main.state("zoomed")
main.config(bg="#000000")

# this will add title
main.title("Vending Machine")

# this will create a label widget
space1 = Label(main,padx=50,pady=20,bg="#000000").grid(row=0,column=0)
space2 = Label(main,padx=50,pady=5,bg="#000000").grid(row=1,column=1)

# create products table
product.create_productTable()

def register():

    def drink():
        a = Label(main,text="Values"+str(var.get()))
        a.pack(anchor=S)
    
    def biscus():
        b = Label(main,text="Values"+str(vari.get()))
        b.pack(anchor=S)

    def chi():
        c = Label(main,text="Values"+str(varia.get()))
        c.pack(anchor=S)
        
    def choco():
        d = Label(main,text="Values"+str(variab.get()))
        d.pack(anchor=S)  
       
              
    var = IntVar()
    drinks_img = Label(main, padx=40,pady=30)
    drinks_img.grid(row=2,column=2)
    drinks = Label(main, text="Drinks",bg="#000000",fg="white")
    drinks.grid(row=3,column=2)
    coke_img = Label(main, padx=40,pady=30)
    coke_img.grid(row=2,column=3)
    coke = Label(main,text="Coke",bg="#000000",fg="white")
    coke.grid(row=3,column=3)
    coke_click = Radiobutton(main,variable=var,value=1,command=drink,bg="#000000",fg="blue",state=DISABLED)
    coke_click.grid(row=4,column=3)
    fanta_img = Label(main, padx=40,pady=30)
    fanta_img.grid(row=2,column=4)
    fanta = Label(main,text="Fanta",bg="#000000",fg="white")
    fanta.grid(row=3,column=4)
    fanta_click = Radiobutton(main,variable=var,value=2,command=drink,bg="#000000",fg="blue",state=DISABLED)
    fanta_click.grid(row=4,column=4)
    sprite_img = Label(main, padx=40,pady=30)
    sprite_img.grid(row=2,column=5)
    sprite = Label(main,text="Sprite",bg="#000000",fg="white")
    sprite.grid(row=3,column=5)
    sprite_click = Radiobutton(main,variable=var,value=3,command=drink,bg="#000000",fg="blue",state=DISABLED)
    sprite_click.grid(row=4,column=5)
    slice_img = Label(main, padx=40,pady=30)
    slice_img.grid(row=2,column=6)
    slice = Label(main,text="Slice",bg="#000000",fg="white")
    slice.grid(row=3,column=6)
    slice_click = Radiobutton(main,variable=var,value=4,command=drink,bg="#000000",fg="blue",state=DISABLED)
    slice_click.grid(row=4,column=6)


    vari = IntVar()
    biscuits_img = Label(main, padx=40,pady=30)
    biscuits_img.grid(row=5,column=2)
    biscuits = Label(main, text="Biscuits",bg="#000000",fg="white")
    biscuits.grid(row=6,column=2)
    bonbon_img = Label(main, padx=40,pady=30)
    bonbon_img.grid(row=5,column=3)
    bonbon = Label(main,text="Bonbon",bg="#000000",fg="white")
    bonbon.grid(row=6,column=3)
    bonbon_click = Radiobutton(main,variable=vari,value=5,command=biscus,bg="#000000",fg="blue",state=DISABLED)
    bonbon_click.grid(row=7,column=3)
    oreo_img = Label(main, padx=40,pady=30)
    oreo_img.grid(row=5,column=4)
    oreo = Label(main,text="Oreo",bg="#000000",fg="white")
    oreo.grid(row=6,column=4)
    oreo_click = Radiobutton(main,variable=vari,value=6,command=biscus,bg="#000000",fg="blue",state=DISABLED)
    oreo_click.grid(row=7,column=4)
    digestive_img = Label(main, padx=40,pady=30)
    digestive_img.grid(row=5,column=5)
    digestive = Label(main,text="Digestive",bg="#000000",fg="white")
    digestive.grid(row=6,column=5)
    digestive_click = Radiobutton(main,variable=vari,value=7,command=biscus,bg="#000000",fg="blue",state=DISABLED)
    digestive_click.grid(row=7,column=5)
    hide_and_sick_img = Label(main, padx=40,pady=30)
    hide_and_sick_img.grid(row=5,column=6)
    hide_and_sick = Label(main,text="Hide_and_Sick",bg="#000000",fg="white")
    hide_and_sick.grid(row=6,column=6)
    hide_and_sick_click = Radiobutton(main,variable=vari,value=8,command=biscus,bg="#000000",fg="blue",state=DISABLED)
    hide_and_sick_click.grid(row=7,column=6)


    varia = IntVar()
    chips_img = Label(main, padx=40,pady=30)
    chips_img.grid(row=8,column=2)
    chips = Label(main, text="Chips",bg="#000000",fg="white")
    chips.grid(row=9,column=2)
    dorritos_img = Label(main, padx=40,pady=30)
    dorritos_img.grid(row=8,column=3)
    dorritos = Label(main,text="Dorritos",bg="#000000",fg="white")
    dorritos.grid(row=9,column=3)
    dorritos_click = Radiobutton(main,variable=varia,value=9,command=chi,bg="#000000",fg="blue",state=DISABLED)
    dorritos_click.grid(row=10,column=3)
    lays_img = Label(main, padx=40,pady=30)
    lays_img.grid(row=8,column=4)
    lays = Label(main,text="Lays",bg="#000000",fg="white")
    lays.grid(row=9,column=4)
    lays_click = Radiobutton(main,variable=varia,value=10,command=chi,bg="#000000",fg="blue",state=DISABLED)
    lays_click.grid(row=10,column=4)
    local_chips_img = Label(main, padx=40,pady=30)
    local_chips_img.grid(row=8,column=5)
    local_chips = Label(main,text="Local_Chips",bg="#000000",fg="white")
    local_chips.grid(row=9,column=5)
    local_chips_click = Radiobutton(main,variable=varia,value=11,command=chi,bg="#000000",fg="blue",state=DISABLED)
    local_chips_click.grid(row=10,column=5)
    uncle_chips_img = Label(main, padx=40,pady=30)
    uncle_chips_img.grid(row=8,column=6)
    uncle_chips = Label(main,text="Uncle_Chips",bg="#000000",fg="white")
    uncle_chips.grid(row=9,column=6)
    uncle_chips_click = Radiobutton(main,variable=varia,value=12,command=chi,bg="#000000",fg="blue",state=DISABLED)
    uncle_chips_click.grid(row=10,column=6)



    variab = IntVar()
    chocolates_img = Label(main, padx=50,pady=30,bg="red")
    chocolates_img.grid(row=11,column=2)
    chocolates = Label(main, text="Chocolates",bg="#000000",fg="white")
    chocolates.grid(row=12,column=2)
    snickers_img = Label(main, padx=50,pady=30,bg="blue",state=DISABLED)
    snickers_img.grid(row=11,column=3)
    snickers = Label(main,text="Snickers",bg="#000000",fg="white")
    snickers.grid(row=12,column=3)
    snickers_click = Radiobutton(main,variable=variab,value=13,command=choco,bg="#000000",fg="blue",state=DISABLED)
    snickers_click.grid(row=13,column=3)
    twix_img = Label(main, padx=50,pady=30,bg="green")
    twix_img.grid(row=11,column=4)
    twix = Label(main,text="Twix",bg="#000000",fg="white")
    twix.grid(row=12,column=4)
    twix_click = Radiobutton(main,variable=variab,value=14,command=choco,bg="#000000",fg="blue",state=DISABLED)
    twix_click.grid(row=13,column=4)
    rafello_img = Label(main, padx=50,pady=30,bg="yellow")
    rafello_img.grid(row=11,column=5)
    rafello = Label(main,text="Rafello",bg="#000000",fg="white")
    rafello.grid(row=12,column=5)
    rafello_click = Radiobutton(main,variable=variab,value=15,command=choco,bg="#000000",fg="blue",state=DISABLED)
    rafello_click.grid(row=13,column=5)
    mars_img = Label(main, padx=50,pady=30,bg="purple")
    mars_img.grid(row=11,column=6)
    mars = Label(main,text="Mars",bg="#000000",fg="white")
    mars.grid(row=12,column=6)
    mars_click = Radiobutton(main,variable=variab,value=16,command=choco,bg="#000000",fg="blue",state=DISABLED)
    mars_click.grid(row=13,column=6)


    space3 = Label(main,padx=80,pady=5,bg="#000000")
    space3.grid(row=0,column=7)
    space4 = Label(main,padx=80,pady=5,bg="#000000")
    space4.grid(row=0,column=8)
    space5 = Label(main,padx=80,pady=5,bg="#000000")
    space5.grid(row=0,column=9)

    def ema(emaa):
        email.config(state=NORMAL)
        email.delete(0, END)
    def use(useee):
        username.config(state=NORMAL)
        username.delete(0, END)
    def pas(passs):
        password.config(state=NORMAL)
        password.delete(0, END)
      
    sign = Label(main, text="Become a member",font=("Arail",30,"bold"),fg="white",bg="black")
    sign.place(x=1120,y=10)
    email = Entry(main,bg="#202020",borderwidth=0,fg="white")
    email.place(x=1170,y=70,height=40,width=250)
    email.insert(0,"   Email")
    email.bind("<Button-1>",ema)
    username = Entry(main,bg="#202020",borderwidth=0,fg="white")
    username.place(x=1170,y=130,height=40,width=250)
    username.insert(0,"   Username")
    username.bind("<Button-1>",use)
    password = Entry(main,bg="#202020",borderwidth=0,fg="white",show="*")
    password.place(x=1170,y=190,height=40,width=250)
    password.insert(0,"   Password")
    password.bind("<Button-1>",pas)
    

    
    up = LabelFrame(main,bg="black",pady=15,borderwidth=0)
    up.place(x=1155,y=235)
    signip = Label(up, text= "Already have an account?",fg="white",bg="#202020",font=("Arial",10),borderwidth=0,justify="left").grid(padx=70,pady=37)
    btn = Button(up, text="Sign In!",fg="#00FF7F",bg="#202020",borderwidth=0).place(x=225,y=35)
    btn2 = Label(up, text="-------->",fg="#00FF7F",bg="#202020",borderwidth=0).place(x=13,y=37)
    signup = Button(up,text="Sign up",bg="#00FF7F")
    signup.place(x=120,y=2)
    
    
    purchase = Button(main,text="Purchase",border=3,bg="#00FF7F",state=DISABLED)
    purchase.grid(row=14,column=4,pady=30)
    
    spin_coke = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_coke.place(x=380,y=190)
    spin_fanta = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_fanta.place(x=485,y=190)
    spin_sprite = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_sprite.place(x=590,y=190)
    spin_slice = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_slice.place(x=693,y=190)
    
    spin_bourborn = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_bourborn.place(x=375,y=315)
    spin_oreo = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_oreo.place(x=480,y=315)
    spin_dugestive = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_dugestive.place(x=585,y=315)
    spin_hide_and_sick = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_hide_and_sick.place(x=687,y=315)
    
    spin_dorritos = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_dorritos.place(x=375,y=440)
    spin_lays = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_lays.place(x=480,y=440)
    spin_local_chips = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_local_chips.place(x=585,y=440)
    spin_uncle_chips = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_uncle_chips.place(x=687,y=440)
    
    spin_snickers = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_snickers.place(x=375,y=565)
    spin_twix = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_twix.place(x=480,y=565)
    spin_rafello = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_rafello.place(x=585,y=565)
    spin_mars = Spinbox(main,from_=1,to=5,width=2,state=DISABLED)
    spin_mars.place(x=687,y=565)



def login():
    
    def drink():
        a = Label(main,text="Values"+str(var.get()))
        a.pack(anchor=S)
    
    def biscus():
        b = Label(main,text="Values"+str(vari.get()))
        b.pack(anchor=S)

    def chi():
        c = Label(main,text="Values"+str(varia.get()))
        c.pack(anchor=S)
        
    def choco():
        d = Label(main,text="Values"+str(variab.get()))
        d.pack(anchor=S) 


              
    var = IntVar()
    drinks_img = Label(main, padx=40,pady=30)
    drinks_img.grid(row=2,column=2)
    drinks = Label(main, text="Drinks",bg="#000000",fg="white")
    drinks.grid(row=3,column=2)
    coke_img = Label(main, padx=40,pady=30)
    coke_img.grid(row=2,column=3)
    coke = Label(main,text="Coke",bg="#000000",fg="white")
    coke.grid(row=3,column=3)
    coke_click = Radiobutton(main,variable=var,value=1,command=drink,bg="#000000",fg="blue")
    coke_click.grid(row=4,column=3)
    fanta_img = Label(main, padx=40,pady=30)
    fanta_img.grid(row=2,column=4)
    fanta = Label(main,text="Fanta",bg="#000000",fg="white")
    fanta.grid(row=3,column=4)
    fanta_click = Radiobutton(main,variable=var,value=2,command=drink,bg="#000000",fg="blue")
    fanta_click.grid(row=4,column=4)
    sprite_img = Label(main, padx=40,pady=30)
    sprite_img.grid(row=2,column=5)
    sprite = Label(main,text="Sprite",bg="#000000",fg="white")
    sprite.grid(row=3,column=5)
    sprite_click = Radiobutton(main,variable=var,value=3,command=drink,bg="#000000",fg="blue")
    sprite_click.grid(row=4,column=5)
    slice_img = Label(main, padx=40,pady=30)
    slice_img.grid(row=2,column=6)
    slice = Label(main,text="Slice",bg="#000000",fg="white")
    slice.grid(row=3,column=6)
    slice_click = Radiobutton(main,variable=var,value=4,command=drink,bg="#000000",fg="blue")
    slice_click.grid(row=4,column=6)


    vari = IntVar()
    biscuits_img = Label(main, padx=40,pady=30)
    biscuits_img.grid(row=5,column=2)
    biscuits = Label(main, text="Biscuits",bg="#000000",fg="white")
    biscuits.grid(row=6,column=2)
    bonbon_img = Label(main, padx=40,pady=30)
    bonbon_img.grid(row=5,column=3)
    bonbon = Label(main,text="Bonbon",bg="#000000",fg="white")
    bonbon.grid(row=6,column=3)
    bonbon_click = Radiobutton(main,variable=vari,value=5,command=biscus,bg="#000000",fg="blue")
    bonbon_click.grid(row=7,column=3)
    oreo_img = Label(main, padx=40,pady=30)
    oreo_img.grid(row=5,column=4)
    oreo = Label(main,text="Oreo",bg="#000000",fg="white")
    oreo.grid(row=6,column=4)
    oreo_click = Radiobutton(main,variable=vari,value=6,command=biscus,bg="#000000",fg="blue")
    oreo_click.grid(row=7,column=4)
    digestive_img = Label(main, padx=40,pady=30)
    digestive_img.grid(row=5,column=5)
    digestive = Label(main,text="Digestive",bg="#000000",fg="white")
    digestive.grid(row=6,column=5)
    digestive_click = Radiobutton(main,variable=vari,value=7,command=biscus,bg="#000000",fg="blue")
    digestive_click.grid(row=7,column=5)
    hide_and_sick_img = Label(main, padx=40,pady=30)
    hide_and_sick_img.grid(row=5,column=6)
    hide_and_sick = Label(main,text="Hide and Sick",bg="#000000",fg="white")
    hide_and_sick.grid(row=6,column=6)
    hide_and_sick_click = Radiobutton(main,variable=vari,value=8,command=biscus,bg="#000000",fg="blue")
    hide_and_sick_click.grid(row=7,column=6)


    varia = IntVar()
    chips_img = Label(main, padx=40,pady=30)
    chips_img.grid(row=8,column=2)
    chips = Label(main, text="Chips",bg="#000000",fg="white")
    chips.grid(row=9,column=2)
    dorritos_img = Label(main, padx=40,pady=30)
    dorritos_img.grid(row=8,column=3)
    dorritos = Label(main,text="Dorritos",bg="#000000",fg="white")
    dorritos.grid(row=9,column=3)
    dorritos_click = Radiobutton(main,variable=varia,value=9,command=chi,bg="#000000",fg="blue")
    dorritos_click.grid(row=10,column=3)
    lays_img = Label(main, padx=40,pady=30)
    lays_img.grid(row=8,column=4)
    lays = Label(main,text="Lays",bg="#000000",fg="white")
    lays.grid(row=9,column=4)
    lays_click = Radiobutton(main,variable=varia,value=10,command=chi,bg="#000000",fg="blue")
    lays_click.grid(row=10,column=4)
    local_chips_img = Label(main, padx=40,pady=30)
    local_chips_img.grid(row=8,column=5)
    local_chips = Label(main,text="Local Chips",bg="#000000",fg="white")
    local_chips.grid(row=9,column=5)
    local_chips_click = Radiobutton(main,variable=varia,value=11,command=chi,bg="#000000",fg="blue")
    local_chips_click.grid(row=10,column=5)
    uncle_chips_img = Label(main, padx=40,pady=30)
    uncle_chips_img.grid(row=8,column=6)
    uncle_chips = Label(main,text="Uncle Chips",bg="#000000",fg="white")
    uncle_chips.grid(row=9,column=6)
    uncle_chips_click = Radiobutton(main,variable=varia,value=12,command=chi,bg="#000000",fg="blue")
    uncle_chips_click.grid(row=10,column=6)



    variab = IntVar()
    chocolates_img = Label(main, padx=50,pady=30,bg="red")
    chocolates_img.grid(row=11,column=2)
    chocolates = Label(main, text="Chocolates",bg="#000000",fg="white")
    chocolates.grid(row=12,column=2)
    snickers_img = Label(main, padx=50,pady=30,bg="blue")
    snickers_img.grid(row=11,column=3)
    snickers = Label(main,text="Snickers",bg="#000000",fg="white")
    snickers.grid(row=12,column=3)
    snickers_click = Radiobutton(main,variable=variab,value=13,command=choco,bg="#000000",fg="blue")
    snickers_click.grid(row=13,column=3)
    twix_img = Label(main, padx=50,pady=30,bg="green")
    twix_img.grid(row=11,column=4)
    twix = Label(main,text="Twix",bg="#000000",fg="white")
    twix.grid(row=12,column=4)
    twix_click = Radiobutton(main,variable=variab,value=14,command=choco,bg="#000000",fg="blue")
    twix_click.grid(row=13,column=4)
    rafello_img = Label(main, padx=50,pady=30,bg="yellow")
    rafello_img.grid(row=11,column=5)
    rafello = Label(main,text="Rafello",bg="#000000",fg="white")
    rafello.grid(row=12,column=5)
    rafello_click = Radiobutton(main,variable=variab,value=15,command=choco,bg="#000000",fg="blue")
    rafello_click.grid(row=13,column=5)
    mars_img = Label(main, padx=50,pady=30,bg="purple")
    mars_img.grid(row=11,column=6)
    mars = Label(main,text="Mars",bg="#000000",fg="white")
    mars.grid(row=12,column=6)
    mars_click = Radiobutton(main,variable=variab,value=16,command=choco,bg="#000000",fg="blue")
    mars_click.grid(row=13,column=6)


    space3 = Label(main,padx=80,pady=5,bg="#000000")
    space3.grid(row=0,column=7)
    space4 = Label(main,padx=80,pady=5,bg="#000000")
    space4.grid(row=0,column=8)
    space5 = Label(main,padx=80,pady=5,bg="#000000")
    space5.grid(row=0,column=9)

    def use(usee):
        username.config(state=NORMAL)
        username.delete(0, END)
    def pas(passs):
        password.config(state=NORMAL)
        password.delete(0, END)
      
    def top():
        if username.get() == "":
            messagebox.showerror("error", "All Fields Required")
        elif password.get() == "":
            messagebox.showerror("error", "All Fields Required")
        elif len(password.get()) <8:
            messagebox.showerror("error", "Password Must Be Of 8 Or More Character")
        

        
    sign = Label(main, text="Sign In",font=("Arail",30,"bold"),fg="white",bg="black")
    sign.place(x=1220,y=10)
    username = Entry(main,bg="#202020",borderwidth=0,fg="white")
    username.place(x=1170,y=70,height=40,width=250)
    username.insert(0,"   Username")
    username.bind("<Button-1>",use)
    password = Entry(main,bg="#202020",borderwidth=0,fg="white",show="*")
    password.place(x=1170,y=130,height=40,width=250)
    password.insert(0,"password")
    password.bind("<Button-1>",pas)

    button = Button(main, text= "Sign In",border=4,bg="#00FF7F",command=top)
    button.place(x=1270,y=190)
    
    up = LabelFrame(main,bg="#202020")
    up.place(x=1170,y=235)
    signip = Label(up, text= "Don't have an account?",fg="white",bg="#202020",font=("Arial",10),borderwidth=0,justify="left").grid(padx=60,pady=5)
    btn = Button(up, text="Sign Up!",fg="#00FF7F",bg="#202020",borderwidth=0,command=register).place(x=200,y=3)
    btn2 = Label(up, text="------>",fg="#00FF7F",bg="#202020",borderwidth=0).place(x=10,y=3)
    
    


    def pur():
        
        bought.config(text=spin_coke.get())

    spin_coke = Spinbox(main,from_=1,to=5,width=2)
    spin_coke.place(x=380,y=190)
    spin_fanta = Spinbox(main,from_=1,to=5,width=2)
    spin_fanta.place(x=485,y=190)
    spin_sprite = Spinbox(main,from_=1,to=5,width=2)
    spin_sprite.place(x=590,y=190)
    spin_slice = Spinbox(main,from_=1,to=5,width=2)
    spin_slice.place(x=693,y=190)

    spin_bourborn = Spinbox(main,from_=1,to=5,width=2)
    spin_bourborn.place(x=375,y=315)
    spin_oreo = Spinbox(main,from_=1,to=5,width=2)
    spin_oreo.place(x=480,y=315)
    spin_digestive = Spinbox(main,from_=1,to=5,width=2)
    spin_digestive.place(x=585,y=315)
    spin_hide_and_sick = Spinbox(main,from_=1,to=5,width=2)
    spin_hide_and_sick.place(x=687,y=315)

    spin_dorritos = Spinbox(main,from_=1,to=5,width=2)
    spin_dorritos.place(x=375,y=440)
    spin_lays = Spinbox(main,from_=1,to=5,width=2)
    spin_lays.place(x=480,y=440)
    spin_local_chips = Spinbox(main,from_=1,to=5,width=2)
    spin_local_chips.place(x=585,y=440)
    spin_uncle_chips = Spinbox(main,from_=1,to=5,width=2)
    spin_uncle_chips.place(x=687,y=440)

    spin_snickers = Spinbox(main,from_=1,to=5,width=2)
    spin_snickers.place(x=375,y=565)
    spin_twix = Spinbox(main,from_=1,to=5,width=2)
    spin_twix.place(x=480,y=565)
    spin_rafello = Spinbox(main,from_=1,to=5,width=2)
    spin_rafello.place(x=585,y=565)
    spin_mars = Spinbox(main,from_=1,to=5,width=2)
    spin_mars.place(x=687,y=565)



    purchase = Button(main,text="Purchase",border=3,bg="#00FF7F",command=pur)
    purchase.grid(row=14,column=4,pady=30)

    bought = Label(main,text="",bg="#000000",fg="white")
    bought.grid(row=15,column=4)
    
login()

main.mainloop()

