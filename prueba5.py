import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# background="..." doesn't work...
ttk.Style().configure('black/black.TLabel', foreground='black', background='black')
ttk.Style().configure('black/black.TButton', foreground='black', background='black')

label = ttk.Label(root, text='I am a ttk.Label with text!', style='black/black.TLabel')
label.pack()

button = ttk.Button(root, text='Click Me!', style='black/black.TButton')
button.pack()

root.mainloop() 