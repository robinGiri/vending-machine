from tkinter import messagebox
from tkinter import *
import sqlite3
import product


def record_of_drinks(main, vendingState):
    '''
        @params: no
        added drinks button
        if clicked drinks window appears
    '''
            
    frame1 = Frame(main, width=1700,height=800,bg="#000000")
    frame1.place(x=90, y=1)
    listbox1 = Listbox(main, width=130, height=35,bg="#6A6161",fg="#FFFFFF")
    listbox1.place(x=90,y=60)


    def update_record_of_drinks():
        '''
            @params: no
            added update button
            if clicked update form appears
        '''                  
        frame1 = Frame(main, width=250,height=200,bg="#141414")
        frame1.place(x=900, y=60)
            
        def create_drink_button(): 
            product.add_drink(id.get(), name.get(), price.get(), quantity.get())                              

            
            added_user = Frame(main, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="Drink Has Been Updated",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n Drinks Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Update Drink Again",command=record_of_drinks,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

        def idd(usee):
            id.config(state=NORMAL)
            id.delete(0, END)
        def namee(passs):
            name.config(state=NORMAL)
            name.delete(0, END)
            
        def pricee(emaii):
            price.config(state=NORMAL)
            price.delete(0, END)
        
        def quantityy(e):
            quantity.config(state=NORMAL)
            quantity.delete(0, END) 
                    
        Label(frame1,text="Update Drinks",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame1,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame1,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame1,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame1,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame1,text="Update Drink",command=create_drink_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

    def create_record_of_drinks():
        '''
            @params: no
            added create button
            if clicked create form appears
        '''                  
        frame1 = Frame(main, width=250,height=200,bg="#141414")
        frame1.place(x=900, y=60)
            
        def create_drink_button(): 
            product.add_drink(id.get(), name.get(), price.get(), quantity.get())                              

            added_user = Frame(main, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="Drink Has Been Added",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n Drinks Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Add Drink Again",command=record_of_drinks,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
                    
        def idd(usee):
            id.config(state=NORMAL)
            id.delete(0, END)
        def namee(passs):
            name.config(state=NORMAL)
            name.delete(0, END)
            
        def pricee(emaii):
            price.config(state=NORMAL)
            price.delete(0, END)
        
        def quantityy(e):
            quantity.config(state=NORMAL)
            quantity.delete(0, END) 
                    
        Label(frame1,text="For Drinks",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame1,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame1,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame1,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame1,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame1,text="Add Drink",command=create_drink_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
    def show_drink_record():
        '''
            @params: no
            added show record button
            if clicked it will show records of drinks
        '''
        try:

            records = product.query_all_drinks()   
            listbox1.delete(0, END)

            for record in records:
                listbox1.insert(END, record)

        except sqlite3.Error as e:
            print(e)

    def delete():
        '''
            @params: no
            added delete button
            if clicked records will be deleted
        '''
        clear = Frame(main, width=250,height=200,bg="#141414")
        clear.place(x=900, y=60)

        def delete_selected_user_record():
            try:
                selected_item = listbox1.get(ACTIVE)
                user_id = selected_item[0]
                product.delete_drink(user_id)     

                show_drink_record()

            except sqlite3.Error as e:
                print(e)




        Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
        Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

    Button(frame1, text="Create Record Of Drinks",command=create_record_of_drinks,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
    Button(frame1, text="Show Drinks Records",command=show_drink_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=250,y=25)
    Button(frame1, text="Update Drinks Record",command=update_record_of_drinks,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=388,y=25)
    Button(frame1, text="Delete Drinks Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=530,y=25)
