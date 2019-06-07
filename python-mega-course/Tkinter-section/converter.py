from tkinter import *

window=Tk()
def converter_fun():
    kg=float(e1_value.get())
    grams=kg*1000
    pounds=kg*2.2046
    ounces=kg*35.274
    t1.delete("1.0",END)
    t1.insert(END,grams)
    t2.delete("1.0",END)
    t2.insert(END,pounds)
    t3.delete("1.0",END)
    t3.insert(END,ounces)
e2=Label(window,text="kg")
b1=Button(window,text="Convert",command=converter_fun)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
t1=Text(window,height=1,width=20)
t2=Text(window,height=1,width=20)
t3=Text(window,height=1,width=20)

b1.grid(row=0,column=2)
e1.grid(row=0,column=1)
e2.grid(row=0,column=0)
t1.grid(row=1,column=0)
t2.grid(row=1,column=1)
t3.grid(row=1,column=2)
window.mainloop()
