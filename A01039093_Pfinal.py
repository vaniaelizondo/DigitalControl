from tkinter import *
import matplotlib.pyplot as plt
from numpy import *

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
PE = 0
PS = 0

# Leer archivo entrada
# i = 0
# entrada = open("entrada.txt")
# for x in entrada:
#     m.append(float(x))
#     i += 1
# entrada.close()

################# Definicion de funciones #################
# Funcion que grafica
def startGraphs():
    global mainGUI
    global fig, axs
    global m, c, k, PE, PS
    global eMk, eRk, eT
    global eA1, eA2, eA3, eA4
    global eB0, eB1, eB2, eB3, eB4, eD
    global eKc, eTau, eTheta
    global eKp, eTauI, eTauD
    global eAlpha1, eAlpha2, eAlpha3, eAlpha4
    global eBeta0, eBeta1, eBeta2, eBeta3, eBeta4
    global modoOperacion, ordenPlanta, controlador

# Actualizar entradas dependiendo de orden de planta, modo de operacion y controlador
    try:
        t = float(eT.get())
    except:
        t = 0

    if (ordenPlanta.get() == 'cero'):
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
    elif (ordenPlanta.get() == 'primero'):
        try:
            kc = float(eKc.get())
        except:
            kc = 0
        try:
            tau = float(eTau.get())
        except:
            tau = 0
        try:
            thetaP = float(eTheta.get())
        except:
            thetaP = 0
        try:
            d = int(floor(thetaP/t))
        except ZeroDivisionError:
            d = 0
        theta = thetaP - d * t
        try:
            mt = 1 - (theta/t)
        except ZeroDivisionError:
            mt = 1
        try:
            a1 = exp(-(t/tau))
        except ZeroDivisionError:
            a1 = 1
        a2 = 0
        a3 = 0
        a4 = 0
        b0 = 0
        try:
            b1 = kc * (1 - exp(-(mt*t/tau)))
        except ZeroDivisionError:
            b1 = 0
        try:
            exp1 = (mt*t/tau)
        except ZeroDivisionError:
            exp1 = 0
        try:
            exp2 = (t/tau)
        except ZeroDivisionError:
            exp2 = 0
        b2 = kc * (exp(-exp1) - exp(-exp2))
        b3 = 0
        b4 = 0

    if (controlador.get() == 'PID'):
        try:
            kp = float(eKp.get())
        except:
            kp = 0
        try:
            tauI = float(eTauI.get())
        except:
            tauI = 0
        try:
            tauD = float(eTauD.get())
        except:
            tauD = 0
        alpha1 = 1
        alpha2 = 0
        alpha3 = 0
        alpha4 = 0
        try:
            ti = t/tauI
        except ZeroDivisionError:
            ti = 0
        try:
            td = tauD/t
        except ZeroDivisionError:
            td = 0
        beta0 = kp * (1 + ti + td)
        beta1 = -kp * (1 + 2 * td)
        beta2 = kp * (td)
        beta3 = 0
        beta4 = 0
    elif (controlador.get() == 'ecgral'):
        try: 
            alpha1 = float(eAlpha1.get())
        except:
            alpha1 = 0
        try:
            alpha2 = float(eAlpha2.get())
        except:
            alpha2 = 0
        try:
            alpha3 = float(eAlpha3.get())
        except:
            alpha3 = 0
        try:
            alpha4 = float(eAlpha4.get())
        except:
            alpha4 = 0
        try:
            beta0 = float(eBeta0.get())
        except:
            beta0 = 0
        try:
            beta1 = float(eBeta1.get())
        except:
            beta1 = 0
        try:
            beta2 = float(eBeta2.get())
        except:
            beta2 = 0
        try:
            beta3 = float(eBeta3.get())
        except:
            beta3 = 0
        try:
            beta4 = float(eBeta4.get())
        except:
            beta4 = 0

    if (modoOperacion.get() == 'manual'):
        try:
            mk = float(eMk.get())
        except:
            mk = 0
        m.append(mk)
        if ((k-1) < 0):
            c1 = 0
            rk = 0
        else:
            c1 = c[k-1]
            rk = c[k-1]
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
    elif (modoOperacion.get() == 'auto'):
        try:
            rk = float(eRk.get())
        except:
            rk = 0
        if ((k-1) < 0):
            c1 = 0
            e0 = 0
        else:
            c1 = c[k-1]
            e0 = rk - c[k-1]
        if ((k-2) < 0):
            c2 = 0
            e1 = 0
        else:
            c2 = c[k-2]
            e1 = rk - c[k-2]
        if ((k-3) < 0):
            c3 = 0
            e2 = 0
        else:
            c3 = c[k-3]
            e2 = rk - c[k-3]
        if ((k-4) < 0):
            c4 = 0
            e3 = 0
        else:
            c4 = c[k-4]
            e3 = rk - c[k-4]
        if ((k-5) < 0):
            e4 = 0
        else:
            e4 = rk - c[k-5]
        m0 = 0
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
        m.append(alpha1*m1 + alpha2*m2 + alpha3*m3 + alpha4*m4 + beta0*e0 + beta1*e1 + beta2*e2 + beta3*e3 + beta4*e4)
    
# Graficar
    c.append(PE + a1*c1 + a2*c2 + a3*c3 + a4*c4 + b0*m0 + b1*m1 + b2*m2 + b3*m3 + b4*m4 + PS)
    axs[0].plot(k, rk, 'bs', k, c[k], 'm.')
    axs[0].legend(['rk', 'c[k]'], loc='upper right')
    axs[1].plot(k, m[k], 'gs', k, PE, 'rd', k, PS, 'c.')
    axs[1].legend(['m[k]', 'Pert. Entrada', 'Pert. Salida'], loc='upper right')
    print('ordenPlanta: {}     controlador: {}     modoOperacion: {}'.format(ordenPlanta.get(),controlador.get(),modoOperacion.get()))
    print('a1: {}   a2: {}    a3: {}     a4: {} '.format(a1,a2,a3,a4))
    print('b0: {}   b1: {}    b2: {}     b3: {}     b4: {}   d: {}'.format(b0,b1,b2,b3,b4,d))
    print('alpha1: {}   alpha2: {}    alpha3: {}     alpha4: {} '.format(alpha1,alpha2,alpha3,alpha4))
    print('beta0: {}    beta1: {}     beta2: {}    beta3: {}   beta4: {}'.format(beta0,beta1,beta2,beta3,beta4))
    # print('t: {}    mk: {}      rk: {}'.format(t,mk,rk))
    print('PE: {}   PS: {}'.format(PE,PS))
    print('m0: {}   m1: {}    m2: {}     m3: {}  m4: {} '.format(m0,m1,m2,m3,m4))
    # print('e0: {}   e1: {}    e2: {}     e3: {}  e4: {} '.format(e0,e1,e2,e3,e4))
    print('c1: {}   c2: {}    c3: {}     c4: {}'.format(c1,c2,c3,c4))
    print('c[{}]={}     m[{}]={}\n'. format(k, c[k], k, m[k]))
    plt.pause(t)
    k += 1
    mainGUI.after(1000, startGraphs)

# Funcion que agrega perturbacion de entrada
def pertEntrada():
    global aplicarPE, ePE, PE
    try:
        PE += float(ePE.get())
    except:
        pass

# Funcion que agrega perturbacion de salida
def pertSalida():
    global aplicarPS, ePS, PS
    try:
        PS += float(ePS.get())
    except:
        pass

################# Definicion de ambiente grafico  #################
mainGUI = Tk()
mainGUI.title("Simulación de planta de control")

# Variables 
aplicarPE = BooleanVar()
aplicarPS = BooleanVar()
modoOperacion = StringVar(value='manual')
ordenPlanta = StringVar(value='cero')
controlador = StringVar(value='PID')

# Radio buttons
rbMan = Radiobutton(mainGUI, text='Manual', indicatoron=False, selectcolor='magenta', variable=modoOperacion, value='manual')
rbAuto = Radiobutton(mainGUI, text='Automático', indicatoron=False, selectcolor='magenta', variable=modoOperacion, value='auto')
rbCero = Radiobutton(mainGUI, text='Orden cero', indicatoron=False, selectcolor='cyan', variable=ordenPlanta, value='cero')
rbPrimero = Radiobutton(mainGUI, text='Primer orden', indicatoron=False, selectcolor='cyan', variable=ordenPlanta, value='primero')
rbPID = Radiobutton(mainGUI, text='PID', indicatoron=False, selectcolor='yellow', variable=controlador, value='PID')
rbEcGral = Radiobutton(mainGUI, text='Ec. General', indicatoron=False, selectcolor='yellow', variable=controlador, value='ecgral')
rbMan.grid(row=1, column=3)
rbAuto.grid(row=1, column=4)
rbCero.grid(row=5, column=1)
rbPrimero.grid(row=5, column=3)
rbPID.grid(row=5, column=5)
rbEcGral.grid(row=5, column=7)

# Labels
Label(mainGUI, text='').grid(row=0) 
Label(mainGUI, text='').grid(row=2) 
Label(mainGUI, text='').grid(row=4) 
Label(mainGUI, text='').grid(row=6) 
Label(mainGUI, text='mk', anchor=W, justify=RIGHT).grid(row=3, column=2) 
Label(mainGUI, text='Rk', anchor=W, justify=RIGHT).grid(row=3, column=4) 
Label(mainGUI, text='a1', anchor=W, justify=RIGHT).grid(row=7, column=0) 
Label(mainGUI, text='a2', anchor=W, justify=RIGHT).grid(row=8, column=0) 
Label(mainGUI, text='a3', anchor=W, justify=RIGHT).grid(row=9, column=0) 
Label(mainGUI, text='a4', anchor=W, justify=RIGHT).grid(row=10, column=0) 
Label(mainGUI, text='b0', anchor=W, justify=RIGHT).grid(row=12, column=0) 
Label(mainGUI, text='b1', anchor=W, justify=RIGHT).grid(row=13, column=0) 
Label(mainGUI, text='b2', anchor=W, justify=RIGHT).grid(row=14, column=0) 
Label(mainGUI, text='b3', anchor=W, justify=RIGHT).grid(row=15, column=0) 
Label(mainGUI, text='b4', anchor=W, justify=RIGHT).grid(row=16, column=0) 
Label(mainGUI, text='d', anchor=W, justify=RIGHT).grid(row=18, column=0) 
Label(mainGUI, text='K', anchor=W, justify=RIGHT).grid(row=7, column=2)
Label(mainGUI, text='Tau', anchor=W, justify=RIGHT).grid(row=8, column=2)
Label(mainGUI, text='Theta', anchor=W, justify=RIGHT).grid(row=9, column=2)
Label(mainGUI, text='T', anchor=W, justify=RIGHT).grid(row=11, column=3)
Label(mainGUI, text='Kp', anchor=W, justify=RIGHT).grid(row=7, column=4)
Label(mainGUI, text='TauI', anchor=W, justify=RIGHT).grid(row=8, column=4)
Label(mainGUI, text='TauD', anchor=W, justify=RIGHT).grid(row=9, column=4)
Label(mainGUI, text='alpha1', anchor=W, justify=RIGHT).grid(row=7, column=6) 
Label(mainGUI, text='alpha2', anchor=W, justify=RIGHT).grid(row=8, column=6) 
Label(mainGUI, text='alpha3', anchor=W, justify=RIGHT).grid(row=9, column=6) 
Label(mainGUI, text='alpha4', anchor=W, justify=RIGHT).grid(row=10, column=6) 
Label(mainGUI, text='beta0', anchor=W, justify=RIGHT).grid(row=12, column=6) 
Label(mainGUI, text='beta1', anchor=W, justify=RIGHT).grid(row=13, column=6) 
Label(mainGUI, text='beta2', anchor=W, justify=RIGHT).grid(row=14, column=6) 
Label(mainGUI, text='beta3', anchor=W, justify=RIGHT).grid(row=15, column=6) 
Label(mainGUI, text='beta4', anchor=W, justify=RIGHT).grid(row=16, column=6) 
Label(mainGUI, text='Pert. Entrada', anchor=W, justify=RIGHT).grid(row=20, column=2) 
Label(mainGUI, text='Pert. Salida', anchor=W, justify=RIGHT).grid(row=20, column=4) 
Label(mainGUI, text='').grid(row=17) 
Label(mainGUI, text='').grid(row=19) 
Label(mainGUI, text='').grid(row=20) 
Label(mainGUI, text='').grid(row=22) 
Label(mainGUI, text='').grid(row=24) 

# Entradas de texto
eMk = Entry(mainGUI, width=7)
eRk = Entry(mainGUI, width=7)
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
eKc = Entry(mainGUI, width=7)
eTau = Entry(mainGUI, width=7)
eTheta = Entry(mainGUI, width=7)
eT = Entry(mainGUI, width=7)
eKp = Entry(mainGUI, width=7)
eTauI = Entry(mainGUI, width=7)
eTauD = Entry(mainGUI, width=7)
eAlpha1 = Entry(mainGUI, width=7) 
eAlpha2 = Entry(mainGUI, width=7) 
eAlpha3 = Entry(mainGUI, width=7) 
eAlpha4 = Entry(mainGUI, width=7) 
eBeta0 = Entry(mainGUI, width=7) 
eBeta1 = Entry(mainGUI, width=7) 
eBeta2 = Entry(mainGUI, width=7) 
eBeta3 = Entry(mainGUI, width=7) 
eBeta4 = Entry(mainGUI, width=7) 
ePE = Entry(mainGUI, width=7) 
ePS = Entry(mainGUI, width=7) 

# Configuracion entradas de texto
eMk.grid(row=3, column=3)
eRk.grid(row=3, column=5)
eA1.grid(row=7, column=1) 
eA2.grid(row=8, column=1)
eA3.grid(row=9, column=1)
eA4.grid(row=10, column=1)
eB0.grid(row=12, column=1) 
eB1.grid(row=13, column=1) 
eB2.grid(row=14, column=1)
eB3.grid(row=15, column=1)
eB4.grid(row=16, column=1)
eD.grid(row=18, column=1)
eKc.grid(row=7, column=3)
eTau.grid(row=8, column=3)
eTheta.grid(row=9, column=3)
eT.grid(row=11, column=4)
eKp.grid(row=7, column=5)
eTauI.grid(row=8, column=5)
eTauD.grid(row=9, column=5)
eAlpha1.grid(row=7, column=7) 
eAlpha2.grid(row=8, column=7)
eAlpha3.grid(row=9, column=7)
eAlpha4.grid(row=10, column=7)
eBeta0.grid(row=12, column=7) 
eBeta1.grid(row=13, column=7) 
eBeta2.grid(row=14, column=7)
eBeta3.grid(row=15, column=7)
eBeta4.grid(row=16, column=7)
ePE.grid(row=20, column=3)
ePS.grid(row=20, column=5)

# Botones
Button(mainGUI, text='Aplicar', command=pertEntrada).grid(row=21, column=3)
Button(mainGUI, text='Aplicar', command=pertSalida).grid(row=21, column=5)
Button(mainGUI, text='Comenzar', command=startGraphs).grid(row=23, column=3)
Button(mainGUI, text='Terminar', command=mainGUI.destroy).grid(row=23, column=4)

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
