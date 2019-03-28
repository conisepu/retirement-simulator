from tkinter import *
from tkinter.ttk import Combobox

def clicked():
 	
 	res = txt.get()

 	txt2.configure(text= res)


 

window = Tk()
window.resizable(width=False, height=False) 
window.title("Retirement Simulator")
 
window.geometry('720x540')

lbl = Label(window, text=" ", font=("Arial Bold", 	17))
lbl.place(x=400, y=130)


txt = Entry(window,width=3)
txt.place(x=150, y=130)
txt2 = Entry(window,width=3)
txt2.place(x=200, y=130)


btnB= Button(window, text="Calcular", command=clicked)
btnB.place(x=500, y=425)
window.mainloop()