from tkinter import *
from tkinter.ttk import Combobox

def clicked():
 	
 	res =  cb.get()
 	
 
 	lbl.configure(text= res)
 	
 	
	


window = Tk()
window.resizable(width=False, height=False) 
window.title("Retirement Simulator")
window.geometry('720x540')


data=("Enero", "Febrero", "Marzo", "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
cb=Combobox(window,width=8, values=data)
cb.place(x=210, y=175)

lbl = Label(window, text="nada aun ", font=("Arial Bold", 	17))
lbl.place(x=400, y=130)

btnB= Button(window, text="Calcular", command=clicked)
btnB.place(x=500, y=425)



window.mainloop()