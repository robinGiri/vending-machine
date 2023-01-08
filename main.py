from tkinter import *
import seed

main = Tk()
main.state("zoomed")


# this will add title
main.title("Vending Machine")

# this will create a label widget
space1 = Label(main).grid(row=0,column=0,padx=50,pady=50)
space2 = Label(main).grid(row=1,column=1,padx=50,pady=50)

i = 0
while i < len(seed.items):
    Label(main, text= list(seed.items)[i]).grid(row=i*2+2,column=2,padx=5)
    for j,options in enumerate(seed.items[list(seed.items)[i]]):
        Label(main,text=options).grid(row=i*2+2,column=j+3,padx=5)
    i +=1
    
def Success():
    print("login or registered..")

def Register():
    registerMainTitle = Label(main, text="Become a member",fg="white", font=(None, 35)).grid(row=1,column=11,padx=5)
    userNameInput = Entry(main, width=40,bg="#4b443f",fg="white")
    userNameInput.insert(0, '')
    userNameInput.grid(row=2,column=11,padx=5)
    passwordInput = Entry(main, width=40,bg="#4b443f",fg="white")
    passwordInput.insert(0, '')
    passwordInput.grid(row=3,column=11,padx=5)
    
    reg = LabelFrame(main,bg="#202020",pady=20).grid(row=6,column=11)
    
    sign = Button(main, text="Sign Up",borderwidth=0,bg="#00FF7F",padx=20,pady=1,font=7,border=3,command=Success)
    sign.grid(row=5,column=11,pady=20)

    up = LabelFrame(main,bg="#202020")
    up.grid(row=6,column=11)
    sign = Label(up, text= "Already have an account?",fg="white",bg="#202020",font=("Arial",10),borderwidth=0).grid(row=6,column=11,padx=120,pady=10)
    btn = Button(up, text="Sign In!",fg="#00FF7F",bg="#202020",borderwidth=0,command=Login).place(x=258,y=8)

def Login():
    space1 = Label(main).grid(row=0,column=10,padx=10,pady=10)
    loginMainTitle = Label(main, text="Sign In",fg="white", font=(None, 35)).grid(row=1,column=11,padx=5)
    userNameInput = Entry(main, width=40,bg="#4b443f",fg="white")
    userNameInput.insert(0, 'Username')
    userNameInput.grid(row=2,column=11,padx=5)
    passwordInput = Entry(main, width=40,bg="#4b443f",fg="white")
    passwordInput.insert(0, 'Password')
    passwordInput.grid(row=3,column=11,padx=5)
    
    sign = Button(main, text="Sign In",borderwidth=0,bg="#00FF7F",padx=20,pady=1,font=7,border=3,command=Success)
    sign.grid(row=5,column=11,pady=20)

    up = LabelFrame(main,bg="#202020")
    up.grid(row=6,column=11)
    sign = Label(up, text= "Don't have an account?",fg="white",bg="#202020",font=("Arial",10),borderwidth=0).grid(row=6,column=11,padx=120,pady=10)
    btn = Button(up, text="Sign Up!",fg="#00FF7F",bg="#202020",borderwidth=0,command=Register).place(x=258,y=8)

Login()

main.mainloop()

