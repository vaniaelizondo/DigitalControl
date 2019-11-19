from tkinter import *
import matplotlib.pyplot as plt

###########################################################
# Vania Alejandra Elizondo Martínez
# A01039093
# Control Computarizado
###########################################################

################# Declaracion de ambiente #################
# Variables globales
m = [0]*1000
c = [0]*1000
k = 0
t = 0.5
i = 0

# Leer archivo entrada
entrada = open('entrada.txt')
for x in entrada:
    m[i] = float(x)
    i += 1
entrada.close()

################# Definicion de funciones #################
# Funcion que grafica
def startGraphs():
    global mainGUI
    global fig, axs
    global c, m, k, t
    global a1, a2, a3, a4
    global b0, b1, b2, b3, b4
    global d, P, aplicarP

    # Grafica con perturbacion
    if (aplicarP.get()):
        c[k] = a1*c[k-1] + a2*c[k-2] + a3*c[k-3] + a4*c[k-4] + b0*m[k-d] + b1*m[k-1-d] + b2*m[k-2-d] + b3*m[k-3-d] + b4*m[k-4-d] + P
        
    # Grafica sin perturbacion
    else:
        c[k] = a1*c[k-1] + a2*c[k-2] + a3*c[k-3] + a4*c[k-4] + b0*m[k-d] + b1*m[k-1-d] + b2*m[k-2-d] + b3*m[k-3-d] + b4*m[k-4-d]
        P = 0

    axs[0].plot(k*t, c[k], 'b.')
    axs[1].plot(k*t, m[k], 'g.', k*t, P, 'r+')
    axs[1].legend(['m[k]', 'P'], loc='upper right')
    print('c[{}]={}, m[{}]={}, P: {} clicked: {}'. format(k, c[k], k, m[k], P, aplicarP.get()))
    plt.pause(0.001)
    k += 1
    mainGUI.after(1000, startGraphs)

################# Funcion que abre interfaz grafica #################
def main():
# Variables globales
    global mainGUI
    global fig, axs
    global c, m, k, t
    global a1, a2, a3, a4
    global b0, b1, b2, b3, b4
    global d, P, aplicarP

# Definicion de ambiente grafico 
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

# Programa recursivo
if __name__ == "__main__":
    main()