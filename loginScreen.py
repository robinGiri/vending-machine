from tkinter import *
from tkinter import messagebox
import registerScreen
import auth
import adminScreen

def login(main, vendingState):

    # admin age
    def go_to_admin():
        '''
        params: no params
        check weather you are admin or not
        if admin opens new window and let you use admin pannel
        if not admin pops error
        '''

        if vendingState["is_admin"]:
            adminScreen.newWindow(main)
        else:
            messagebox.showerror("error", "Please Login As Admin User")
    # sign up page
    def sign_up():
        '''
        params: no params
        redirects to register UI
        '''
        registerScreen.register(main, vendingState)
    
    # log out of vending machine 
    def log_out():
        '''
        params: no params
        removes auth from vending machine
        '''
        vendingState["is_authenticated"] = False
        vendingState["is_admin"] = False

    # configure username input
    def username_input(user):
        username.config(state=NORMAL)
        username.delete(0, END)

    # configure password input
    def password_imput(secret):
        password.config(state=NORMAL)
        password.delete(0, END)

    def get_sign_in():
        '''
        params: no params
        checks username and passowrd exist in users table
        checks user is admin or not
        vendingState["is_authenticated"] = True if uses in table
        vendingState["is_admin"] = True if user is admin
        error if uses dosen't exists
        '''
        
        # check if username and password are empty
        if username.get() == "" or password.get() == "":
            messagebox.showerror("error", "Username OR Password Should Not Be Empty")
            return

        # check id user is in users table and is user is admin and update vendingState accordingly
        isLogin, isAdmin = auth.isLogin(username.get(), password.get())
        if isLogin == None:
            messagebox.showerror("error", "User Name OR Password is wrong")
            return
        else:
            vendingState["is_authenticated"] = True
            vendingState["is_admin"] = isAdmin
            frame = Frame(main, width=600,height=285,bg="#000000")
            frame.place(x=765, y=40)
            button = Button(frame, text= "Logout",border=4,bg="#00FF7F",pady=2,command=log_out,activebackground="#000000",activeforeground="#FFFFFF")
            button.place(x=530, y=250)
            button = Button(frame, text= "Go To Admin",border=4,bg="#00FF7F",pady=2,command=go_to_admin,activebackground="#000000",activeforeground="#FFFFFF")
            button.place(x=430, y=250)

    # sign in frame and its elements
    frame = Frame(main, width=600,height=285,bg="#000000")
    frame.place(x=765, y=40)
    Label(frame,text="Sign in",font=("Arial",30,"bold"),fg="white",bg="#000000").place(x=230,y=15)

    # username input
    username = Entry(frame, width=40)
    username.place(x=180, y=80, height=30)
    username.insert(0,"   Username")
    username.bind("<Button-1>",username_input)

    # password input
    password = Entry(frame, width=40,show="*")
    password.place(x=180, y=130, height=30)
    password.insert(0,"*******@")
    password.bind("<Button-1>",password_imput)

    # Sign In Button
    button = Button(frame, text= "Sign In",border=4,bg="#00FF7F",pady=2,command=get_sign_in,activebackground="#000000",activeforeground="#FFFFFF")
    button.place(x=265, y=180)

    # Sign Up area and button
    donot = LabelFrame(frame,width=300,height=40,bg="#000000")
    donot.place(x=155,y=230)
    Label(donot, text="Don't have an account?",fg="white",bg="#000000").place(x=40, y=6)
    Button(donot, text="Sign up!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_up,activebackground="#000000",activeforeground="#FFFFFF").place(x=180, y=6)
