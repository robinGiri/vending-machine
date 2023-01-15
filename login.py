from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import register

def login(main, vendingState):

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
            
            vendingState["is_authenticated"] = "true"     
            
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

    button = Button(frame, text= "Sign In",border=4,bg="#00FF7F",pady=2,command=getSignIn)
    button.place(x=165, y=180)

    Label(frame, text="Don't have an account?",fg="white",bg="#000000").place(x=100, y=230)
    Button(frame, text="Sign up!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_up).place(x=230, y=230)
    
def sign_up():
    register.register(state)
