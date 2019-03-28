
from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Welcome to LikeGeeks app")
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Hello", font=("Arial Bold", 50))
lbl2.grid(column=1, row=1)
window.geometry('350x200')

btn = Button(window, text="Click Me", highlightbackground='#3E4149')
btn.grid(column=2, row=2)
	
def clicked():
 
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)

 
window.mainloop()