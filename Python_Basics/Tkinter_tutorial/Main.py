from tkinter import *

root = Tk()
# creating a Label widget
mylabel= Label(root, text='Hello World')
mylabe2= Label(root,text='My Name is Subin Balachandran')
# showing it onto the sreen
mylabel.grid(row= 0, column= 0)
mylabe2.grid(row= 1, column= 0)


root.mainloop()