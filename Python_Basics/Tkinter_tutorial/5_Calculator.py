from tkinter import *
root =Tk()
root.title('Simple Calculator')
def button_click(number):
    #
    current_number= Display.get()
    Display.delete(0, END)
    Display.insert(0,str(current_number)+str(number))

Display =Entry(root, width= 50, borderwidth=5)
Display.grid(row=0, column= 0,padx=10,pady=10,columnspan=3)

# define Buttons
Button1= Button(root,text='1', padx=40, pady=20,command=lambda:button_click(1))
Button2= Button(root,text='2', padx=40, pady=20,command=lambda :button_click(2))
Button3= Button(root,text='3', padx=40, pady=20,command=lambda :button_click(3))
Button4= Button(root,text='4', padx=40, pady=20,command=lambda :button_click(4))
Button5= Button(root,text='5', padx=40, pady=20,command=lambda :button_click(5))
Button6= Button(root,text='6', padx=40, pady=20,command=lambda :button_click(6))
Button7= Button(root,text='7', padx=40, pady=20,command=lambda :button_click(7))
Button8= Button(root,text='8', padx=40, pady=20,command=lambda :button_click(8))
Button9= Button(root,text='9', padx=40, pady=20,command=lambda :button_click(9))
Button0= Button(root,text='0', padx=40, pady=20,command=lambda :button_click(0))
Button_add= Button(root,text='+', padx=40, pady=20,command=lambda :button_click())
Button_equal= Button(root,text='=', padx=93, pady=20,command=lambda :button_click())
Button_clear= Button(root,text='clear', padx=85, pady=20,command=lambda :button_click())
# put the buttons on screen
Button1.grid(row= 3, column=0 )
Button2.grid(row= 3, column= 1)
Button3.grid(row= 3, column= 2)
Button4.grid(row= 2, column= 0)
Button5.grid(row= 2, column= 1)
Button6.grid(row= 2, column= 2)
Button7.grid(row=1 , column= 0)
Button8.grid(row=1 , column=1 )
Button9.grid(row=1 , column=2 )

Button_clear.grid(row= 4, column=1,columnspan=2 )
Button0.grid(row= 4, column=0 )
Button_equal.grid(row= 5, column=1,columnspan=2 )
Button_add.grid(row= 5, column=0,)

root.mainloop()
