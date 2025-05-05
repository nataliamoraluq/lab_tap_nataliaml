import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import *
from scipy.stats import norm
import matplotlib.pyplot as plt


class ModeloProb():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("MODELO PROBABILISTICO")
        self.window.geometry("710x620") # width x heigth
        self.window.resizable(0,0) #non resizable 0,0
        self.window.config(bg='#f2f4f4') #background 

        #83df8e
        
        # ----- FONTS & COLORS -----
            #Bahnschrift SemiBold -- title
            #Segoe UI Semibold",20,'bold'))
            #bg="#f2f4f4",fg='#273746' #base

            #tangerine - orangey color #ff5731
        #
        # --- VARS ---

        self.demanda = tk.DoubleVar()
        self.costo = tk.DoubleVar()
        self.tiempoL = tk.DoubleVar()
        self.costK = tk.DoubleVar()
        self.costH = tk.DoubleVar()
        self.cantQ = tk.DoubleVar()
        self.ptoR = tk.DoubleVar()
        self.totCost = tk.DoubleVar()
        #
        #entradas
        self.miu = tk.DoubleVar() #miu 
        self.sigma = tk.DoubleVar() #zigma
        self.L = tk.DoubleVar() #tiempo de demora L
        self.h = tk.DoubleVar() #costo de almacenamiento/mantenimiento
        self.k = tk.DoubleVar() #costo de pedido por lote
        self.n = tk.DoubleVar() #n - cantidad
        self.pA = tk.DoubleVar() #faltante acumulado
        self.pN = tk.DoubleVar() #faltante no acumulado
        #salidas
        self.ptoR = tk.DoubleVar() #Pto de reorden R cuando
        self.cantQ = tk.DoubleVar() #Q cuanto
        self.probCalc = tk.DoubleVar() #prob en la tabla sin despejar
        self.z = tk.DoubleVar() #z despejado/ obtenido de la tabla
        
        #
        #LABEL MAIN
        self.lblMain=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Modelo Probabilístico:",) #bg = background color, fg= foreground?color, font color basically
        self.lblMain.place(x=30,y=30)
        self.lblMain.configure(font=("Century Gothic",21,'bold'))
        #
        #LABEL TEXT
        self.lblText=tk.Label(self.window, bg="#f2f4f4",fg='#ff5731',text="Para calcular probabilidad, cuánto pagar y cuándo pagar, con faltantes") #bg=
        self.lblText.place(x=35,y=68)
        self.lblText.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        #
        # ------------------- MEDIA - MIU (μ)  -------------------
        #LABEL 
        self.lblMiu=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Media (μ):") #bg=
        self.lblMiu.place(x=40,y=110)
        self.lblMiu.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxMiu=tk.Entry(self.window, textvariable=self.miu, bg="#ffe5cc", fg='#273746', width=8) #

        self.tboxC=tk.Entry(self.window, textvariable=self.costo, bg="#def3b9", fg='black', width=10) #

        self.tboxMiu.place(x=140,y=112)
        self.tboxMiu.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- SIGMA - DESVIACION ESTANDAR (σ) -------------------
        #LABEL 
        self.lblSigma=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Desviación estándar (sigma):") #bg=
        self.lblSigma.place(x=290,y=110)
        self.lblSigma.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxSigma=tk.Entry(self.window, bg="#ffe5cc", fg='#273746', width=8, textvariable=self.sigma) #
        self.tboxSigma.place(x=550,y=112)
        self.tboxSigma.configure(font=("Segoe UI Semibold",14,'bold'))
        # ------------------- TIEMPO DE DEMORA (L)  -------------------
        #LABEL
        self.lblTiempoL=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Tiempo de demora (L):") #bg=
        self.lblTiempoL.place(x=40,y=150)
        self.lblTiempoL.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxL=tk.Entry(self.window, textvariable=self.L, bg="#ffe5cc", fg='#273746', width=10,) #
        self.tboxL.place(x=245,y=152)
        self.tboxL.configure(font=("Segoe UI Semibold",14,'bold'))

        # ------------------- CANTIDAD (n)  -------------------
        #LABEL
        self.lblCantN=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Cantidad (n):") #bg=
        self.lblCantN.place(x=40,y=192)
        self.lblCantN.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxCantN=tk.Entry(self.window, textvariable=self.n, bg="#ffe5cc", fg='#273746', width=10,) #
        self.tboxCantN.place(x=165,y=195)
        self.tboxCantN.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- COSTO DE ALMACENAMIENTO (h)  -------------------
        #LABEL
        self.lblCostoH=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Costo de almacenamiento (h):") #bg=
        self.lblCostoH.place(x=40,y=232)
        self.lblCostoH.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxCostoH=tk.Entry(self.window, textvariable=self.h, bg="#ffe5cc", fg='#273746', width=10,) #
        self.tboxCostoH.place(x=310,y=235)
        self.tboxCostoH.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- COSTO DE PEDIDO (k)  -------------------
        #LABEL
        self.lblCostoK=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Costo de pedido (k):") #bg=
        self.lblCostoK.place(x=40,y=277)
        self.lblCostoK.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxCostoK=tk.Entry(self.window, textvariable=self.k, bg="#ffe5cc", fg='#273746', width=10,) #
        self.tboxCostoK.place(x=230,y=280)
        self.tboxCostoK.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- TIPO DE FALTANTE A USAR  -------------------
        #LABEL
        self.lblFaltantes=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Tipo de Faltante a utilizar:") #bg=
        self.lblFaltantes.place(x=40,y=317)
        self.lblFaltantes.configure(font=("Segoe UI Semibold",14,'bold'))
        #RADIOBUTTONS OR COMBOBOX -- 
        #
        # ------------------ MEDIDAS DE TIEMPO - COMBOBOX ----------------
        valueOfM=("dias","semanas","meses","años")
        self.varMedidas=tk.StringVar() # --- *
        
        self.cmbBoxTiempo=ttk.Combobox(self.window,values=valueOfM, textvariable=self.varMedidas, font=("Segoe UI Semibold",12,'bold'), width=16)
        self.cmbBoxTiempo.place(x=480,y=190)
        #self.lblTiempoL.place(x=120,y=150)
        self.cmbBoxTiempo.configure(foreground='#273746',background="#f2f4f4")#

        self.lblMedidaTiempo=tk.Label(self.window, bg="#f2f4f4",fg='#ff5731',text="Todos los valores en:") #bg=
        self.lblMedidaTiempo.place(x=470,y=150)
        self.lblMedidaTiempo.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------ COMBOBOX - TIPO FALTANTES ----------------
        valueFaltantes=("acumulados","no_acumulados")
        self.varFaltantes=tk.StringVar() # --- *
        
        self.cmbBoxTipoFaltantes=ttk.Combobox(self.window,values=valueFaltantes, textvariable=self.varFaltantes, font=("Segoe UI Semibold",12,'bold'), width=16)
        self.cmbBoxTipoFaltantes.place(x=320,y=317)
        self.cmbBoxTipoFaltantes.configure(foreground='#273746',background="#f2f4f4")#
        
        # ------------------- FALTANTE ACUMULADO (pA)  -------------------
        #LABEL
        self.lblPa=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Costo de faltante acumulado (pA):") #bg=
        self.lblPa.place(x=40,y=357)
        self.lblPa.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxPa=tk.Entry(self.window, textvariable=self.pA, bg="#ffe5cc", fg='#273746', width=10,) #
        self.tboxPa.place(x=350,y=359)
        self.tboxPa.configure(font=("Segoe UI Semibold",14,'bold'))

        # ------------------- FALTANTE NO ACUMULADO (pN)  -------------------
        #LABEL
        self.lblPn=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Costo de faltante no acumulado (pN):") #bg=
        self.lblPn.place(x=40,y=402)
        self.lblPn.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxPn=tk.Entry(self.window, textvariable=self.pN, bg="#ffe5cc", fg='#273746', width=10,) #
        self.tboxPn.place(x=380,y=405)
        self.tboxPn.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- PROBABILIDAD  -------------------
        #LABEL 
        self.lblProb=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="P(Dl <= R):") #bg=
        self.lblProb.place(x=40,y=445)
        self.lblProb.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxProb=tk.Entry(self.window, textvariable=self.probCalc, bg="#ffe5cc", fg='#273746', width=8) #
        self.tboxProb.place(x=167,y=450)
        self.tboxProb.configure(state='disable', font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- z DE PROBABILIDAD EN LA TABLA -------------------
        #LABEL 
        self.lblZcalc=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="z:") #bg=
        self.lblZcalc.place(x=300,y=445)
        self.lblZcalc.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxZcalc=tk.Entry(self.window, textvariable=self.z, bg="#ffe5cc", fg='#273746', width=8) #
        self.tboxZcalc.place(x=330,y=450)
        self.tboxZcalc.configure(state='disable', font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- Q -------------------
        #LABEL 
        self.lblQ=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Q:") #bg=
        self.lblQ.place(x=485,y=445)
        self.lblQ.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxQ=tk.Entry(self.window, textvariable=self.cantQ, bg="#ffe5cc", fg='#273746', width=8) #
        self.tboxQ.place(x=520,y=450)
        self.tboxQ.configure(state='disable', font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- R Calc. -------------------
        #LABEL 
        self.lblRcalc=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="R:") #bg=
        self.lblRcalc.place(x=40,y=500)
        self.lblRcalc.configure(font=("Segoe UI Semibold",16,'bold'))
        #TEXTBOX 
        self.tboxRcalc=tk.Entry(self.window, textvariable=self.ptoR, bg="#f6beb2", fg='#273746', width=8) #
        self.tboxRcalc.place(x=75,y=505)
        self.tboxRcalc.configure(state='disable', font=("Segoe UI Semibold",16,'bold'))
        #
        # ------------------------ BUTTONS ---------------------------------------
        #BTN CALC -- MAIN CALC
        self.btnCalc=tk.Button(self.window, bg="#ffe5cc",fg='#273746',text="Calcular",command=lambda:self.calcProb()) #
        self.btnCalc.place(x=205,y=545)
        self.btnCalc.configure(font=("Segoe UI Semibold",14,'bold'), cursor="hand2")

        #BTN CALC -- GRAFICOS
        """
        self.btnGraphics=tk.Button(self.window, bg="#ffe5cc",fg='#273746',text="Generar Gráficas",command=lambda:self.showGrafica()) #
        self.btnGraphics.place(x=310,y=545)
        self.btnGraphics.configure(font=("Segoe UI Semibold",14,'bold'), cursor="hand2")"""

        #BTN CALC -- CLEAN ALL
        self.btnClean=tk.Button(self.window, bg="#ffe5cc",fg='#273746',text="Limpiar",command=lambda:self.cleanAll()) #
        self.btnClean.place(x=310,y=545) #with the past one x=490, ifnot, the x of the past one
        self.btnClean.configure(font=("Segoe UI Semibold",14,'bold'), cursor="hand2")
        #
    def showGrafica(plt):
        # Mostrar la gráfica
        plt.show()
    def makeGraphics(self, Q, R, D, L):
        #
        try:
            #Q = self.cantQ.get()
            #R = self.ptoR.get()
            #
            #D = 25
            #L = 25
            lead_time = L

            if Q <= 0 or R < 0 or D <= 0 or L < 0:
                print("Por favor, ingrese valores no negativos y lógicos.")
                return

            # Calcular el tiempo hasta el punto de reorden desde un inventario máximo (Q)
            tiempo_hasta_reorden = (Q - R) / D

            # Calcular el tiempo que tarda en agotarse el inventario desde el punto de reorden
            tiempo_hasta_agotamiento = R / D

            # Calcular el ciclo de pedido (T)
            ciclo_pedido = Q / D
            #ciclo_pedido = T

            # Generar los puntos para la gráfica
            tiempo_puntos = [0, tiempo_hasta_reorden, tiempo_hasta_reorden, tiempo_hasta_reorden + lead_time,
                            ciclo_pedido, ciclo_pedido + tiempo_hasta_reorden, ciclo_pedido + tiempo_hasta_reorden,
                            ciclo_pedido + tiempo_hasta_reorden + lead_time, 2 * ciclo_pedido]
            cantidad_puntos = [Q, R, R, 0, Q, R, R, 0, Q]

            # Crear la gráfica
            plt.figure(figsize=(10, 6))
            plt.plot(tiempo_puntos, cantidad_puntos, marker='.', linestyle='-', color='red')
            plt.axhline(y=R, color='blue', linestyle='-', label=f'Punto de Reorden (R = {R})')
            plt.axvline(x=tiempo_hasta_reorden + lead_time, color='gray', linestyle='--', label=f'Lead Time (L = {lead_time:.2f})', ymax=R/Q) # Línea de ejemplo para el Lead Time

            # Etiquetas y título
            plt.xlabel("Tiempo")
            plt.ylabel("Cantidad")
            plt.title("Modelo de Cantidad Fija de Pedido")
            plt.legend()
            plt.grid(True)
            plt.ylim(bottom=0) # Asegurar que el eje Y comience en 0
            plt.show()
            #self.showGrafica(plt)
        except ValueError as e:
            messagebox.showerror("Error en la grafica!", "{e}")
            return
    def calcProb(self):
        #entradas
        miu = self.miu.get()
        #tryal = self.tboxMiu.get()
        sigma = self.sigma.get()
        tiempoL = self.L.get()
        h = self.h.get()
        k = self.k.get()
        n = self.n.get()
        pA = self.pA.get()
        pN = self.pN.get()
        #salidas
        #CALCULO DE LA ESPERANZA
        Esp = n * miu
        print(f"Esperanza: {Esp}")    
        #int(input("Esperanza: "))
        #CALCULO DE CANT. Q
        Qval = sqrt((2*k*Esp)/h)
        #
        print(f" Q = {Qval}")
        Qround = round(Qval,2)
        self.cantQ.set(Qround)
        #
        prob = 0
        #valueFaltantes=("acumulados","no_acumulados")
        
        if(self.varFaltantes.get()=="acumulados"):
            #
            pSub = pA
            # NORMALIZACION
            prob = (h * Qval) / (pSub * Esp)
            #probRound = round(prob,4)
            self.probCalc.set(prob)
            print(f" valor de prob = {prob}")
        else:
            #print(f"vers de faltantes NO acumulados")
            #
            pSub = pN
            # NORMALIZACION
            prob = (h * Qval) / (h * Qval + (pSub * Esp))
            #probRound = round(prob,4) 
            self.probCalc.set(prob) #OJO: como da nros muy pequeños con e-elevado, seteo completo para ver el valor de la prob!!
            print(f" valor de prob = {prob}")
        #prob 
        z = abs(norm.ppf(prob))
        zRound = round(z,2)
        self.z.set(zRound)
        print(f" z = {z}")        
        #CALC DE PTO DE REORDEN -> R    
        Rval = round(((z * sigma) + miu),2)
        roundR = round(Rval,2)
        #self.ptoR.set(roundR)
        self.ptoR.set(Rval)
        #
        print("Luego de despejar, punto de reorden (R):")
        #print(f"R = {round(Rval,3)}")
        print(f"R = {Rval}")

        self.makeGraphics(Qval, Rval, zRound, tiempoL)

        #self.makeGraphics(Q, R, D, L)
    def runView(self):
        self.window.mainloop()
    def cleanAll(self):
        """self.miu.set('') #miu 
        self.sigma.set('') #zigma
        self.L.set('') #tiempo de demora L
        self.h.set('') #costo de almacenamiento/mantenimiento
        self.k.set('')#costo de pedido por lote
        self.n.set('') #n - cantidad
        self.pA.set('') #faltante acumulado
        self.pN.set('') #faltante no acumulado
        #salidas
        self.ptoR.set('') #Pto de reorden R cuando
        self.cantQ.set('') #Q cuanto
        self.probCalc.set('') #prob en la tabla sin despejar"""
        self.z.set('') #z despejado/ obtenido de la tabla

if (__name__=="__main__"):
    ModeloProb().runView()

#main
"""
def main():
    ModeloProb()
#main - llamado de la clase
if (__name__=="__main__"):
    main()"""