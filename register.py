from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import login

def register(main):
    global reg_state
    reg_state = main    

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
    Local_Chips_img.place(x=535,y=324)
    Local_Chips_btn = Button(main, image=new_pic14,command=Local_Chips,border=0,borderwidth=0,bg="#000000",state=DISABLED)
    Local_Chips_btn.place(x=535,y=324)
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
    
    Frame(main, width=100,height=100,bg="#000000").place(x=447,y=630)
     
    def use(usee):
        username.config(state=NORMAL)
        username.delete(0, END)
    def pas(passs):
        password.config(state=NORMAL)
        password.delete(0, END)
        
    def emai(emaii):
        email.config(state=NORMAL)
        email.delete(0, END)
        
    def top():
        
        if username.get() == "":
            messagebox.showerror("error", "Username Should Not Be Empty")      
      
        elif password.get() == "":
            messagebox.showerror("error", "Password Should Not Be Empty")
            
        elif email.get() == "":
            messagebox.showerror("error", "Email Should Not Be Empty")
            
        elif "@gmail.com" not in email.get():
            messagebox.showerror("error","Email Must Have Ending With @gmail.com")
            
        elif "@" not in password.get():
            messagebox.showerror("error","Password Must Contain @")
            
        elif len(password.get()) <8:
            messagebox.showerror("error", "Password Must Be Of 8 Or More Character")
            
        elif  "   Username" in username.get():
            messagebox.showerror("error", "Choose Username")

        elif "email@gmail.com" in email.get() :
            messagebox.showerror("error", "Choose Email")            
            
        elif "*******@" in password.get():
            messagebox.showerror("error", "Choose Password")
            

            
        else:
            frame = Frame(main, width=400,height=400,bg="black",)
            frame.place(x=1100, y=30)
            Label(frame,text="Registration Successfull",font=("Arial",15,"bold"),fg="green",bg="#000000").place(x=130,y=50)
            button = Button(frame, text= "Login",border=4,bg="#00FF7F",pady=2,command=login)
            button.place(x=230, y=85)
            

    frame = Frame(main, width=400,height=400,bg="black",)
    frame.place(x=1100, y=30)
    Label(frame,text="Become a member",font=("Arial",25,"bold"),fg="white",bg="#000000").place(x=60,y=15)

    username = Entry(frame, width=40)
    username.place(x=80, y=80, height=30)
    username.insert(0,"   Username")
    username.bind("<Button-1>",use)

    email = Entry(frame, width=40)
    email.place(x=80, y=130, height=30)
    email.insert(0,"   email@gmail.com")
    email.bind("<Button-1>",emai)

    password = Entry(frame, width=40,show="*")
    password.place(x=80, y=180, height=30)
    password.insert(0,"*******@")
    password.bind("<Button-1>",pas)

    button = Button(frame, text= "Sign up",border=4,bg="#00FF7F",pady=2,command=top)
    button.place(x=165, y=230)

    Label(frame, text="Already have an account?",fg="white",bg="#000000").place(x=100, y=280)
    Button(frame, text="Sign in!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_in).place(x=240, y=280)

def sign_in():
    login.login(reg_state)
