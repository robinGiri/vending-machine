from tkinter import *
import sqlite3
import product

def record_of_product(new, type):
    '''
    @params: new as param
    added record button
    if clicked chips window will be displayed
    '''

    frame4 = Frame(new, width=1700,height=800,bg="#000000")
    frame4.place(x=90, y=1)
    listbox4 = Listbox(new, width=130, height=35,bg="#6A6161",fg="#FFFFFF")
    listbox4.place(x=90,y=60)
    def update_record_of_products(): 
        '''
        @params: no
        added update button
        if clicked update form appears
        '''

        frame4 = Frame(new, width=250,height=200,bg="#141414")
        frame4.place(x=900, y=60)
            
        def create_products_button():
            if type == "Drinks" :
                product.add_drink(id.get(), name.get(), price.get(), quantity.get())

            if type == "Biscuits" :
                product.add_Biscuit(id.get(), name.get(), price.get(), quantity.get())

            if type == "Chocolate" :
                product.add_chocolate(id.get(), name.get(), price.get(), quantity.get())                       

            if type == "Chips" :
                product.add_chips(id.get(), name.get(), price.get(), quantity.get())
    
            added_user = Frame(new, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="{} Has Been Updated".format(type),font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n {} Info".format(type),font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Update {} Again".format(type),command=record_of_product,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

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

        Label(frame4,text="Update {}".format(type),font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame4,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame4,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame4,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame4,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame4,text="Update {}".format(type),command=create_products_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

    def create_record_of_products():
        '''
        @params: no
        added create button
        if clicked create form appears
        '''            
                            
        frame4 = Frame(new, width=250,height=200,bg="#141414")
        frame4.place(x=900, y=60)
            
        def create_products_button(): 
            if type == "Drinks" :
                product.add_drink(id.get(), name.get(), price.get(), quantity.get())  

            if type == "Biscuits" :
                product.add_Biscuit(id.get(), name.get(), price.get(), quantity.get())

            if type == "Chocolate" :
                product.add_chocolate(id.get(), name.get(), price.get(), quantity.get())                       

            if type == "Chips" :
                product.add_chips(id.get(), name.get(), price.get(), quantity.get())                             

            added_user = Frame(new, width=250,height=200,bg="#000000")
            added_user.place(x=900, y=60)   
            Label(added_user,text="{} Has Been Added".format(type),font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
            Label(added_user,text="Press Okey To Return Back To \n {} Info".format(type),font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
            Button(added_user,text="Add {} Again".format(type),command=record_of_product,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

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

        Label(frame4,text="For {}".format(type),font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
        id = Entry(frame4,width=30)
        id.place(x=30,y=40,height=20)
        id.insert(0,"   Id")
        id.bind("<Button-1>",idd)         
        name = Entry(frame4,width=30)
        name.place(x=30,y=70,height=20)
        name.insert(0,"   Name")
        name.bind("<Button-1>",namee)  
        price = Entry(frame4,width=30)
        price.place(x=30,y=100,height=20)
        price.insert(0,"   Price")
        price.bind("<Button-1>",pricee)  
        quantity = Entry(frame4,width=30)
        quantity.place(x=30,y=130,height=20)
        quantity.insert(0,"   Quantity")
        quantity.bind("<Button-1>",quantityy)  
        Button(frame4,text="Add {}".format(type),command=create_products_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

    def show_products_record():
        '''
        @params: no
        added show record button
        if clicked records will be shown
        '''

        try:
            
            if type == "Drinks" :
                records = product.query_all_drinks()       

            if type == "Biscuits" :
                records = product.query_all_biscuits()       

            if type == "Chocolate" :
                records = product.query_all_chocolates()       

            if type == "Chips" :
                records = product.query_all_chips()       

            listbox4.delete(0, END)

            for record in records:
                listbox4.insert(END, record)

        except sqlite3.Error as e:
            print(e)

    def delete():
        '''
        @params: no
        added delete button
        if clicked records will be deleted
        '''

        clear = Frame(new, width=250,height=200,bg="#141414")
        clear.place(x=900, y=60)
        
        def delete_selected_products_record():
            try:
                selected_item = listbox4.get(ACTIVE)
                user_id = selected_item[0]
                product.delete_chips(user_id)  
                
                if type == "Drinks" :
                    product.delete_drink(user_id)    

                if type == "Biscuits" :
                    product.delete_biscuit(user_id)    

                if type == "Chocolate" :
                    product.delete_chocolate(user_id)    

                if type == "Chips" :
                    product.delete_chips(user_id)    

                show_products_record()

            except :
                print("An Error Occured")

        Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
        Button(clear, text="Delete Record",command=delete_selected_products_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

    Button(frame4, text="Create Record Of {}".format(type),command=create_record_of_products,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
    Button(frame4, text="Show {} Records".format(type),command=show_products_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=247,y=25)
    Button(frame4, text="Update {} Record".format(type),command=update_record_of_products,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=385,y=25)
    Button(frame4, text="Delete {} Record".format(type),command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=527,y=25)
