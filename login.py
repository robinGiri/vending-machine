from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import register
import auth

def login(main):

    global state
    state = main
    
    def use(usee):
        username.config(state=NORMAL)
        username.delete(0, END)
    def pas(passs):
        password.config(state=NORMAL)
        password.delete(0, END)
        
    def getSignIn():

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
            isLogin = auth.isLogin(username.get(), password.get())
            print(isLogin)
            frame = Frame(main, width=400,height=310,bg="#000000")
            frame.place(x=880, y=15)
            button = Button(frame, text= "Logout",border=4,bg="#00FF7F",pady=2,command=login,activebackground="#000000",activeforeground="#FFFFFF")
            button.place(x=165, y=100)
            

                


    frame = Frame(main, width=400,height=310,bg="#000000")
    frame.place(x=880, y=15)
    Label(frame,text="Sign in",font=("Arial",30,"bold"),fg="white",bg="#000000").place(x=130,y=15)
    
    username = Entry(frame, width=40)
    username.place(x=80, y=80, height=30)
    username.insert(0,"   Username")
    username.bind("<Button-1>",use)

    password = Entry(frame, width=40,show="*")
    password.place(x=80, y=130, height=30)
    password.insert(0,"*******@")
    password.bind("<Button-1>",pas)

    button = Button(frame, text= "Sign In",border=4,bg="#00FF7F",pady=2,command=getSignIn,activebackground="#000000",activeforeground="#FFFFFF")
    button.place(x=165, y=180)
    
    donot = LabelFrame(frame,width=300,height=40,bg="#000000")
    donot.place(x=55,y=230)
    Label(donot, text="Don't have an account?",fg="white",bg="#000000").place(x=40, y=6)
    Button(donot, text="Sign up!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_up,activebackground="#000000",activeforeground="#FFFFFF").place(x=170, y=6)
    
def sign_up():
    register.register(state)
