from tkinter import *
from tkinter.ttk import Combobox

def clicked():
 	
 	res = v0.get()
 	
 
 	lbl.configure(text= res)
 	
 	
	


window = Tk()
window.resizable(width=False, height=False) 
window.title("Retirement Simulator")
window.geometry('720x540')
v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="Masculino", variable=v0,value="aaa")
r2=Radiobutton(window, text="Femenino", variable=v0,value="bbb")
r1.place(x=140,y=95)
r2.place(x=240, y=95)

lbl = Label(window, text=" ", font=("Arial Bold", 	17))
lbl.place(x=400, y=130)
lbl2 = Label(window, text=" ", font=("Arial Bold", 	17))
lbl2.place(x=400, y=170)
btnB= Button(window, text="Calcular", command=clicked)
btnB.place(x=500, y=425)



window.mainloop()