sexo=input("sexo: ")
mesHoy=int(input("mes hoy: "))
añoHoy=int(input("año actual: "))
edadHoy=int(input("edad hoy: "))
MesNacido=int(input("mes que nacio: "))
FondoAcumulado=int(input("Fondos acumulado hoy: "))
sueldoHoy=int(input("sueldo: "))
RfondosAFP=input("afp a la que perteneces: ")
RFondo=float(input("cual fondo eres: "))### es valor de rantabilidad como numero NO como porcentaje


#------DATOS------
JHombre=65
JMujer=60
COTO=0.1
mesxaño=12
vidaH=80
vidaM=85


# TECLA A
COTVa=float(input("porcentaje de APV: ")) #apv en boton A
COTVa=COTVa/100
pensionXmes=(COTO+COTVa)*int(sueldoHoy)

if sexo=="hombre":
	AñoJub=(JHombre-int(edadHoy))+int(añoHoy)
	MesesparaJub=12-int(mesHoy)+MesNacido+12*(JHombre-int(edadHoy)-2)


if sexo=="mujer":
	AñoJub=(JMujer-int(edadHoy))+int(añoHoy)
	MesesparaJub=12-int(mesHoy)+MesNacido+12*(JMujer-int(edadHoy)-2)


pension=FondoAcumulado
for i in range (MesesparaJub):
	
	if (i+1)%12 != 0:
		
		pension = pensionXmes+pension
		
	elif (i+1)%12==0:
		
		pension=pension+RFondo*(pension)
		
	

if sexo=="hombre":
	pension=pension/(15*mesxaño)
	print(int(pension))

if sexo=="mujer":
	pension=pension/(25*mesxaño)
	print(int(pension))