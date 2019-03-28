from tkinter import *
from tkinter.ttk import Combobox

def clicked():
 
    res = "Acabas de escribir  " + txt.get()
 
    lbl.configure(text= res)
 

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

lbl = Label(window, text="Ingrese su información", font=("Arial Bold", 20))
lbl.place(x=25, y=60)

lbl = Label(window, text=" Sexo",font=("Arial ", 20))
lbl.place(x=30, y=90)
lbl = Label(window, text=" Edad actual",font=("Arial ", 20))
lbl.place(x=30, y=130)
lbl = Label(window, text=" Mes de nacimiento",font=("Arial ", 20))
lbl.place(x=30, y=170)
lbl = Label(window, text=" Año actual ",font=("Arial ", 20))
lbl.place(x=30, y=210)
lbl = Label(window, text=" Mes actual ",font=("Arial ", 20))
lbl.place(x=30, y=250)

lbl = Label(window, text=" Fondo acumulado",font=("Arial ", 20))
lbl.place(x=380, y=90)
lbl = Label(window, text=" Sueldo actual",font=("Arial ", 20))
lbl.place(x=380, y=130)
lbl = Label(window, text=" AFP",font=("Arial ", 20))
lbl.place(x=380, y=170)
lbl = Label(window, text=" Fondo ",font=("Arial ", 20))
lbl.place(x=380, y=210)

#OPCIONES BOTONES CIRCULARES
v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="Masculino", variable=v0,value=1)
r2=Radiobutton(window, text="Femenino", variable=v0,value=2)
r1.place(x=140,y=95)
r2.place(x=240, y=95)

#OPCIONES LISTA
var = StringVar()
var.set("one")
data=("Enero", "Febrero", "Marzo", "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
cb=Combobox(window,width=8, values=data)
cb.place(x=210, y=175)

var2 = StringVar()
var2.set("two")
data2=("Enero", "Febrero", "Marzo", "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
cb2=Combobox(window,width=8, values=data2)
cb2.place(x=140, y=255)

var3 = StringVar()
var3.set("tres")
data3=("Capital", "Cuprum", "Habitat", "Modelo","PlanVital","ProVida","Sistema")
cb3=Combobox(window,width=5, values=data3)
cb3.place(x=430, y=175)

var4 = StringVar()
var4.set("cuatro")
data4=("A", "B", "C", "D","E")
cb4=Combobox(window,width=3, values=data4)
cb4.place(x=450, y=215)

#ENTRADA TEXTO
txt = Entry(window,width=3)
txt.place(x=150, y=130)

txt2 = Entry(window,width=5)
txt2.place(x=140, y=210)

txt3 = Entry(window,width=11)
txt3.place(x=550, y=90)

txt4 = Entry(window,width=8)
txt4.place(x=530, y=130)

#CUADRO A

lbl = Label(window, text="Calcular proyección de pensión futura", font=("Arial Bold", 17))
lbl.place(x=25, y=315)
lbl = Label(window, text="Ingrese monto de cotización voluntaria mensual", font=("Arial ", 14))
lbl.place(x=25, y=350)
lbl = Label(window, text="Proyección futura mensual", font=("Arial ", 14))
lbl.place(x=25, y=470)

txtA1 = Entry(window,width=8)
txtA1.place(x=152, y=380)
txtA2 = Entry(window,width=8)
txtA2.place(x=210, y=470)

btnA = Button(window, text="Calcular", command=clicked)
btnA.place(x=165, y=425)

#CUADRO B

lbl = Label(window, text="Calcular monto necesario de APV ", font=("Arial Bold", 	17))
lbl.place(x=397, y=315)
lbl = Label(window, text="para una pensión deseada mensual", font=("Arial Bold", 17))
lbl.place(x=390, y=340)
lbl = Label(window, text="Ingrese monto deseado", font=("Arial ", 14))
lbl.place(x=380, y=380)
lbl = Label(window, text="Monto mensual de APV necesario", font=("Arial ", 14))
lbl.place(x=380, y=470)

txtB1 = Entry(window,width=8)
txtB1.place(x=550, y=380)
txtB2 = Entry(window,width=8)
txtB2.place(x=605, y=470)

btnB= Button(window, text="Calcular", command=clicked)
btnB.place(x=500, y=425)
 
window.mainloop()