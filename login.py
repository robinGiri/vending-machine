from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import register
import auth
import adminMain

def login(main, vendingState):
    def go_to_admin():
        if vendingState["is_admin"]:
            adminMain.newpage(main)
        else:
            messagebox.showerror("error", "Please Login As Admin User")


    def sign_up():
        register.register(main, vendingState)

    def use(usee):
        username.config(state=NORMAL)
        username.delete(0, END)

    def pas(passs):
        password.config(state=NORMAL)
        password.delete(0, END)
        
    def get_sign_in():
        if username.get() == "" or password.get() == "":
            messagebox.showerror("error", "Username OR Password Should Not Be Empty")
            return

        isLogin, isAdmin = auth.isLogin(username.get(), password.get())
        if isLogin == None:
            messagebox.showerror("error", "User Name OR Password is wrong")
            return
        else:
            vendingState["is_authenticated"] = True
            vendingState["is_admin"] = isAdmin 
            frame = Frame(main, width=600,height=285,bg="#000000")
            frame.place(x=765, y=40)
            button = Button(frame, text= "Logout",border=4,bg="#00FF7F",pady=2,command=login,activebackground="#000000",activeforeground="#FFFFFF")
            button.place(x=530, y=250)
            button = Button(frame, text= "Go To Admin",border=4,bg="#00FF7F",pady=2,command=go_to_admin,activebackground="#000000",activeforeground="#FFFFFF")
            button.place(x=430, y=250)
    frame = Frame(main, width=600,height=285,bg="#000000")
    frame.place(x=765, y=40)
    Label(frame,text="Sign in",font=("Arial",30,"bold"),fg="white",bg="#000000").place(x=230,y=15)
    
    username = Entry(frame, width=40)
    username.place(x=180, y=80, height=30)
    username.insert(0,"   Username")
    username.bind("<Button-1>",use)

    password = Entry(frame, width=40,show="*")
    password.place(x=180, y=130, height=30)
    password.insert(0,"*******@")
    password.bind("<Button-1>",pas)

    button = Button(frame, text= "Sign In",border=4,bg="#00FF7F",pady=2,command=get_sign_in,activebackground="#000000",activeforeground="#FFFFFF")
    button.place(x=265, y=180)
    
    donot = LabelFrame(frame,width=300,height=40,bg="#000000")
    donot.place(x=155,y=230)
    Label(donot, text="Don't have an account?",fg="white",bg="#000000").place(x=40, y=6)
    Button(donot, text="Sign up!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_up,activebackground="#000000",activeforeground="#FFFFFF").place(x=180, y=6)

