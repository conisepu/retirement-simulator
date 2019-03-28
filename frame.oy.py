from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.resizable(width=False, height=False) 
window.title("Retirement Simulator")
 
window.geometry('720x540')
frame1=Frame(window, width=720, height=50, background="grey")
frame1.place(x=0, y=0)
frame2=Frame(window, width=720, height=10, background="grey")
frame2.place(x=0, y=300)
frame3=Frame(window, width=10, height=300, background="grey")
frame3.place(x=360, y=300)
frame4=Frame(window, width=720, height=20, background="grey")
frame4.place(x=0, y=520)
frame5=Frame(window, width=20, height=540, background="grey")
frame5.place(x=0, y=0)
frame6=Frame(window, width=20, height=540, background="grey")
frame6.place(x=700, y=0)

window.mainloop()