from tkinter import *

root = Tk()

def Myclick():

    Label1= Label(root, text='Look i clicked a Button',font='Arial',fg='Blue')
    Label1.pack()

Mybutton= Button(root, text='Click me!!',padx=100, pady=25,bg='yellow',fg='red',command=Myclick) # state=DISABLED  means disabling the button
Mybutton.pack()


root.mainloop()