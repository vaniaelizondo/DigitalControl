from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

###########################################################
# Vania Alejandra Elizondo Martínez
# A01039093
# Control Computarizado
###########################################################

################# Declaracion de ambiente #################
# Variables globales
c = [0]*1000
m = [0]*1000
k = 0
i = 0
t = 0.5

# Leer archivo entrada
entrada = open('entrada.txt')
for x in entrada:
    m[i] = float(x)
    i += 1

################# Definicion de funciones #################
# Funcion que grafica
def startGraphs():
    # Variables inciales
    global c
    global k
    global t

    

################# Definicion de ambiente grafico #################
# Funcion que abre interfaz grafica 
mainGUI = Tk()
mainGUI.title("Planta con Modelo ARX")

# Frames
frameTop = Frame(mainGUI)
frameMiddle0 = Frame(mainGUI)
frameMiddle1 = Frame(mainGUI)
frameBottom = Frame(mainGUI)

frameTop.pack(side=TOP)
frameMiddle0.pack(side=TOP)
frameMiddle1.pack(side=TOP)
frameBottom.pack(side=BOTTOM)

frameVars1 = Frame(frameTop)
frameEntries1 = Frame(frameTop)
frameVars2 = Frame(frameTop)
frameEntries2 = Frame(frameTop)
frameVars3 = Frame(frameTop)
frameEntries3 = Frame(frameTop)

frameVars1.pack(side=LEFT)
frameEntries1.pack(side=LEFT)
frameVars2.pack(side=LEFT)
frameEntries2.pack(side=LEFT)
frameVars3.pack(side=LEFT)
frameEntries3.pack(side=LEFT)

# Labels
la1 = Label(frameVars1, text='a1') 
la2 = Label(frameVars1, text='a2')
la3 = Label(frameVars1, text='a3')
la4 = Label(frameVars1, text='a4')
lb0 = Label(frameVars2, text='b0')
lb1 = Label(frameVars2, text='b1')
lb2 = Label(frameVars2, text='b2')
lb3 = Label(frameVars2, text='b3')
lb4 = Label(frameVars2, text='b4')
ld = Label(frameVars3, text='d')
le = Label(frameMiddle0, text='')

la1.pack()
la2.pack()
la3.pack()
la4.pack()
lb0.pack()
lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()
ld.pack()

# Entradas de texto
ea1 = Entry(frameEntries1) 
ea2 = Entry(frameEntries1) 
ea3 = Entry(frameEntries1) 
ea4 = Entry(frameEntries1) 
eb0 = Entry(frameEntries2) 
eb1 = Entry(frameEntries2) 
eb2 = Entry(frameEntries2) 
eb3 = Entry(frameEntries2) 
eb4 = Entry(frameEntries2) 
ed = Entry(frameEntries3) 
eP = Entry(frameEntries3) 

ea1.pack()
ea2.pack()
ea3.pack()
ea4.pack()
eb0.pack()
eb1.pack()
eb2.pack()
eb3.pack()
eb4.pack()
ed.pack()
eP.pack()

# Boton de seleccion
aplicarP = BooleanVar()
bp = Checkbutton(frameVars3, text='Aplicar Perturbación', var=aplicarP)
bp.pack()

# Botones
bComenzar = Button(frameBottom, text='Comenzar programa', command=startGraphs)
bTerminar = Button(frameBottom, text='Terminar programa', command=mainGUI.destroy)
bComenzar.pack(side=TOP)
bTerminar.pack(side=BOTTOM)

# Actualizar entradas de coeficientes
try: 
    a1 = float(ea1.get())
except:
    a1 = 0
try:
    a2 = float(ea2.get())
except:
    a2 = 0
try:
    a3 = float(ea3.get())
except:
    a3 = 0
try:
    a4 = float(ea4.get())
except:
    a4 = 0
try:
    b0 = float(eb0.get())
except:
    b0 = 0
try:
    b1 = float(eb1.get())
except:
    b1 = 0
try:
    b2 = float(eb2.get())
except:
    b2 = 0
try:
    b3 = float(eb3.get())
except:
    b3 = 0
try:
    b4 = float(eb4.get())
except:
    b4 = 0
try:
    d = int(ed.get())
except:
    d = 0
try:
    P = float(eP.get())
except:
    P = 0

# Figura dentro de GUI
fig0 = Figure(figsize=(6,2.5))
fig1 = Figure(figsize=(6,2.5))

ax0 = fig0.add_subplot(111)
ax1 = fig1.add_subplot(111)

# plt.ion()
# plt.show()
# fig, axs = plt.subplots(2, sharex=True)

# Grafica con perturbacion
if (aplicarP.get()):
    c[k] = a1*c[k-1] + a2*c[k-2] + a3*c[k-3] + a4*c[k-4] + b0*m[k-d] + b1*m[k-1-d] + b2*m[k-2-d] + b3*m[k-3-d] + b4*m[k-4-d] + P
    P = float(eP.get())
    
# Grafica sin perturbacion
else:
    c[k] = a1*c[k-1] + a2*c[k-2] + a3*c[k-3] + a4*c[k-4] + b0*m[k-d] + b1*m[k-1-d] + b2*m[k-2-d] + b3*m[k-3-d] + b4*m[k-4-d]
    P = 0

ax0.plot(k*t, c[k], 'b.')
ax0.set_title('Salida c(k)')
ax0.set_xlabel('Tiempo')
ax0.set_ylabel('Amplitud')
ax1.plot(k*t, m[k], 'g.', k*t, P, 'r+')
ax1.set_title('Entrada m(k) y Perturbación')
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Amplitud')
ax1.legend(['m[k]', 'P'], loc='upper right')
print('c[{}]={}, m[{}]={}, P: {} clicked: {}'. format(k, c[k], k, m[k], P, aplicarP.get()))
# plt.pause(1)
k += 1

# Canvas and toolbar
canvas0 = FigureCanvasTkAgg(fig0, master=frameMiddle0)
canvas0.get_tk_widget().pack(side=TOP)
canvas0.draw()

toolbar0 = NavigationToolbar2Tk(canvas0, frameMiddle0)
toolbar0.pack(side=TOP)
toolbar0.update()

le.pack(side=BOTTOM)

canvas1 = FigureCanvasTkAgg(fig1, master=frameMiddle1)
canvas1.get_tk_widget().pack(side=TOP)
canvas1.draw()

toolbar1 = NavigationToolbar2Tk(canvas1, frameMiddle1)
toolbar1.pack(side=TOP)
toolbar1.update()

# Funcion recursiva
mainGUI.mainloop()

# Terminacion de programa
entrada.close()