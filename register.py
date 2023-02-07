from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import login
import auth

def register(main):
    global reg_state
    reg_state = main 

     
    def use(usee):
        username.config(state=NORMAL)
        username.delete(0, END)
    def pas(passs):
        password.config(state=NORMAL)
        password.delete(0, END)
        
    def emai(emaii):
        email.config(state=NORMAL)
        email.delete(0, END)
        
    def getRegistered():
        
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
            auth.create_user(username.get(), email.get(), password.get())
            frame = Frame(main, width=400,height=400,bg="black",)
            frame.place(x=1100, y=30)
            Label(frame,text="Registration Successfull",font=("Arial",15,"bold"),fg="green",bg="#000000").place(x=130,y=50)
            button = Button(frame, text= "Login",border=4,bg="#00FF7F",pady=2,command=login)
            button.place(x=230, y=85)
            

    frame = Frame(main, width=400,height=310,bg="#000000",)
    frame.place(x=880, y=15)
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

    button = Button(frame, text= "Sign up",border=4,bg="#00FF7F",pady=2,command=getRegistered,activebackground="#000000",activeforeground="#FFFFFF")
    button.place(x=165, y=225)

    already = LabelFrame(frame,width=300,height=40,bg="#000000")
    already.place(x=50, y=265)
    Label(already, text="Already have an account?",fg="white",bg="#000000").place(x=40, y=6)
    Button(already, text="Sign in!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_in,activebackground="#000000",activeforeground="#FFFFFF").place(x=180, y=6)

def sign_in():
    login.login(reg_state)
