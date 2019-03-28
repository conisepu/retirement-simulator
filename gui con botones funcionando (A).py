from tkinter import *
from tkinter.ttk import Combobox

def clicked():
 	#sexo
    sexo=v0.get()
    #edad
    edadHoy=int(txt.get())
    mesHoy=cb2.get()
    #mes de nacimiento
    MesNacido=cb.get()
    #año actual
    añoHoy=int((txt2.get()))
    #mes actual
    mesHoy=(cb2.get())
    #fondo acumulado
    FondoAcumulado=int((txt3.get()))
    #sueldo actual
    sueldoHoy=int((txt4.get()))
    #fondo
    ###################RFondo=cb4.get()
    
    # A cotizacion mensual
    COTVa=float(txtA1.get())
    # B monto deseado jubilacion
    JubilacionDeseada=int((txtB1.get()))
    


    if mesHoy == "Enero":
    	mesHoy=1
    if MesNacido == "Enero":
    	MesNacido=1
    if mesHoy == "Febrero":
    	mesHoy=2
    if MesNacido == "Febrero":
    	MesNacido=2		
    if mesHoy == "Marzo":
    	mesHoy=3
    if MesNacido == "Marzo":
    	MesNacido=3
    if mesHoy == "Abril":
    	mesHoy=4
    if MesNacido == "Abril":
    	MesNacido=4
    if mesHoy == "Mayo":
    	mesHoy=5
    if MesNacido == "Mayo":
    	MesNacido=5	
    if mesHoy == "Junio":
    	mesHoy=6
    if MesNacido == "Junio":
    	MesNacido=6	
    if mesHoy == "Julio":
    	mesHoy=7
    if MesNacido == "Julio":
    	MesNacido=7	
    if mesHoy == "Agosto":
    	mesHoy=8
    if MesNacido == "Agosto":
    	MesNacido=8	
    if mesHoy == "Septiembre":
    	mesHoy=9
    if MesNacido == "Septiembre":
    	MesNacido=9	
    if mesHoy == "Octubre":
    	mesHoy=10
    if MesNacido == "Octubre":
    	MesNacido=10	
    if mesHoy == "Noviembre":
    	mesHoy=11
    if MesNacido == "Noviembre":
    	MesNacido=11	
    if mesHoy == "Diciembre":
    	mesHoy=12
    if MesNacido =="Diciembre":
    	MesNacido=12	

    MesNacido=int(MesNacido)
    mesHoy=int(mesHoy)	


    ####OPCION A
    
    COTVa=COTVa/100
    pensionXmes=(COTO+COTVa)*(sueldoHoy)

    if sexo==1:
    	AñoJub=(JHombre-int(edadHoy))+int(añoHoy)
    	MesesparaJub=12-int(mesHoy)+MesNacido+12*(JHombre-int(edadHoy)-2)

    if sexo==2:
    	AñoJub=(JMujer-int(edadHoy))+int(añoHoy)
    	MesesparaJub=12-int(mesHoy)+MesNacido+12*(JMujer-int(edadHoy)-2)

    pension=FondoAcumulado
    MesesparaJub=int(MesesparaJub)

    for i in range (MesesparaJub):
    	if (i+1)%12 != 0:
    		pension = pensionXmes+pension
    	elif (i+1)%12==0:
    		pension=pension+(RFondo/100)*(pension)

    if sexo==1:
    	pension=pension/(15*mesxaño)
    	ResA=int(pension)
    if sexo==2:
    	pension=pension/(25*mesxaño)
    	ResA=int(pension)

    print(ResA)
    print(ResB)
    txtA2.configure(text= ("$ " + str(ResA) +" pesos"))
    txtB2.configure(text= ResB)
 
# sexo=0
# mesHoy=0
# añoHoy=0
# edadHoy=0
# MesNacido=0
# FondoAcumulado=0
# sueldoHoy=0
# RFondo=0
# COTVa=0
# JubilacionDeseada=0
# ResA=0
ResB=0

RFondo=float(5.42)
JHombre=int(65)
JMujer=int(60)
COTO=float(0.1)
mesxaño=int(12)
vidaH=int(80)
vidaM=int(85)


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

data=("Enero", "Febrero", "Marzo", "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
cb=Combobox(window,width=10, values=data)
cb.place(x=210, y=175)

cb2=Combobox(window,width=8, values=data)
cb2.place(x=140, y=255)

data2=("Capital", "Cuprum", "Habitat", "Modelo","PlanVital","ProVida","Sistema")
cb3=Combobox(window,width=9, values=data2)
cb3.place(x=430, y=175)

data3=("A", "B", "C", "D","E")
cb4=Combobox(window,width=3, values=data3)
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
lbl = Label(window, text="Ingrese porcentaje de APV mensual", font=("Arial ", 14))
lbl.place(x=25, y=350)
lbl = Label(window, text="Proyección futura mensual", font=("Arial ", 14))
lbl.place(x=25, y=470)

txtA1 = Entry(window,width=8)
txtA1.place(x=152, y=380)
txtA2 = Label(window,width=15, text=" ", font=("Arial Bold", 	16))
txtA2.place(x=205, y=470)

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




############# codigo de formulas



 
window.mainloop()