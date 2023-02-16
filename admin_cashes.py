from tkinter import *
import sqlite3
import cash

def record_of_cashes(main):
    '''
    @params: main as param
    added record button
    if clicked cash window will be displayed
    '''

    frame1_1 = Frame(main, width=1700,height=800,bg="#000000")
    frame1_1.place(x=90, y=1)
    listbox1_1 = Listbox(main, width=130, height=35,bg="#6A6161",fg="#FFFFFF")
    listbox1_1.place(x=90,y=60)

    def update_record_of_cashes():
        '''
        @params: no
        added update button
        if clicked update form appears
        '''

        add_user1 = Frame(main, width=250,height=200,bg="#141414")
        add_user1.place(x=900, y=60)

        def create_cash_button():                                
            '''
            @params: no
            added create button
            if clicked create cash in DB
            '''

            cash.add_cash(ID.get(), Value.get(), Quantity.get())                

            added_user = Frame(main, width=250,height=200,bg="#000000")
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
        '''
        @params: no
        added create button
        if clicked create form appears
        '''

        add_user1 = Frame(main, width=250,height=200,bg="#141414")
        add_user1.place(x=900, y=60)
            
        def create_cash_button():                                 
            
            cash.add_cash(ID.get(), Value.get(), Quantity.get())                

            added_user = Frame(main, width=250,height=200,bg="#000000")
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
        '''
        @params: no
        added show record button
        if clicked it will show records of cashes
        '''
        try:
            records = cash.query_all_cashes()
            listbox1_1.delete(0, END)

            for record in records:
                listbox1_1.insert(END, record)
                
        except sqlite3.Error as e:
            print(e)


    def delete():
        '''
        @params: no
        added delete button
        if clicked delete the records
        '''    

        clear = Frame(main, width=250,height=200,bg="#141414")
        clear.place(x=900, y=60)

        def delete_selected_user_record():
            try:
                selected_item = listbox1_1.get(ACTIVE)
                user_id = selected_item[0]
                cash.delete_cash(user_id)     

                show_cash_record()

            except sqlite3.Error as e:
                print(e)

        Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
        Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

    Button(frame1_1, text="Create Record Of Cashes",command=create_record_of_cashes,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=95,y=25)        
    Button(frame1_1, text="Show Cashes Records",command=show_cash_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=255,y=25)
    Button(frame1_1, text="Update Cashes Record",command=update_record_of_cashes,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=398,y=25)
    Button(frame1_1, text="Delete Cashes Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=547,y=25)
