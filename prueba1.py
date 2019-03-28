from tkinter import *

window= Tk()

l1=Label(window, text="prueba1")
l1.grid(row=0, column=0)


l1=Label(window, text="prueba2")
l1.grid(row=0, column=2)

l1=Label(window, text="prueba3")
l1.grid(row=1, column=0)

l1=Label(window, text="prueba4")
l1.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window,textvariable=prueba2_text)
e1.grid(row=0,column=1)	

title_text=StringVar()
e2=Entry(window,textvariable=prueba2_text)
e2.grid(row=0,column=1)

title_text=StringVar()
e3=Entry(window,textvariable=prueba2_text)
e3.grid(row=0,column=1)

title_text=StringVar()
e4=Entry(window,textvariable=prueba2_text)
e4.grid(row=0,column=1)


window.mainloop()
