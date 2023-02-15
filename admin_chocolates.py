from tkinter import messagebox
from tkinter import *
import sqlite3
import product

def record_of_chocolates(main, vendingState): 
    '''
    @params: no
    added chocolate button
    if clicked chocolate window appears
    '''      
                    
    frame3 = Frame(main, width=1700,height=800,bg="#000000")
    frame3.place(x=90, y=1)
    listbox3 = Listbox(main, width=130, height=35,bg="#6A6161",fg="#FFFFFF")
    listbox3.place(x=90,y=60)


    def update_record_of_chocolates():
        '''
            @params: no
            added update button
            if clicked update form appears
        '''                  
        frame3 = Frame(main, width=250,height=200,bg="#141414")
        frame3.place(x=900, y=60)
            
        def create_chocolates_button(): 
            product.add_chocolate(id.get(), name.get(), price.get(), quantity.get())                              

            added_user = Frame(main, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="Chocolates Has Been Updated",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n Chocolates Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Update Chocolates Again",command=record_of_chocolates,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

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
                    
        Label(frame3,text="Update Chocolates",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame3,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame3,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame3,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame3,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame3,text="Update Chocolates",command=create_chocolates_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

    def create_record_of_chocolates():
        '''
            @params: no
            added create button
            if clicked create form appears
        '''                  
        frame3 = Frame(main, width=250,height=200,bg="#141414")
        frame3.place(x=900, y=60)
            
        def create_chocolates_button(): 
            product.add_chocolate(id.get(), name.get(), price.get(), quantity.get())                              

            added_user = Frame(main, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="Chocolates Has Been Added",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n Chocolates Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Add Chocolates Again",command=record_of_chocolates,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

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
                    
        Label(frame3,text="For Chocolates",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame3,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame3,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame3,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame3,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame3,text="Add Chocolates",command=create_chocolates_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

    def show_chocolates_record():
        '''
            @params: no
            added show record button
            if clicked records will be shown
        '''
        try:
            records = product.query_all_chocolates()         
            listbox3.delete(0, END)

            for record in records:
                listbox3.insert(END, record)

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
                selected_item = listbox3.get(ACTIVE)
                user_id = selected_item[0]
                product.delete_chocolate(user_id)     

                show_chocolates_record()

            except sqlite3.Error as e:
                print(e)

        Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
        Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

    Button(frame3, text="Create Record Of Chocolates",command=create_record_of_chocolates,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=78,y=25)        
    Button(frame3, text="Show Chocolates Records",command=show_chocolates_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=257,y=25)
    Button(frame3, text="Update Chocolates Record",command=update_record_of_chocolates,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=418,y=25)
    Button(frame3, text="Delete Chocolates Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=582,y=25)
    