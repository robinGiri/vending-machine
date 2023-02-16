from tkinter import *
import sqlite3
import auth

def record_of_users(main):
    '''
    @params: main as param
    added record button
    if clicked users window will be displayed
    '''

    frame1_1_1 = Frame(main, width=1700,height=800,bg="#000000")
    frame1_1_1.place(x=90, y=1)
    listbox1_1_1 = Listbox(main, width=130, height=35,bg="#6A6161",fg="#FFFFFF")
    listbox1_1_1.place(x=90,y=60)

    def show_user_record():
        '''
        @params: no
        added record button
        if clicked record of user will show up
        '''

        try:
            records = auth.query_all_users()       
            listbox1_1_1.delete(0, END)
            for record in records:
                listbox1_1_1.insert(END, record)

        except sqlite3.Error as e:
            print(e)

    def delete():
        '''
        @params: no
        added delete button
        if clicked it will delete record
        '''
        
        clear = Frame(main, width=250,height=200,bg="#141414")
        clear.place(x=900, y=60)

        def delete_selected_user_record():
            try:
                selected_item = listbox1_1_1.get(ACTIVE)
                user_id = selected_item[0]
                auth.delete_user(user_id)     

                show_user_record()

            except sqlite3.Error as e:
                print(e)

        Label(clear,text="Delete The Selected Record",font=("Arial",10,"bold"),fg="white",bg="#000000").place(x=40,y=20)
        Button(clear, text="Delete Record",command=delete_selected_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=85,y=60)

    Button(frame1_1_1, text="Show Users Records",command=show_user_record,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=100,y=25)
    Button(frame1_1_1, text="Delete Users Record",command=delete,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=530,y=25)
