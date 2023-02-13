from tkinter import *
import sqlite3
import product
from tkinter import messagebox
import cash
from PIL import Image,ImageTk
import register
import auth
import adminMain


def newpage(main):
    new = Toplevel(main)
    new.state("zoomed")
    new.title("Records")
    frame = Frame(new, width=1700,height=800,bg="#000000")
    frame.place(x=1, y=1)
    listbox = Listbox(new, width=130, height=35,bg="white")
    listbox.place(x=90,y=60)

    
    def record_of_users():
        frame1_1_1 = Frame(new, width=1700,height=800,bg="purple")
        frame1_1_1.place(x=90, y=1)
        listbox1_1_1 = Listbox(new, width=130, height=35,bg="white")
        listbox1_1_1.place(x=90,y=60)
        
        def create_record_of_user():
            add_user1 = Frame(new, width=250,height=200,bg="#000000")
            add_user1.place(x=900, y=60)
            Label(add_user1,text="For Users",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            id = Entry(add_user1,width=30).place(x=30,y=40,height=20)        
            name = Entry(add_user1,width=30).place(x=30,y=70,height=20)
            price = Entry(add_user1,width=30).place(x=30,y=100,height=20)
            quantity = Entry(add_user1,width=30).place(x=30,y=130,height=20)
            Button(add_user1,text="Add User",fg="#00FF7F",bg="#000000",activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
            
        def show_user_record():
            try:
                conn = sqlite3.connect("vending_machine.db")
                c = conn.cursor() 

                c.execute("SELECT * FROM users") 
                records = c.fetchall()        
                listbox1_1_1.delete(0, END)

                for record in records:
                    listbox1_1_1.insert(END, record)
                    
            except sqlite3.Error as e:
                print(e)
                
            finally:
                conn.close() 


        Button(frame1_1_1, text="Create Record Of Users",command=create_record_of_user).place(x=95,y=25)        
        Button(frame1_1_1, text="Show Users Records",command=show_user_record).place(x=250,y=25)
        Button(frame1_1_1, text="Update Users Record").place(x=375,y=25)
        Button(frame1_1_1, text="Delete Users Record").place(x=530,y=25)


    def record_of_cashes():
        frame1_1 = Frame(new, width=1700,height=800,bg="gray")
        frame1_1.place(x=90, y=1)
        listbox1_1 = Listbox(new, width=130, height=35,bg="purple")
        listbox1_1.place(x=90,y=60)
        def create_record_of_cashes():
            frame1_1 = Frame(new, width=250,height=200,bg="#000000")
            frame1_1.place(x=900, y=60)
            Label(frame1_1,text="For Cashes",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            id = Entry(frame1_1,width=30).place(x=30,y=40,height=20)        
            name = Entry(frame1_1,width=30).place(x=30,y=70,height=20)
            price = Entry(frame1_1,width=30).place(x=30,y=100,height=20)
            quantity = Entry(frame1_1,width=30).place(x=30,y=130,height=20)
            Button(frame1_1,text="Add Cashes",fg="#00FF7F",bg="#000000",activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
            
        def show_cash_record():
            try:
                conn = sqlite3.connect("vending_machine.db")
                c = conn.cursor() 

                c.execute("SELECT * FROM Cash") 
                records = c.fetchall()        
                listbox1_1.delete(0, END)

                for record in records:
                    listbox1_1.insert(END, record)
                    
            except sqlite3.Error as e:
                print(e)
                
            finally:
                conn.close() 
            
        Button(frame1_1, text="Create Record Of Cashes",command=create_record_of_cashes).place(x=95,y=25)        
        Button(frame1_1, text="Show Cashes Records",command=show_cash_record).place(x=250,y=25)
        Button(frame1_1, text="Update Cashes Record").place(x=375,y=25)
        Button(frame1_1, text="Delete Cashes Record").place(x=530,y=25)


    def record_of_drinks():
                
        frame1 = Frame(new, width=1700,height=800,bg="red")
        frame1.place(x=90, y=1)
        listbox1 = Listbox(new, width=130, height=35,bg="gray")
        listbox1.place(x=90,y=60)

        def create_record_of_drinks():
            
            def create_drinks():
                product.add_drink(id.get(), name.get(), price.get(), quantity.get())
                
            frame1 = Frame(new, width=250,height=200,bg="#000000")
            frame1.place(x=900, y=60)
            Label(frame1,text="For Drinks",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            id = Entry(frame1,width=30)
            id.place(x=30,y=40,height=20)        
            name = Entry(frame1,width=30)
            name.place(x=30,y=70,height=20)
            price = Entry(frame1,width=30)
            price.place(x=30,y=100,height=20)
            quantity = Entry(frame1,width=30)
            quantity.place(x=30,y=130,height=20)
            Button(frame1,text="Add Drink",fg="#00FF7F",bg="#000000",activebackground="#000000",activeforeground="#FFFFFF",command=create_drinks).place(x=90,y=160)
        Button(frame1, text="Create Record Of Drinks",command=create_record_of_drinks).place(x=95,y=25)        
        Button(frame1, text="Show Drinks Records").place(x=250,y=25)
        Button(frame1, text="Update Drinks Record").place(x=375,y=25)
        Button(frame1, text="Delete Drinks Record").place(x=530,y=25)

    def record_of_biscuits():
        frame2 = Frame(new, width=1700,height=800,bg="blue")
        frame2.place(x=90, y=1)
        listbox2 = Listbox(new, width=130, height=35,bg="red")
        listbox2.place(x=90,y=60)
        def create_record_of_biscuits():
            frame2 = Frame(new, width=250,height=200,bg="#000000")
            frame2.place(x=900, y=60)
            Label(frame2,text="For Biscuits",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            id = Entry(frame2,width=30).place(x=30,y=40,height=20)        
            name = Entry(frame2,width=30).place(x=30,y=70,height=20)
            price = Entry(frame2,width=30).place(x=30,y=100,height=20)
            quantity = Entry(frame2,width=30).place(x=30,y=130,height=20)
            Button(frame2,text="Add Biscuits",fg="#00FF7F",bg="#000000",activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
        Button(frame2, text="Create Record Of Biscuits",command=create_record_of_biscuits).place(x=95,y=25)        
        Button(frame2, text="Show Biscuits Records").place(x=250,y=25)
        Button(frame2, text="Update Biscuits Record").place(x=375,y=25)
        Button(frame2, text="Delete Biscuits Record").place(x=530,y=25)
        
    def record_of_chocolates():
        frame3 = Frame(new, width=1700,height=800,bg="green")
        frame3.place(x=90, y=1)
        listbox3 = Listbox(new, width=130, height=35,bg="yellow")
        listbox3.place(x=90,y=60)
        def create_record_of_chocolates():
            frame3 = Frame(new, width=250,height=200,bg="#000000")
            frame3.place(x=900, y=60)
            Label(frame3,text="For Chocolates",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            id = Entry(frame3,width=30).place(x=30,y=40,height=20)        
            name = Entry(frame3,width=30).place(x=30,y=70,height=20)
            price = Entry(frame3,width=30).place(x=30,y=100,height=20)
            quantity = Entry(frame3,width=30).place(x=30,y=130,height=20)
            Button(frame3,text="Add Chocolates",fg="#00FF7F",bg="#000000",activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
        Button(frame3, text="Create Record Of Chocolates",command=create_record_of_chocolates).place(x=95,y=25)        
        Button(frame3, text="Show Chocolates Records").place(x=250,y=25)
        Button(frame3, text="Update Chocolates Record").place(x=375,y=25)
        Button(frame3, text="Delete Chocolates Record").place(x=530,y=25)

    def record_of_chips():
        frame4 = Frame(new, width=1700,height=800,bg="yellow")
        frame4.place(x=90, y=1)
        listbox4 = Listbox(new, width=130, height=35,bg="green")
        listbox4.place(x=90,y=60) 
        def create_record_of_chips():
            frame4 = Frame(new, width=250,height=200,bg="#000000")
            frame4.place(x=900, y=60)
            Label(frame4,text="For Chips",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            id = Entry(frame4,width=30).place(x=30,y=40,height=20)        
            name = Entry(frame4,width=30).place(x=30,y=70,height=20)
            price = Entry(frame4,width=30).place(x=30,y=100,height=20)
            quantity = Entry(frame4,width=30).place(x=30,y=130,height=20)
            Button(frame4,text="Add Chips",fg="#00FF7F",bg="#000000",activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
        Button(frame4, text="Create Record Of Chips",command=create_record_of_chips).place(x=95,y=25)        
        Button(frame4, text="Show Chips Records").place(x=250,y=25)
        Button(frame4, text="Update Chips Record").place(x=375,y=25)
        Button(frame4, text="Delete Chips Record").place(x=530,y=25)


    Button(frame, text="Users",command=record_of_users).place(x=10,y=80)
    Button(frame, text="Cashes",command=record_of_cashes).place(x=10,y=140)
    Button(frame, text="Drinks",command=record_of_drinks).place(x=10,y=200)
    Button(frame, text="Biscuits",command=record_of_biscuits).place(x=10,y=260)
    Button(frame, text="Chocolates",command=record_of_chocolates).place(x=10,y=320)
    Button(frame, text="Chips",command=record_of_chips).place(x=10,y=380)


            