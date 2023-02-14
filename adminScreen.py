from tkinter import *
import sqlite3
import product
import cash
import auth

def newWindow(main):

    new = Toplevel(main)
    new.state("zoomed")
    new.title("Vending Admin Pannel")

    frame = Frame(new, width=1700,height=800,bg="#000000")
    frame.place(x=1, y=1)
    listbox = Listbox(new, width=130, height=35,bg="#141414",fg="#FFFFFF")
    listbox.place(x=90,y=60)

    def record_of_users():
        frame1_1_1 = Frame(new, width=1700,height=800,bg="#000000")
        frame1_1_1.place(x=90, y=1)
        listbox1_1_1 = Listbox(new, width=130, height=35,bg="#141414",fg="#FFFFFF")
        listbox1_1_1.place(x=90,y=60)

        def show_user_record():

            try:
                records = auth.query_all_users()       
                listbox1_1_1.delete(0, END)
                for record in records:
                    listbox1_1_1.insert(END, record)
  
            except sqlite3.Error as e:
                print(e)

        def delete():
            clear = Frame(new, width=250,height=200,bg="#141414")
            clear.place(x=900, y=60)

            def delete_selected_user_record():
                try:
                    auth.delete_user(user_id)     
                    selected_item = listbox1_1_1.get(ACTIVE)
                    user_id = selected_item[0]

                    show_user_record()

                except sqlite3.Error as e:
                    print(e)

            Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
            Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)
  
        Button(frame1_1_1, text="Show Users Records",command=show_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=250,y=25)
        Button(frame1_1_1, text="Delete Users Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=530,y=25)

    def record_of_cashes():
        frame1_1 = Frame(new, width=1700,height=800,bg="#000000")
        frame1_1.place(x=90, y=1)
        listbox1_1 = Listbox(new, width=130, height=35,bg="#141414",fg="#FFFFFF")
        listbox1_1.place(x=90,y=60)

        def update_record_of_cashes():
            add_user1 = Frame(new, width=250,height=200,bg="#141414")
            add_user1.place(x=900, y=60)
            
            def create_cash_button():                                 
                
                cash.add_cash(ID.get(), Value.get(), Quantity.get())                

                added_user = Frame(new, width=250,height=200,bg="#000000")
                added_user.place(x=900, y=60)   
                Label(added_user,text="Cash Has Been Updated",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
                Label(added_user,text="Press Okey To Return Back To \n Cashes Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)              
                Button(added_user,text="Update Cash Again",command=record_of_cashes,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
            def use(usee):
                ID.config(state=NORMAL)
                ID.delete(0, END)
            def pas(passs):
                Value.config(state=NORMAL)
                Value.delete(0, END)
                
            def emai(emaii):
                Quantity.config(state=NORMAL)
                Quantity.delete(0, END)      
                
            Label(add_user1,text="Update Cashes",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            ID = Entry(add_user1,width=30)
            ID.place(x=30,y=40,height=20) 
            ID.insert(0,"   ID")
            ID.bind("<Button-1>",use)       
            Value = Entry(add_user1,width=30)
            Value.place(x=30,y=70,height=20)
            Value.insert(0,"   Value")
            Value.bind("<Button-1>",pas)
            Quantity = Entry(add_user1,width=30)
            Quantity.place(x=30,y=100,height=20)
            Quantity.insert(0, "Quantity")
            Quantity.bind("<Button-1>",emai)
            Button(add_user1,text="Update Cash",command=create_cash_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

        def create_record_of_cashes():
            add_user1 = Frame(new, width=250,height=200,bg="#141414")
            add_user1.place(x=900, y=60)
             
            def create_cash_button():                                 
                
                cash.add_cash(ID.get(), Value.get(), Quantity.get())                
                
                added_user = Frame(new, width=250,height=200,bg="#000000")
                added_user.place(x=900, y=60)   
                Label(added_user,text="Cash Has Been Added",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
                Label(added_user,text="Press Okey To Return Back To \n Cashes Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)
                    
                             
                Button(added_user,text="Add Cash Again",command=record_of_cashes,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
            def use(usee):
                ID.config(state=NORMAL)
                ID.delete(0, END)
            def pas(passs):
                Value.config(state=NORMAL)
                Value.delete(0, END)
                
            def emai(emaii):
                Quantity.config(state=NORMAL)
                Quantity.delete(0, END)      
                
            Label(add_user1,text="For Cashes",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
            ID = Entry(add_user1,width=30)
            ID.place(x=30,y=40,height=20) 
            ID.insert(0,"   ID")
            ID.bind("<Button-1>",use)       
            Value = Entry(add_user1,width=30)
            Value.place(x=30,y=70,height=20)
            Value.insert(0,"   Value")
            Value.bind("<Button-1>",pas)
            Quantity = Entry(add_user1,width=30)
            Quantity.place(x=30,y=100,height=20)
            Quantity.insert(0, "Quantity")
            Quantity.bind("<Button-1>",emai)
            Button(add_user1,text="Add Cash",command=create_cash_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)
         
        def show_cash_record():
            try:
                records = cash.query_all_cashes()
                listbox1_1.delete(0, END)

                for record in records:
                    listbox1_1.insert(END, record)
                    
            except sqlite3.Error as e:
                print(e)
  
        def delete():
            clear = Frame(new, width=250,height=200,bg="#141414")
            clear.place(x=900, y=60)
        
            def delete_selected_user_record():
                try:
                    cash.delete_cash(user_id)

                    selected_item = listbox1_1.get(ACTIVE)
                    user_id = selected_item[0]

                    show_cash_record()
                    
                except sqlite3.Error as e:
                    print(e)

            Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
            Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

        Button(frame1_1, text="Create Record Of Cashes",command=create_record_of_cashes,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
        Button(frame1_1, text="Show Cashes Records",command=show_cash_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=250,y=25)
        Button(frame1_1, text="Update Cashes Record",command=update_record_of_cashes,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=385,y=25)
        Button(frame1_1, text="Delete Cashes Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=530,y=25)

    def record_of_drinks():
                
        frame1 = Frame(new, width=1700,height=800,bg="#000000")
        frame1.place(x=90, y=1)
        listbox1 = Listbox(new, width=130, height=35,bg="#141414",fg="#FFFFFF")
        listbox1.place(x=90,y=60)


        def update_record_of_drinks():                  
            frame1 = Frame(new, width=250,height=200,bg="#141414")
            frame1.place(x=900, y=60)
                
            def create_drink_button(): 
                product.add_drink(id.get(), name.get(), price.get(), quantity.get())                              

                
                added_user = Frame(new, width=250,height=200,bg="#000000")
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
            frame1 = Frame(new, width=250,height=200,bg="#141414")
            frame1.place(x=900, y=60)
                
            def create_drink_button(): 
                product.add_drink(id.get(), name.get(), price.get(), quantity.get())                              

                added_user = Frame(new, width=250,height=200,bg="#000000")
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
            try:

                records = product.query_all_drinks()   
                listbox1.delete(0, END)

                for record in records:
                    listbox1.insert(END, record)

            except sqlite3.Error as e:
                print(e)

        def delete():
            clear = Frame(new, width=250,height=200,bg="#141414")
            clear.place(x=900, y=60)
        
            def delete_selected_user_record():
                try:
                    product.delete_drink(user_id)

                    selected_item = listbox1.get(ACTIVE)
                    user_id = selected_item[0]

                    show_drink_record()

                except sqlite3.Error as e:
                    print(e)

            Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
            Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

        Button(frame1, text="Create Record Of Drinks",command=create_record_of_drinks,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
        Button(frame1, text="Show Drinks Records",command=show_drink_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=250,y=25)
        Button(frame1, text="Update Drinks Record",command=update_record_of_drinks,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=385,y=25)
        Button(frame1, text="Delete Drinks Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=530,y=25)

    def record_of_biscuits():
                        
        frame2 = Frame(new, width=1700,height=800,bg="#000000")
        frame2.place(x=90, y=1)
        listbox2 = Listbox(new, width=130, height=35,bg="#141414",fg="#FFFFFF")
        listbox2.place(x=90,y=60)


        def update_record_of_biscuits():                  
            frame2 = Frame(new, width=250,height=200,bg="#141414")
            frame2.place(x=900, y=60)
                
            def create_biscuits_button(): 
                product.add_Biscuit(id.get(), name.get(), price.get(), quantity.get())                              

                
                added_user = Frame(new, width=250,height=200,bg="#000000")
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
            frame2 = Frame(new, width=250,height=200,bg="#141414")
            frame2.place(x=900, y=60)
                
            def create_biscuits_button(): 
                product.add_Biscuit(id.get(), name.get(), price.get(), quantity.get())                              

                added_user = Frame(new, width=250,height=200,bg="#000000")
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
            try:
                records = product.query_all_biscuits()
                listbox2.delete(0, END)

                for record in records:
                    listbox2.insert(END, record)
                    
            except sqlite3.Error as e:
                print(e)

        def delete():
            clear = Frame(new, width=250,height=200,bg="#141414")
            clear.place(x=900, y=60)

            def delete_selected_user_record():
                try:
                    product.delete_biscuit(user_id)

                    selected_item = listbox2.get(ACTIVE)
                    user_id = selected_item[0]

                    show_biscuits_record()

                except sqlite3.Error as e:
                    print(e)

            Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
            Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

        Button(frame2, text="Create Record Of Biscuits",command=create_record_of_biscuits,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
        Button(frame2, text="Show Biscuits Records",command=show_biscuits_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=250,y=25)
        Button(frame2, text="Update Biscuits Record",command=update_record_of_biscuits,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=385,y=25)
        Button(frame2, text="Delete Biscuits Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=530,y=25)
      
    def record_of_chocolates():       
                       
        frame3 = Frame(new, width=1700,height=800,bg="#000000")
        frame3.place(x=90, y=1)
        listbox3 = Listbox(new, width=130, height=35,bg="#141414",fg="#FFFFFF")
        listbox3.place(x=90,y=60)


        def update_record_of_chocolates():                  
            frame3 = Frame(new, width=250,height=200,bg="#141414")
            frame3.place(x=900, y=60)
                
            def create_chocolates_button(): 
                product.add_chocolate(id.get(), name.get(), price.get(), quantity.get())                              

                added_user = Frame(new, width=250,height=200,bg="#000000")
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
            frame3 = Frame(new, width=250,height=200,bg="#141414")
            frame3.place(x=900, y=60)
                
            def create_chocolates_button(): 
                product.add_chocolate(id.get(), name.get(), price.get(), quantity.get())                              

                added_user = Frame(new, width=250,height=200,bg="#000000")
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
            try:
                records = product.query_all_chocolates()         
                listbox3.delete(0, END)

                for record in records:
                    listbox3.insert(END, record)

            except sqlite3.Error as e:
                print(e)

        def delete():
            clear = Frame(new, width=250,height=200,bg="#141414")
            clear.place(x=900, y=60)
        
            def delete_selected_user_record():
                try:
                    product.delete_chocolate(user_id)

                    selected_item = listbox3.get(ACTIVE)
                    user_id = selected_item[0]

                    show_chocolates_record()

                except sqlite3.Error as e:
                    print(e)

            Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
            Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

        Button(frame3, text="Create Record Of Chocolates",command=create_record_of_chocolates,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=75,y=25)        
        Button(frame3, text="Show Chocolates Records",command=show_chocolates_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=260,y=25)
        Button(frame3, text="Update Chocolates Record",command=update_record_of_chocolates,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=420,y=25)
        Button(frame3, text="Delete Chocolates Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=580,y=25)
       
    def record_of_chips():
                       
        frame4 = Frame(new, width=1700,height=800,bg="#000000")
        frame4.place(x=90, y=1)
        listbox4 = Listbox(new, width=130, height=35,bg="#141414",fg="#FFFFFF")
        listbox4.place(x=90,y=60)

        def update_record_of_chips():                  
            frame4 = Frame(new, width=250,height=200,bg="#141414")
            frame4.place(x=900, y=60)
                
            def create_chips_button(): 
                product.add_chips(id.get(), name.get(), price.get(), quantity.get())                              

                added_user = Frame(new, width=250,height=200,bg="#000000")
                added_user.place(x=900, y=60)   
                Label(added_user,text="Chips Has Been Updated",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
                Label(added_user,text="Press Okey To Return Back To \n Chips Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
                Button(added_user,text="Update Chips Again",command=record_of_chips,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

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

            Label(frame4,text="Update Chips",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
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
            Button(frame4,text="Update Chips",command=create_chips_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

        def create_record_of_chips():                  
            frame4 = Frame(new, width=250,height=200,bg="#141414")
            frame4.place(x=900, y=60)
                
            def create_chips_button(): 
                product.add_chips(id.get(), name.get(), price.get(), quantity.get())                              

                added_user = Frame(new, width=250,height=200,bg="#000000")
                added_user.place(x=900, y=60)   
                Label(added_user,text="Chips Has Been Added",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=10)
                Label(added_user,text="Press Okey To Return Back To \n Chips Info",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=15,y=30)                             
                Button(added_user,text="Add Chips Again",command=record_of_chips,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

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

            Label(frame4,text="For Chips",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=90,y=10)
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
            Button(frame4,text="Add Chips",command=create_chips_button,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=90,y=160)

        def show_chips_record():
            try:
                records = product.query_all_chips()       
                listbox4.delete(0, END)

                for record in records:
                    listbox4.insert(END, record)

            except sqlite3.Error as e:
                print(e)

        def delete():
            clear = Frame(new, width=250,height=200,bg="#141414")
            clear.place(x=900, y=60)

            def delete_selected_user_record():
                try:
                    product.delete_chips(user_id)

                    selected_item = listbox4.get(ACTIVE)
                    user_id = selected_item[0]

                    show_chips_record()

                except sqlite3.Error as e:
                    print(e)

            Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
            Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

        Button(frame4, text="Create Record Of Chips",command=create_record_of_chips,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
        Button(frame4, text="Show Chips Records",command=show_chips_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=250,y=25)
        Button(frame4, text="Update Chips Record",command=update_record_of_chips,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=385,y=25)
        Button(frame4, text="Delete Chips Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=530,y=25)
  
#   buttons on left site bar
    Button(frame, text="Users",command=record_of_users,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=80)
    Button(frame, text="Cashes",command=record_of_cashes,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=140)
    Button(frame, text="Drinks",command=record_of_drinks,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=200)
    Button(frame, text="Biscuits",command=record_of_biscuits,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=260)
    Button(frame, text="Chocolates",command=record_of_chocolates,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=320)
    Button(frame, text="Chips",command=record_of_chips,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=380)
