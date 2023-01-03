from tkinter import *
import seed

main = Tk()
main.state("zoomed")


# this will add title
main.title("Vending Machine")

# this will create a label widget
space1 = Label(main).grid(row=0,column=0,padx=50,pady=50)
space2 = Label(main).grid(row=1,column=1,padx=50,pady=50)

i = 0
while i < len(seed.items):
    Label(main, text= list(seed.items)[i]).grid(row=i*2+2,column=2,padx=5)
    for j,options in enumerate(seed.items[list(seed.items)[i]]):
        Label(main,text=options).grid(row=i*2+2,column=j+3,padx=5)
    i +=1

main.mainloop()

