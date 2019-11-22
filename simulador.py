from tkinter import *
import matplotlib.pyplot as plt

###########################################################
# Vania Alejandra Elizondo Martínez
# A01039093
# Control Computarizado
###########################################################

################# Declaracion de ambiente #################
# Variables globales
m = []
c = []
k = 0
i = 0
t = 0.5
c1 = 0
c2 = 0
c3 = 0
c4 = 0
m0 = 0
m1 = 0
m2 = 0
m3 = 0
m4 = 0

# Leer archivo entrada
entrada = open("entrada.txt")
for x in entrada:
    m.append(float(x))
    i += 1
entrada.close()

################# Definicion de funciones #################
# Funcion que grafica
def startGraphs():
    global mainGUI
    global fig, axs
    global c, m, k, i, t
    global c1, c2, c3, c4
    global m0, m1, m2, m3, m4
    global ea1, ea2, ea3, ea4
    global eb0, eb1, eb2, eb3, eb4
    global ed, eP, aplicarP

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

# Validar indices
    try:
        m[k]
    except IndexError:
        m.append(m[k-1])
    if ((k-1) < 0):
        c1 = 0
    else:
        c1 = c[k-1]
    if ((k-2) < 0):
        c2 = 0
    else:
        c2 = c[k-2]
    if ((k-3) < 0):
        c3 = 0
    else:
        c3 = c[k-3]
    if ((k-4) < 0):
        c4 = 0
    else:
        c4 = c[k-4]
    if ((k-d) < 0):
        m0 = 0
    else:
        m0 = m[k-d]
    if ((k-1-d) < 0):
        m1 = 0
    else:
        m1 = m[k-1-d]
    if ((k-2-d) < 0):
        m2 = 0
    else:
        m2 = m[k-2-d]
    if ((k-3-d) < 0):
        m3 = 0
    else:
        m3 = m[k-3-d]
    if ((k-4-d) < 0):
        m4 = 0
    else:
        m4 = m[k-4-d]
    if (aplicarP.get()):
        try:
            P = float(eP.get())
        except:
            P = 0
    else:
        P = 0

# Graficar
    c.append(a1*c1 + a2*c2 + a3*c3 + a4*c4 + b0*m0 + b1*m1 + b2*m2 + b3*m3 + b4*m4 + P)
    axs[0].plot(k*t, c[k], 'b.')
    axs[1].plot(k*t, m[k], 'g.', k*t, P, 'r+')
    axs[1].legend(['m[k]', 'P'], loc='upper right')
    print('a1: {} a2: {} a3: {} a4: {} '.format(a1,a2,a3,a4))
    print('b0: {} b1: {} b2: {} b3: {} b4: {} '.format(b0,b1,b2,b3,b4))
    print('c1: {} c2: {} c3: {} c4: {} '.format(c1,c2,c3,c4))
    print('m0: {} m1: {} m2: {} m3: {} m4: {} '.format(m0,m1,m2,m3,m4))
    print('d: {} P: {}'.format(d,P))
    print('c[{}]={}, m[{}]={}, clicked: {}\n'. format(k, c[k], k, m[k], aplicarP.get()))
    plt.pause(0.01)
    k += 1
    mainGUI.after(1000, startGraphs)

################# Definicion de ambiente grafico  #################
mainGUI = Tk()
mainGUI.title("Planta con Modelo ARX")

# Labels
Label(mainGUI, text='').grid(row=0) 
Label(mainGUI, text='a1').grid(row=1) 
Label(mainGUI, text='a2').grid(row=2) 
Label(mainGUI, text='a3').grid(row=3) 
Label(mainGUI, text='a4').grid(row=4) 
Label(mainGUI, text='b0').grid(row=1, column=2) 
Label(mainGUI, text='b1').grid(row=2, column=2) 
Label(mainGUI, text='b2').grid(row=3, column=2) 
Label(mainGUI, text='b3').grid(row=4, column=2) 
Label(mainGUI, text='b4').grid(row=5, column=2) 
Label(mainGUI, text='d').grid(row=1, column=4) 
Label(mainGUI, text='').grid(row=6) 
Label(mainGUI, text='').grid(row=8) 
Label(mainGUI, text='').grid(row=10) 

# Entradas de texto
ea1 = Entry(mainGUI) 
ea2 = Entry(mainGUI) 
ea3 = Entry(mainGUI) 
ea4 = Entry(mainGUI) 
eb0 = Entry(mainGUI) 
eb1 = Entry(mainGUI) 
eb2 = Entry(mainGUI) 
eb3 = Entry(mainGUI) 
eb4 = Entry(mainGUI) 
ed = Entry(mainGUI) 
eP = Entry(mainGUI) 

# Configuracion entradas de texto
ea1.grid(row=1, column=1) 
ea2.grid(row=2, column=1)
ea3.grid(row=3, column=1)
ea4.grid(row=4, column=1)
eb0.grid(row=1, column=3) 
eb1.grid(row=2, column=3) 
eb2.grid(row=3, column=3)
eb3.grid(row=4, column=3)
eb4.grid(row=5, column=3)
ed.grid(row=1, column=5)
eP.grid(row=2, column=5)

# Boton de seleccion
aplicarP = BooleanVar()
bp = Checkbutton(mainGUI, text='Aplicar Perturbación', var=aplicarP)
bp.grid(row=2, column=4)

# Botones
Button(mainGUI, text='Comenzar programa', command=startGraphs).grid(row=7, column=3)
Button(mainGUI, text='Terminar programa', command=mainGUI.destroy).grid(row=9, column=3)

# Creacion de graficas interactivas
plt.ion()
plt.show()
fig, axs = plt.subplots(2, sharex=True)
axs[0].set_title('Salida c(k)')
axs[0].set_ylabel('Amplitud')
axs[1].set_title('Entrada m(k) y Perturbación')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Amplitud')

# Funcion recursiva del ambiente grafico
mainGUI.mainloop()
