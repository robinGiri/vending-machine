from tkinter import *
from PIL import Image,ImageTk

def cash(main, vendingState):

    def add_currency(amount):
        '''
        @param: amount
        if user is not login sent error 
        if login and clicked on any cash load the amount 
        add clicked amount in vendingState["input_currency"]
        '''

        if vendingState["is_authenticated"] == False :
            Label(frame2,text="Please Login", font="bold",fg="#DC372F", bg="#6A6161").place(x=10,y=10)
            return

        else:
            vendingState["input_currency"] += amount
            Label(frame2,text="You have added Rs. {}".format(amount), font="bold",fg="#00FF7F", bg="#6A6161").place(x=10,y=10)
            Label(frame2, text="Your Current Amount is: {}".format(vendingState["input_currency"]), font="bold",fg="#00FF7F", bg="#6A6161").place(x=10,y=30)

    frame = Frame(main, width=600,height=427,bg="#000000")
    frame.place(x=765, y=350)

    def ten():
        '''
        @params: no
        added ten Rupees image in screen
        if clicked call add currenty function and add 10 on vendingState input_currency state
        '''

        add_currency(10)
        my_ten.config(image=new_pic21,bg="#000000",border=0,borderwidth=0)
    image21 = Image.open("public/Ten.png")
    resized = image21.resize((129,68), Image.Resampling.LANCZOS)
    new_pic21 = ImageTk.PhotoImage(resized)
    ten_img = Label(frame, image=new_pic21,borderwidth=0,border=0,bg="#000000")
    ten_img.place(x=350,y=30)
    ten_btn = Button(frame, image=new_pic21,command=ten,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    ten_btn.place(x=350,y=30)
    my_ten = Label(frame,image="",bg="#000000")
    
    def Twenty():
        '''
        @params: no
        added Twenty Rupees image in screen
        if clicked call add currenty function and add 20 on vendingState input_currency state
        '''

        add_currency(20)
        my_Twenty.config(image=new_pic22,bg="#000000",border=0,borderwidth=0)
    image22 = Image.open("public/Twenty.png")
    resized = image22.resize((165,80), Image.Resampling.LANCZOS)
    new_pic22 = ImageTk.PhotoImage(resized)
    Twenty_img = Label(frame, image=new_pic22,borderwidth=0,border=0,bg="#000000")
    Twenty_img.place(x=330,y=115)
    Twenty_btn = Button(frame, image=new_pic22,command=Twenty,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Twenty_btn.place(x=330,y=115)
    my_Twenty = Label(frame,image="",bg="#000000")
    
    def Fifty():
        '''
        @params: no
        added Fifty Rupees image in screen
        if clicked call add currenty function and add 50 on vendingState input_currency state
        '''

        add_currency(50)
        my_Fifty.config(image=new_pic23,bg="#000000",border=0,borderwidth=0)
    image23 = Image.open("public/Fifty.png")
    resized = image23.resize((189,92), Image.Resampling.LANCZOS)
    new_pic23 = ImageTk.PhotoImage(resized)
    Fifty_img = Label(frame, image=new_pic23,borderwidth=0,border=0,bg="#000000")
    Fifty_img.place(x=320,y=210)
    Fifty_btn = Button(frame, image=new_pic23,command=Fifty,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Fifty_btn.place(x=320,y=210)
    my_Fifty = Label(frame,image="",bg="#000000")
    
    def Hundred():
        '''
        @params: no
        added Hundred Rupees image in screen
        if clicked call add currenty function and add 100 on vendingState input_currency state
        '''

        add_currency(100)
        my_Hundred.config(image=new_pic24,bg="#000000",border=0,borderwidth=0)
    image2new_pic24 = Image.open("public/Hundred.png")
    resized = image2new_pic24.resize((221,92), Image.Resampling.LANCZOS)
    new_pic24 = ImageTk.PhotoImage(resized)
    Hundred_img = Label(frame, image=new_pic24,borderwidth=0,border=0,bg="#000000")
    Hundred_img.place(x=305,y=317)
    Hundred_btn = Button(frame, image=new_pic24,command=Hundred,border=0,borderwidth=0,bg="#000000",activebackground="#000000")
    Hundred_btn.place(x=305,y=317)
    my_Hundred = Label(frame,image="",bg="#000000")

    frame1 = Frame(frame, width=227,height=387,bg="#D9D9D9")
    frame1.place(x=30, y=20)

    Label(frame,text="Cash Output",font="bold",bg="#D9D9D9").place(x=60,y=50)

    frame2 = Frame(frame, width=207,height=99,bg="#6A6161")
    frame2.place(x=40, y=100)

    frame = Frame(frame, width=174,height=10,bg="#6A6161")
    frame.place(x=55, y=340)
