import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import *

#
class LoteEconom():
    def __init__(self) -> None:
        #en el constructor -> varTiempo
        #------- MAIN WINDOW / CANVAS -------
        self.window = tk.Tk()
        self.window.title("MODELO LOTE ECONOMICO")
        self.window.geometry("600x480") # width x heigth
        self.window.resizable(0,0) #non resizable 0,0
        self.window.config(bg='#f2f4f4') #background color

        #self.tiempoChosen = varTiempo
        #print(self.tiempoChosen.get())
        #

        # ----- FONTS & COLORS -----
            #Bahnschrift SemiBold -- title
            #Segoe UI Semibold",20,'bold'))
            #bg="#f2f4f4",fg='#3a7741'
        #
        # --- VARS ---
        #(inputs)d, c, L, k, h, (outputs) Q, R, Cost(Q)
        #
        self.demanda = tk.DoubleVar()
        self.costo = tk.DoubleVar()
        self.tiempoL = tk.DoubleVar()
        self.costK = tk.DoubleVar()
        self.costH = tk.DoubleVar()
        self.cantQ = tk.DoubleVar()
        self.ptoR = tk.DoubleVar()
        self.totCost = tk.DoubleVar()
        # CASO EMPRESA PRODUCTO NACIONAL
        self.d4 = [12, 50, 15, 110, 115,90,130,75,54,160,280,41]
        self.d5 = [11,55,10,120,110,100,130,78,51,180,300,43]
        #
        #LABEL MAIN
        self.lblMain=tk.Label(self.window, bg="#f2f4f4",fg='#3a7741',text="Modelo de Lote Economico:",) #bg = background color, fg= foreground?color, font color basically
        self.lblMain.place(x=30,y=30)
        #f2f4f4 bg - fg title 83df8e
        self.lblMain.configure(font=("Century Gothic",24,'bold'))
        #
        #LABEL TEXT
        self.lblText=tk.Label(self.window, bg="#f2f4f4",fg='#3a7741',text="Ingresa los valores solicitados para general los cálculos: ") #bg=
        self.lblText.place(x=40,y=68)
        self.lblText.configure(font=("Segoe UI Semibold",11,'bold'))
        #
        #
        # # ------------------ MEDIDAS DE TIEMPO - COMBOBOX ----------------
        valueOfM=("dias","semanas","meses","años")
        self.varMedidas=tk.StringVar() # --- *
        
        self.cmbBoxTiempo=ttk.Combobox(self.window,values=valueOfM, textvariable=self.varMedidas, font=("Segoe UI Semibold",12,'bold'), width=16)
        self.cmbBoxTiempo.place(x=380,y=120)
        #self.lblTiempoL.place(x=120,y=150)
        self.cmbBoxTiempo.configure(foreground='#273746',background="#f2f4f4")#

        self.lblMedidaTiempo=tk.Label(self.window, bg="#f2f4f4",fg='#ff5731',text="Todos los valores en:") #bg=
        self.lblMedidaTiempo.place(x=380,y=90)
        self.lblMedidaTiempo.configure(font=("Segoe UI Semibold",12,'bold')) 
        #
        # ------------------- DEMANDA CONSTANTE -------------------
        #LABEL 
        self.lblDemanda=tk.Label(self.window, bg="#f2f4f4",fg='#061515',text="Demanda (d):") #bg=
        self.lblDemanda.place(x=40,y=100)
        self.lblDemanda.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxD=tk.Entry(self.window, textvariable=self.demanda, bg="#def3b9", fg='black', width=10,) #
        self.tboxD.place(x=180,y=105)
        self.tboxD.configure(font=("Segoe UI Semibold",12,'bold'))
        #
        # ------------------- COSTO UNITARIO -------------------
        #LABEL
        self.lblCostoUnit=tk.Label(self.window, bg="#f2f4f4",fg='#061515',text="Costo unit. (c):") #bg=
        self.lblCostoUnit.place(x=40,y=140)
        self.lblCostoUnit.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxC=tk.Entry(self.window, textvariable=self.costo, bg="#def3b9", fg='black', width=10) #
        self.tboxC.place(x=180,y=145)
        self.tboxC.configure(font=("Segoe UI Semibold",12,'bold'))
        #
        # ------------------- TIEMPO DE ENTREGA -------------------
        #LABEL 
        self.lblTiempoL=tk.Label(self.window, bg="#f2f4f4",fg='#061515',text="Tiempo de entrega (L):") #bg=
        self.lblTiempoL.place(x=40,y=180)
        self.lblTiempoL.configure(font=("Segoe UI Semibold",12,'bold'))
        #TEXTBOX 
        self.tboxL=tk.Entry(self.window, textvariable=self.tiempoL, bg="#def3b9", fg='black', width=10) #
        self.tboxL.place(x=220,y=185)
        self.tboxL.configure(font=("Segoe UI Semibold",12,'bold'))
        #
        # ------------------- COSTO DE PEDIDO -------------------
        #LABEL
        self.lblCostK=tk.Label(self.window, bg="#f2f4f4",fg='#061515',text="Costo de pedido (k):") #bg=
        self.lblCostK.place(x=40,y=220)
        self.lblCostK.configure(font=("Segoe UI Semibold",12,'bold'))
        #TEXTBOX 
        self.tboxK=tk.Entry(self.window, textvariable=self.costK, bg="#def3b9", fg='black', width=10) #
        self.tboxK.place(x=220,y=225)
        self.tboxK.configure(font=("Segoe UI Semibold",12,'bold'))
        #
        # ------------------- COSTO DE ALMACENAMIENTO -------------------
        #LABEL
        self.lblCostH=tk.Label(self.window, bg="#f2f4f4",fg='#061515',text="Costo de almacenamiento (h):") #bg=
        self.lblCostH.place(x=40,y=260)
        self.lblCostH.configure(font=("Segoe UI Semibold",12,'bold'))
        #TEXTBOX
        self.tboxH = tk.Entry(self.window, bg="#def3b9", fg='black', width=12, textvariable=self.costH) 
        self.tboxH.place(x=295,y=265)
        self.tboxH.configure(font=("Segoe UI Semibold",12,'bold'))
        #
        # ------------------------------------- BUTTONS ----------------------------
        # GENERAR CALCS
        self.btnCost=tk.Button(self.window, bg="#def3b9",fg='#3a7741',text="Generar calcs.",command=lambda:self.calcCostoTotal())#, command=self.metHere() 
        self.btnCost.place(x=430,y=165)
        self.btnCost.configure(font=("Segoe UI Semibold",12,'bold'), cursor="hand2")
        #CLEAN ALL
        self.btnClean=tk.Button(self.window, bg="#def3b9",fg='#3a7741',text="Limpiar",command=lambda:self.cleanAll())#, command=self.metHere() 
        self.btnClean.place(x=430,y=210)
        self.btnClean.configure(font=("Segoe UI Semibold",12,'bold'), cursor="hand2")
        #casoEmpresaversEmpleado
        self.btnEmpleado=tk.Button(self.window, bg="#def3b9",fg='#3a7741',text="Caso Empleado",command=lambda:self.casoEmpresaversEmpleado())#,command=lambda:self.casoEmpresaversEmpleado()
        self.btnEmpleado.place(x=430,y=255)
        self.btnEmpleado.configure(font=("Segoe UI Semibold",12,'bold'), cursor="hand2")
        #casoEmpresaversGerente
        self.btnEmpleado=tk.Button(self.window, bg="#def3b9",fg='#3a7741',text="Caso Gerente",command=lambda:self.casoEmpresaverGerente())#,command=lambda:self.casoEmpresaverGerente()
        self.btnEmpleado.place(x=430,y=305)
        self.btnEmpleado.configure(font=("Segoe UI Semibold",12,'bold'), cursor="hand2")
        #
        #
        # ------------------- CANT. DE PRODUCTOS A PEDIR (Q) -------------------
        #LABEL
        self.lblQ=tk.Label(self.window, bg="#f2f4f4",fg='#3a7741',text="Cant. de productos (Q):") #bg=
        self.lblQ.place(x=40,y=310)
        self.lblQ.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX
        self.tboxQ = tk.Entry(self.window, bg="#def3b9", fg='black', width=12, textvariable=self.cantQ) 
        self.tboxQ.place(x=265,y=315)
        self.tboxQ.configure(state='disable', font=("Segoe UI Semibold",14,'bold'))

        #
        # ------------------- PUNTO DE REORDEN (R) -------------------
        #LABEL
        self.lblR=tk.Label(self.window, bg="#f2f4f4",fg='#3a7741',text="Punto de reorden (R):") #bg=
        self.lblR.place(x=40,y=350)
        self.lblR.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX
        self.tboxR = tk.Entry(self.window, bg="#def3b9", fg='black', width=12, textvariable=self.ptoR) 
        self.tboxR.place(x=265,y=355)
        self.tboxR.configure(state='disable', font=("Segoe UI Semibold",14,'bold'))
        #
        #
        # ------------------- COSTO TOTAL (C(q)) -------------------
        #LABEL
        self.lblTotCost=tk.Label(self.window, bg="#f2f4f4",fg='#3a7741',text="Costo total -> Cost(Q):") #bg=
        self.lblTotCost.place(x=40,y=390)
        self.lblTotCost.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX
        self.tboxTotCost = tk.Entry(self.window, bg="#def3b9", fg='black', width=12, textvariable=self.totCost) 
        self.tboxTotCost.place(x=255,y=395)
        self.tboxTotCost.configure(state='disable', font=("Segoe UI Semibold",14,'bold'))
        # prueba llamado desde el menu -- discard for now, needs to be more worked on
        self.window.mainloop()  
    def runView(self):
        self.window.mainloop() 
    """def makeAGraphic(self, d, k, h, Q, C):
        try:
            #demanda = float(input("Ingrese la demanda anual (D): "))
            demanda = d
            #costoOrdenamiento/pedido = float(input("Ingrese el costo de ordenar por pedido (k): "))
            costoOrdenar = k
            #costo_mantener_unitario = float(input("Ingrese el costo de mantener por unidad al año (H): "))
            costoMant = h

            if demanda <= 0 or costoOrdenar < 0 or costoMant < 0:
                print("Por favor, ingrese valores no negativos y lógicos.")
                return

            # Rango de cantidades de pedido para la gráfica
            cantidades_pedido = np.linspace(1, 2 * np.sqrt((2 * demanda * costoOrdenar) / costoMant), 400)

            # Calcular los costos
            costoOrdenamiento = (demanda / cantidades_pedido) * costoOrdenar
            costoMantenimiento = (cantidades_pedido / 2) * costoMant
            costoTotal = costoOrdenar + costoMantenimiento

            # Calcular la EOQ teórica (para mostrarla como referencia)
            #eoq_teorico = np.sqrt((2 * demanda_anual * costo_ordenar) / costo_mantener_unitario)
            eoq_teorico = Q
            #costo_total_eoq = (demanda_anual / eoq_teorico) * costo_ordenar + (eoq_teorico / 2) * costo_mantener_unitario
            costo_total_eoq = C

            # Crear la primera gráfica: Componentes del costo
            plt.figure(figsize=(12, 6))
            plt.plot(cantidades_pedido, costoOrdenamiento, label='Costo de Pedido (k)', linestyle='--')
            plt.plot(cantidades_pedido, costoMantenimiento, label='Costo de Mantenimiento (h)', linestyle='-.')
            plt.xlabel(f"Cantidad de Pedido (Q) {Q}")
            plt.ylabel("Costo..")
            plt.title("Componentes del Costo Total en el Modelo EOQ")
            plt.legend()
            plt.grid(True)
            plt.annotate(f'Q* = {eoq_teorico:.2f}', xy=(eoq_teorico, costo_total_eoq), xytext=(eoq_teorico * 1.5, costo_total_eoq * 1.2),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            # Crear la segunda gráfica: Costo Total
            plt.figure(figsize=(12, 6))
            plt.plot(cantidades_pedido, costoTotal, label='Costo Total', color='green')
            plt.scatter(eoq_teorico, costo_total_eoq, color='red', marker='o', label=f'Costo Total Mínimo ({costo_total_eoq:.2f})')
            plt.xlabel(f"Cantidad de Pedido (Q): {Q}")
            plt.ylabel(f"Costo Total {C}")
            plt.title("Costo Total en el Modelo de Lote Economico")
            plt.legend()
            plt.grid(True)

            plt.show()
        except ValueError as e:
            messagebox.showerror("Error en la grafica!", "{e}")
            return
    """
    #
    def casoEmpresaverGerente(self): #PN -> Producto Nacional
        h = 0.05
        k = 55
        L = 3 
        c = 25 #aleatorio ya que no esta en el enunciado
        #
        """d4 = [12, 50, 15, 110, 115,90,130,75,54,160,280,41]
        d5 = [11,55,10,120,110,100,130,78,51,180,300,43]"""
            #
        gerente = sum(self.d4)+sum(self.d5)/2

        self.costH.set(h)
        self.costK.set(k)
        self.demanda.set(gerente)
        self.costo.set(c)
        self.tiempoL.set(L)

        """dG = gerente
        dE = nuevoEmp"""

        """gerenteProp = {
            'h' :0.05,
            'k' :55,
            'L' : 3 ,
            'c' : 25,
            'd' : gerente
        }"""


        m = 0 #m
        #
        R = -1 #R por defecto
        T = 0 # T
        #Calc Q: Q = round(sqrt((2*k*D/h)),2)  ---> Ecuacion / Formula
        sqDeQ = sqrt((2*k*gerente/h)) #Raiz de Q
        Q = round(sqDeQ,2)
        # para ver en consola
        print(f"Q = {Q}")
        self.cantQ.set(Q) #setteando a la interfaz visual
        #
        #Calculamos T:
        T = Q/gerente
        #si T > L
        #if(T > L): ----> prueba pq parece q hace un while infinito, check this out later
        if(T < L):
            R = round(gerente*L,2) #siguiendo la ecuacion; en caso de que T sea mayor se calcula R de esta manera
            print(f"R = {R}")
            self.ptoR.set(R) #setteando a la interfaz visual en Punto de Reorden
            #print(f"Cuando T > L, R = {round(R,2)}")
        else:
            #si L > T ****
            while (R==-1):
                if((L - m*T) > 0 and (L - (m+1)*T) < 0): #siguiendo la ecuacion; en caso de que L sea mayor
                    #
                    R = round(gerente*(L-m*T),2)
                    print(f"R = {R}")
                    self.ptoR.set(R) #set here
                    #print(f" Cuando L > T, R = {round(R,2)}")
                else:
                    m+=1
        #costo total
        calcThisC = (c*gerente) + (k * (gerente/Q)) + (1/2 * h * Q)
        C = round(calcThisC,2)
        self.totCost.set(C)#setteando a la interfaz visual 
        #self.makeAGraphic(gerente, k, h, Q, C)
        #
        x = [i for i in range(round(Q)+50)]
        y = [(c*gerente) + (k * (gerente/(i+1))) + (1/2 * h * i) for i in range(round(Q)+50)]
        plt.plot(x, y)
        plt.axvline(Q, color="green", linestyle="--")
        plt.xlabel(f"Cantidad de Pedido (Q): {Q}")
        plt.ylabel(f"Costo Total: {C}")
        plt.show()

        """
        La forma de la curva nos indica la sensibilidad del costo total a las desviaciones 
        de la cantidad óptima. Si la curva es relativamente plana alrededor del punto mínimo, significa 
        que pequeñas variaciones en la cantidad pedida no tendrán un impacto drástico en el costo total
        
        """
        #
    def cleanAll(self):
        self.costH.set('')
        self.costK.set('')
        self.demanda.set('')
        self.costo.set('')
        self.tiempoL.set('')
        self.cantQ.set('')
        self.ptoR.set('')
        self.totCost.set('')
    def casoEmpresaversEmpleado(self): #PN -> Producto Nacional
        self.cleanAll()
        try:
            h = 0.05
            k = 55
            L = 3 
            c = 25 #aleatorio ya que no esta en el enunciado

            #
            """d4 = [12, 50, 15, 110, 115,90,130,75,54,160,280,41]
            d5 = [11,55,10,120,110,100,130,78,51,180,300,43]"""
                #
            #gerente = sum(self.d4)+sum(self.d5)/2
            empleado = []
                #
            for i in self.d5:
                empleado.append(i+0.10)
            nuevoEmp = sum(empleado)

            self.costH.set(h)
            self.costK.set(k)
            self.demanda.set(nuevoEmp)
            self.costo.set(c)
            self.tiempoL.set(L)

            #dG = gerente
            dE = nuevoEmp

            """gerenteProp = {
                'h' :0.05,
                'k' :55,
                'L' : 3 ,
                'c' : 25,
                'd' : gerente
            }"""


            m = 0 #m
            #
            R = -1 #R por defecto
            T = 0 # T
            #Calc Q: Q = round(sqrt((2*k*D/h)),2)  ---> Ecuacion / Formula
            sqDeQ = sqrt((2*k*nuevoEmp/h)) #Raiz de Q
            Q = round(sqDeQ,2)
            # para ver en consola
            print(f"Q = {Q}")
            self.cantQ.set(Q) #setteando a la interfaz visual
            #
            #Calculamos T:
            T = Q/nuevoEmp
            #si T > L
            #if(T > L): ----> prueba pq parece q hace un while infinito, check this out later
            if(T < L):
                R = round(nuevoEmp*L,2) #siguiendo la ecuacion; en caso de que T sea mayor se calcula R de esta manera
                print(f"R = {R}")
                self.ptoR.set(R) #setteando a la interfaz visual en Punto de Reorden
                #print(f"Cuando T > L, R = {round(R,2)}")
            else:
                #si L > T ****
                while (R==-1):
                    if((L - m*T) > 0 and (L - (m+1)*T) < 0): #siguiendo la ecuacion; en caso de que L sea mayor
                        #
                        R = round(nuevoEmp*(L-m*T),2)
                        print(f"R = {R}")
                        self.ptoR.set(R) #set here
                        #print(f" Cuando L > T, R = {round(R,2)}")
                    else:
                        m+=1
            #costo total
            calcThisC = (c*nuevoEmp) + (k * (nuevoEmp/Q)) + (1/2 * h * Q)
            C = round(calcThisC,2)
            self.totCost.set(C)#setteando a la interfaz visual 
            #self.makeAGraphic(nuevoEmp, k, h, Q, C)
        except ValueError as e:
            messagebox.showerror("Error en la grafica", "{e}")
            return
        #
        #print("funciono?")
        #
        x = [i for i in range(round(Q)+50)]
        y = [(c*nuevoEmp) + (k * (nuevoEmp/(i+1))) + (1/2 * h * i) for i in range(round(Q)+50)]
        plt.plot(x, y)
        plt.axvline(Q, color="green", linestyle="--")
        plt.xlabel(f"Cantidad de Pedido (Q): {Q}")
        plt.ylabel(f"Costo Total: {C}")
        plt.show()

        """
        La forma de la curva nos indica la sensibilidad del costo total a las desviaciones 
        de la cantidad óptima. Si la curva es relativamente plana alrededor del punto mínimo, significa 
        que pequeñas variaciones en la cantidad pedida no tendrán un impacto drástico en el costo total
        
        """
    #
    #
    def calcCostoTotal(self):
        # self.var.get()
        # self.var.set()
        #ENTRADAS
        k = self.costK.get()
        h = self.costH.get()
        L = self.tiempoL.get()
        d = self.demanda.get()
        c = self.costo.get()
        #
        #--------------------------------------
        m = 0 #m
        #
        R = -1 #R por defecto
        T = 0 # T
        #Calc Q: Q = round(sqrt((2*k*D/h)),2)  ---> Ecuacion / Formula
        sqDeQ = sqrt((2*k*d/h)) #Raiz de Q
        Q = round(sqDeQ,2)
        # para ver en consola
        print(f"Q = {Q}")
        self.cantQ.set(Q) #setteando a la interfaz visual
        #
        #Calculamos T:
        T = Q/d
        #si T > L
        #if(T > L): ----> prueba pq parece q hace un while infinito, check this out later
        if(T < L):
            R = round(d*L,2) #siguiendo la ecuacion; en caso de que T sea mayor se calcula R de esta manera
            print(f"R = {R}")
            self.ptoR.set(R) #setteando a la interfaz visual en Punto de Reorden
            #print(f"Cuando T > L, R = {round(R,2)}")
        else:
            #si L > T ****
            while (R==-1):
                if((L - m*T) > 0 and (L - (m+1)*T) < 0): #siguiendo la ecuacion; en caso de que L sea mayor
                    #
                    R = round(d*(L-m*T),2)
                    print(f"R = {R}")
                    self.ptoR.set(R) #set here
                    #print(f" Cuando L > T, R = {round(R,2)}")
                else:
                    m+=1
        #costo total
        calcThisC = (c*d) + (k * (d/Q)) + (1/2 * h * Q)
        C = round(calcThisC,2)
        self.totCost.set(C) #setteando a la interfaz visual 
        #salida
        #print(f"Costo total :")
        print(f"Cost (Q) = {C}")

        #self.makeAGraphic(d, k, h, Q, C)
        #------------------------------------------------------------------------------------
        #("")
        
#--------------------------------%------------------------------%------------------------------%------------------------------
if (__name__=="__main__"):
    LoteEconom().runView()





"""#main
def main():
    LoteEconom()
#main - llamado de la clase
if (__name__=="__main__"):
    main()"""