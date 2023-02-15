from tkinter import messagebox
from tkinter import *
import sqlite3
import product


def record_of_biscuits(main, vendingState):
    '''
    @params: no
    added record button
    if clicked biscuits window appear
    '''
    frame2 = Frame(main, width=1700,height=800,bg="#000000")
    frame2.place(x=90, y=1)
    listbox2 = Listbox(main, width=130, height=35,bg="#6A6161",fg="#FFFFFF")
    listbox2.place(x=90,y=60)


    def update_record_of_biscuits(): 
        '''
            @params: no
            added update button
            if clicked update form appears
        '''                 
        frame2 = Frame(main, width=250,height=200,bg="#141414")
        frame2.place(x=900, y=60)
            
        def create_biscuits_button(): 
            product.add_Biscuit(id.get(), name.get(), price.get(), quantity.get())                              

            
            added_user = Frame(main, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="Biscuit Has Been Updated",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n Biscuits Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Update Biscuits Again",command=record_of_biscuits,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
                    
        
        
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
                    
        Label(frame2,text="Update Biscuits",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame2,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame2,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame2,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame2,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame2,text="Update Biscuits",command=create_biscuits_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

    def create_record_of_biscuits():
        '''
            @params: no
            added create button
            if clicked create form appears
        '''                  
        frame2 = Frame(main, width=250,height=200,bg="#141414")
        frame2.place(x=900, y=60)
            
        def create_biscuits_button(): 
            product.add_Biscuit(id.get(), name.get(), price.get(), quantity.get())                              

            added_user = Frame(main, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="Biscuit Has Been Added",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n Biscuits Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Add Biscuits Again",command=record_of_biscuits,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

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
                    
        Label(frame2,text="For Biscuits",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame2,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame2,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame2,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame2,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame2,text="Add Biscuits",command=create_biscuits_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)


    def show_biscuits_record():
        '''
            @params: no
            added show record button
            if clicked record will be shown
        '''
        try:
            records = product.query_all_biscuits()
            listbox2.delete(0, END)

            for record in records:
                listbox2.insert(END, record)
                
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
                selected_item = listbox2.get(ACTIVE)
                user_id = selected_item[0]
                product.delete_biscuit(user_id)     

                show_biscuits_record()

            except sqlite3.Error as e:
                print(e)

        Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
        Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

    Button(frame2, text="Create Record Of Biscuits",command=create_record_of_biscuits,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
    Button(frame2, text="Show Biscuits Records",command=show_biscuits_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=255,y=25)
    Button(frame2, text="Update Biscuits Record",command=update_record_of_biscuits,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=397,y=25)
    Button(frame2, text="Delete Biscuits Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=547,y=25)
    