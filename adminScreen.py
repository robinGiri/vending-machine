from tkinter import *
import admin_user
import admin_cashes
import admin_product

def newWindow(new, vendingState):
    '''
    @params: main
    added a new window
    if clicked admin pannel will show up
    '''

    new = Toplevel(new)
    new.state("zoomed")
    new.title("Vending Admin Pannel")

    frame = Frame(new, width=1700,height=800,bg="#000000")
    frame.place(x=1, y=1)
    listbox = Listbox(new, width=130, height=35,bg="#6A6161",fg="#FFFFFF")
    listbox.place(x=90,y=60)

    def record_of_users():
        '''
        @params: no
        added record button
        if clicked users window will be displayed
        '''
        admin_user.record_of_users(new)
    
    def record_of_cashes():
        '''
        @params: no
        added record button
        if clicked cash window will be displayed
        '''

        admin_cashes.record_of_cashes(new, vendingState)        

    def record_of_drinks():
        '''
        @params: no
        added drinks button
        if clicked drinks window appears
        '''
        admin_product.record_of_product(new, "Drinks")

    def record_of_biscuits():
        '''
        @params: no
        added record button
        if clicked biscuits window appear
        '''
        admin_product.record_of_product(new, "Biscuits")

    def record_of_chocolates(): 
        '''
        @params: no
        added chocolate button
        if clicked chocolate window appears
        '''  
        print("chocolate")
        admin_product.record_of_product(new, "Chocolate")

    def record_of_chips():
        '''
        @params: no
        added record button
        if clicked chips window will be displayed
        '''
        admin_product.record_of_product(new, "Chips")

#   buttons on left site bar
    Button(frame, text="Users",command=record_of_users,padx=17,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=80)
    Button(frame, text="Cashes",command=record_of_cashes,padx=13,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=140)
    Button(frame, text="Drinks",command=record_of_drinks,padx=15,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=200)
    Button(frame, text="Biscuits",command=record_of_biscuits,padx=11,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=260)
    Button(frame, text="Chocolates",command=record_of_chocolates,padx=2,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=320)
    Button(frame, text="Chips",command=record_of_chips,padx=16,border=4,bg="#00FF7F",pady=2,activebackground="#000000",activeforeground="#FFFFFF").place(x=10,y=380)
