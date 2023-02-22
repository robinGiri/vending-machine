from tkinter import messagebox
from tkinter import *
import loginScreen
import auth

def register(main, vendingState):

    def sign_in():
        '''
        params: no params
        redirects to login UI
        '''
        loginScreen.login(main, vendingState)

    # log out of vending machine 
    def log_out():
        '''
        params: no params
        removes auth from vending machine
        '''
        vendingState["is_authenticated"] = False
        loginScreen.login(main, vendingState)        

    # configure username input
    def username_input(user):
        username.config(state=NORMAL)
        username.delete(0, END)

    # configure password input
    def email_imput(myemail):
        email.config(state=NORMAL)
        email.delete(0, END)

    # configure password input
    def password_imput(secret):
        password.config(state=NORMAL)
        password.delete(0, END)

    def getRegistered():
        '''
        params: no params
        check if username already exists
        check correct username, emails and passowrd
        creates username, email and  password exist in users table
        vendingState["is_authenticated"] = True if gets created
        '''

        # check if username, email and password are empty
        if username.get() == "" or password.get() == "" or email.get() == "":
            messagebox.showerror("error", "Username OR Password OR Email Should Not Be Empty")
            return
 
        # check if they have @softwarica.edu.np which is required
        elif "@softwarica.edu.np" not in email.get():
            messagebox.showerror("error", "Email Must BE Ending With @softwarica.edu.np")
            return

        # check if password is less then 8 string
        elif len(password.get()) <8:
            messagebox.showerror("error", "Password Must Be Of 8 Or More Character")
            return

        # check if they haven't change anything and just clicked for sign up
        elif "email@softwarica.edu.np" in email.get() :
            messagebox.showerror("error", "Choose Email")
            return

        # check if they haven't change anything and just clicked for sign up
        elif  "   Username" in username.get():
            messagebox.showerror("error", "Choose Username")
            return

        # check if they haven't change anything and just clicked for sign up
        elif "*******@" in password.get():
            messagebox.showerror("error", "Choose Password")
            return

        else:
            # look for all the username in users table and sent error if username already exist
            users = auth.query_all_users()
            for user in users:
                list1 = list(user)
                if list1[1] == username.get():
                    messagebox.showerror("error", "Username already exist.")
                    return

            auth.create_user(username.get(), email.get(), password.get())
            vendingState["is_authenticated"] = True
            frame = Frame(main, width=600,height=285,bg="black",)
            frame.place(x=765, y=40)
            Label(frame,text="Registration Successfull",font=("Arial",15,"bold"),fg="green",bg="#000000").place(x=50,y=20)
            button = Button(frame, text= "Logout",border=4,bg="#00FF7F",pady=2,command=log_out)
            button.place(x=530, y=250)

    # register frame and its elements
    frame = Frame(main, width=600,height=285,bg="#000000",)
    frame.place(x=765, y=40)
    Label(frame,text="Become a member",font=("Arial",25,"bold"),fg="white",bg="#000000").place(x=160,y=5)

    # username input
    username = Entry(frame, width=40)
    username.place(x=180, y=60, height=30)
    username.insert(0,"   Username")
    username.bind("<Button-1>",username_input)

    # email input
    email = Entry(frame, width=40)
    email.place(x=180, y=110, height=30)
    email.insert(0,"   email@softwarica.edu.np")
    email.bind("<Button-1>",email_imput)

    # password input
    password = Entry(frame, width=40,show="*")
    password.place(x=180, y=160, height=30)
    password.insert(0,"*******@")
    password.bind("<Button-1>",password_imput)

    # Sign Up Button
    button = Button(frame, text= "Sign up",border=4,bg="#00FF7F",pady=2,command=getRegistered,activebackground="#000000",activeforeground="#FFFFFF")
    button.place(x=265, y=205)

    # Sign In area and button
    already = LabelFrame(frame,width=300,height=40,bg="#000000")
    already.place(x=150, y=245)
    Label(already, text="Already have an account?",fg="white",bg="#000000").place(x=40, y=6)
    b=Button(already, text="Sign in!",fg="#00FF7F",bg="#000000",borderwidth=0,command=sign_in,activebackground="#000000",activeforeground="#FFFFFF")
    b.place(x=180, y=6)
