from tkinter import *

window=Tk()

def get_square():
    n=float(e1_value.get())
    squared=n*n
    t1.insert(END,squared)

b1=Button(window,text="Execute",command=get_square)
#b1=pack()
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=30)
t1.grid(row=0,column=3)

window.mainloop()
