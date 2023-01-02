from tkinter import *
from tkinter import messagebox
main = Tk()
main.state("zoomed")


# this will add title
main.title("Vending Machine")

# this will create a label widget
l1 = Label(main, text = "Drinks")
l2 = Label(main, text = "Chocolate")
l3 = Label(main, text = "Chips")
l4 = Label(main, text = "Biscuits")

l5 = Label(main, text = "Drinks")
l6 = Label(main, text = "Chocolate")
l7 = Label(main, text = "Chips")
l8 = Label(main, text = "Biscuits")

l9 = Label(main, text = "Drinks")
l10 = Label(main, text = "Chocolate")
l11 = Label(main, text = "Chips")
l12 = Label(main, text = "Biscuits")

l13 = Label(main, text = "Drinks")
l14 = Label(main, text = "Chocolate")
l15 = Label(main, text = "Chips")
l16 = Label(main, text = "Biscuits")

# grid method to arrange labels in respective
# rows and columns as specified

l1.grid(row = 0, column = 1, pady = 10, padx = 10)
l2.grid(row = 1, column = 1, pady = 10, padx = 10)
l3.grid(row = 2, column = 1, pady = 10, padx = 10)
l4.grid(row = 3, column = 1, pady = 10, padx = 10)

l5.grid(row = 0, column = 2, pady = 10, padx = 10)
l6.grid(row = 1, column = 2, pady = 10, padx = 10)
l7.grid(row = 2, column = 2, pady = 10, padx = 10)
l8.grid(row = 3, column = 2, pady = 10, padx = 10)

l9.grid(row = 0, column = 3, pady = 10, padx = 10)
l10.grid(row = 1, column = 3, pady = 10, padx = 10)
l11.grid(row = 2, column = 3, pady = 10, padx = 10)
l12.grid(row = 3, column = 3, pady = 10, padx = 10)

l13.grid(row = 0, column = 4, pady = 10, padx = 10)
l14.grid(row = 1, column = 4, pady = 10, padx = 10)
l15.grid(row = 2, column = 4, pady = 10, padx = 10)
l16.grid(row = 3, column = 4, pady = 10, padx = 10)

main.mainloop()

