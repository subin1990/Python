from tkinter import *

root = Tk()

entry_1= Entry(root,width=45, bg='white', fg='black')
entry_1.pack()
entry_1.insert(0,'enter the name')

def Myclick():
    name= 'Hello '+entry_1.get()
    Label1= Label(root, text=name,font='Arial',fg='Blue')
    Label1.pack()

Mybutton= Button(root, text='Enter your name!!',padx=75, pady=5,bg='yellow',fg='red',command=Myclick) # state=DISABLED  means disabling the button
Mybutton.pack()


root.mainloop()