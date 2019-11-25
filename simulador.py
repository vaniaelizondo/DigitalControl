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
    global eA1, eA2, eA3, eA4
    global eB0, eB1, eB2, eB3, eB4
    global eD, ePE, ePS, aplicarPE, aplicarPS

# Actualizar entradas de coeficientes
    try: 
        a1 = float(eA1.get())
    except:
        a1 = 0
    try:
        a2 = float(eA2.get())
    except:
        a2 = 0
    try:
        a3 = float(eA3.get())
    except:
        a3 = 0
    try:
        a4 = float(eA4.get())
    except:
        a4 = 0
    try:
        b0 = float(eB0.get())
    except:
        b0 = 0
    try:
        b1 = float(eB1.get())
    except:
        b1 = 0
    try:
        b2 = float(eB2.get())
    except:
        b2 = 0
    try:
        b3 = float(eB3.get())
    except:
        b3 = 0
    try:
        b4 = float(eB4.get())
    except:
        b4 = 0
    try:
        d = int(eD.get())
    except:
        d = 0
    try:
        PE = float(ePE.get())
    except:
        PE = 0
    try:
        PS = float(ePS.get())
    except:
        PS = 0

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
    if (aplicarPS.get()):
        try:
            PS = float(ePS.get())
        except:
            PS = 0
    else:
        PS = 0

# Graficar
    c.append(a1*c1 + a2*c2 + a3*c3 + a4*c4 + b0*m0 + b1*m1 + b2*m2 + b3*m3 + b4*m4 + PS)
    axs[0].plot(k*t, c[k], 'b.')
    axs[1].plot(k*t, m[k], 'gs', k*t, PE, 'rd', k*t, PS, 'c.')
    axs[1].legend(['m[k]', 'Pert. Entrada', 'Pert. Salida'], loc='upper right')
    print('a1: {} a2: {} a3: {} a4: {} '.format(a1,a2,a3,a4))
    print('b0: {} b1: {} b2: {} b3: {} b4: {} '.format(b0,b1,b2,b3,b4))
    print('c1: {} c2: {} c3: {} c4: {} '.format(c1,c2,c3,c4))
    print('m0: {} m1: {} m2: {} m3: {} m4: {} '.format(m0,m1,m2,m3,m4))
    print('d: {} P: {}'.format(d,PS))
    print('c[{}]={}, m[{}]={}, clicked: {}\n'. format(k, c[k], k, m[k], aplicarPS.get()))
    plt.pause(0.01)
    k += 1
    mainGUI.after(1000, startGraphs)

################# Definicion de ambiente grafico  #################
mainGUI = Tk()
mainGUI.title("Simulación de planta de control")

# Variables 
aplicarPE = BooleanVar()
aplicarPS = BooleanVar()
modoOperacion = StringVar(value='manual')
ordenPlanta = StringVar(value='cero')

# Radio buttons
rbCero = Radiobutton(mainGUI, text='Orden cero', indicatoron=False, variable=ordenPlanta, value='cero')
rbPrimero = Radiobutton(mainGUI, text='Primer orden', indicatoron=False, variable=ordenPlanta, value='primero')
rbMan = Radiobutton(mainGUI, text='Manual', indicatoron=False, variable=modoOperacion, value='manual')
rbAuto = Radiobutton(mainGUI, text='Automático', indicatoron=False, variable=modoOperacion, value='auto')
rbCero.grid(row=1, column=1)
rbPrimero.grid(row=1, column=3)
rbMan.grid(row=1, column=5)
rbAuto.grid(row=1, column=7)

# Labels
Label(mainGUI, text='').grid(row=0) 
Label(mainGUI, text='').grid(row=2) 
Label(mainGUI, text='a1', anchor=W, justify=RIGHT).grid(row=3, column=0) 
Label(mainGUI, text='a2', anchor=W, justify=RIGHT).grid(row=4, column=0) 
Label(mainGUI, text='a3', anchor=W, justify=RIGHT).grid(row=5, column=0) 
Label(mainGUI, text='a4', anchor=W, justify=RIGHT).grid(row=6, column=0) 
Label(mainGUI, text='b0', anchor=W, justify=RIGHT).grid(row=8, column=0) 
Label(mainGUI, text='b1', anchor=W, justify=RIGHT).grid(row=9, column=0) 
Label(mainGUI, text='b2', anchor=W, justify=RIGHT).grid(row=10, column=0) 
Label(mainGUI, text='b3', anchor=W, justify=RIGHT).grid(row=11, column=0) 
Label(mainGUI, text='b4', anchor=W, justify=RIGHT).grid(row=12, column=0) 
Label(mainGUI, text='d', anchor=W, justify=RIGHT).grid(row=14, column=0) 
Label(mainGUI, text='K', anchor=W, justify=RIGHT).grid(row=3, column=2)
Label(mainGUI, text='Tau', anchor=W, justify=RIGHT).grid(row=4, column=2)
Label(mainGUI, text='Theta', anchor=W, justify=RIGHT).grid(row=5, column=2)
Label(mainGUI, text='T', anchor=W, justify=RIGHT).grid(row=7, column=3)
Label(mainGUI, text='Kp', anchor=W, justify=RIGHT).grid(row=3, column=4)
Label(mainGUI, text='TauI', anchor=W, justify=RIGHT).grid(row=4, column=4)
Label(mainGUI, text='TauD', anchor=W, justify=RIGHT).grid(row=5, column=4)
Label(mainGUI, text='Rk', anchor=W, justify=RIGHT).grid(row=3, column=6) 
Label(mainGUI, text='alpha1', anchor=W, justify=RIGHT).grid(row=5, column=6) 
Label(mainGUI, text='alpha2', anchor=W, justify=RIGHT).grid(row=6, column=6) 
Label(mainGUI, text='alpha3', anchor=W, justify=RIGHT).grid(row=7, column=6) 
Label(mainGUI, text='alpha4', anchor=W, justify=RIGHT).grid(row=8, column=6) 
Label(mainGUI, text='beta0', anchor=W, justify=RIGHT).grid(row=10, column=6) 
Label(mainGUI, text='beta1', anchor=W, justify=RIGHT).grid(row=11, column=6) 
Label(mainGUI, text='beta2', anchor=W, justify=RIGHT).grid(row=12, column=6) 
Label(mainGUI, text='beta3', anchor=W, justify=RIGHT).grid(row=13, column=6) 
Label(mainGUI, text='beta4', anchor=W, justify=RIGHT).grid(row=14, column=6) 
Label(mainGUI, text='').grid(row=15) 
Label(mainGUI, text='').grid(row=17) 
Label(mainGUI, text='').grid(row=19) 

# Entradas de texto
eA1 = Entry(mainGUI, width=7) 
eA2 = Entry(mainGUI, width=7) 
eA3 = Entry(mainGUI, width=7) 
eA4 = Entry(mainGUI, width=7) 
eB0 = Entry(mainGUI, width=7) 
eB1 = Entry(mainGUI, width=7) 
eB2 = Entry(mainGUI, width=7) 
eB3 = Entry(mainGUI, width=7) 
eB4 = Entry(mainGUI, width=7) 
eD = Entry(mainGUI, width=7) 
eK = Entry(mainGUI, width=7)
eTau = Entry(mainGUI, width=7)
eTheta = Entry(mainGUI, width=7)
eT = Entry(mainGUI, width=7)
eKp = Entry(mainGUI, width=7)
eTauI = Entry(mainGUI, width=7)
eTauD = Entry(mainGUI, width=7)
ePE = Entry(mainGUI, width=7) 
ePS = Entry(mainGUI, width=7) 
eR = Entry(mainGUI, width=7)
eAlpha1 = Entry(mainGUI, width=7) 
eAlpha2 = Entry(mainGUI, width=7) 
eAlpha3 = Entry(mainGUI, width=7) 
eAlpha4 = Entry(mainGUI, width=7) 
eBeta0 = Entry(mainGUI, width=7) 
eBeta1 = Entry(mainGUI, width=7) 
eBeta2 = Entry(mainGUI, width=7) 
eBeta3 = Entry(mainGUI, width=7) 
eBeta4 = Entry(mainGUI, width=7) 

# Configuracion entradas de texto
eA1.grid(row=3, column=1) 
eA2.grid(row=4, column=1)
eA3.grid(row=5, column=1)
eA4.grid(row=6, column=1)
eB0.grid(row=8, column=1) 
eB1.grid(row=9, column=1) 
eB2.grid(row=10, column=1)
eB3.grid(row=11, column=1)
eB4.grid(row=12, column=1)
eD.grid(row=14, column=1)
eK.grid(row=3, column=3)
eTau.grid(row=4, column=3)
eTheta.grid(row=5, column=3)
eT.grid(row=7, column=4)
eKp.grid(row=3, column=5)
eTauI.grid(row=4, column=5)
eTauD.grid(row=5, column=5)
ePE.grid(row=16, column=3)
ePS.grid(row=16, column=5)
eR.grid(row=3, column=7)
eAlpha1.grid(row=5, column=7) 
eAlpha2.grid(row=6, column=7)
eAlpha3.grid(row=7, column=7)
eAlpha4.grid(row=8, column=7)
eBeta0.grid(row=10, column=7) 
eBeta1.grid(row=11, column=7) 
eBeta2.grid(row=12, column=7)
eBeta3.grid(row=13, column=7)
eBeta4.grid(row=14, column=7)

# Boton de seleccion
bpe = Checkbutton(mainGUI, text='Pert. Entrada', var=aplicarPE)
bps = Checkbutton(mainGUI, text='Pert. Salida', var=aplicarPS)
bpe.grid(row=16, column=2)
bps.grid(row=16, column=4)

# Botones
Button(mainGUI, text='Comenzar', command=startGraphs).grid(row=18, column=3)
Button(mainGUI, text='Terminar', command=mainGUI.destroy).grid(row=18, column=4)

# Creacion de graficas interactivas
plt.ion()
plt.show()
fig, axs = plt.subplots(2, sharex=True)
axs[0].set_title('Salida c(k) y Referencia r(k)')
axs[0].set_ylabel('Amplitud')
axs[1].set_title('Manipulación m(k), Perturbación Entrada y Perturbación Salida')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Amplitud')

# Funcion recursiva del ambiente grafico
mainGUI.mainloop()
