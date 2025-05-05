import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import *
#from scipy.stats import norm
#import matplotlib.pyplot as plt


class ModeloMM1():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("MODELO MM1 - TEORIA DE COLAS")
        self.window.geometry("870x690") # width x heigth
        self.window.resizable(0,0) #non resizable 0,0
        self.window.config(bg='#f2f4f4') #background 

        #83df8e
        
        # ----- FONTS & COLORS -----
            #Bahnschrift SemiBold -- title
            #Segoe UI Semibold",20,'bold'))
            #bg="#f2f4f4",fg='#273746' #base

            #cyan / turquoise - miku color #14d3d9
            #lighter variant #a0d8da
            #darker variant #15a0a5
            #grayer variant #a0d8da
        #
        # --- VARS ---
        #entradas
        self.landa = tk.DoubleVar() #tasa de llegada λ
        self.miu = tk.DoubleVar() #tasa de servicio μ
        self.nCant = tk.IntVar() #nro. / cant. de clientes n
        self.tiempoEsp = tk.DoubleVar() #tiempo de espera t
        #salidas
        self.pRho = tk.DoubleVar() # p fea (Rho) -> factor de utilizacion (1 - P0) -> landa/ miu
        self.Lcant = tk.DoubleVar() # Cant. / nro. promedio de clientes en el sistema 
        self.Lq = tk.DoubleVar() # Cant. / nro. promedio de clientes en la COLA 
        self.Wprom = tk.DoubleVar() # Tiempo promedio/esperado de clientes en el sistema 
        self.Wq = tk.DoubleVar() # Tiempo promedio/esperado de clientes en la COLA 
        self.Po = tk.DoubleVar() # P0 = Po para este caso -> Probabilidad 0: cuando no hay clientes en el sistema/ sistema ocioso
        self.Pn = tk.DoubleVar() #Pn -> Probabilida de que existan n (nro.) promedio de clientes en el sistema (Proba. de n)
        self.kCant = tk.IntVar() #sea k una variable entera no negativa dada para comparar / nro de clientes para el cual estamos calculando P (L > k)
        #
        #LABEL MAIN
        self.lblMain=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Teoría de colas | Modelo de Colas MM1:",) #bg = background color, fg= foreground?color, font color basically
        self.lblMain.place(x=30,y=30)
        self.lblMain.configure(font=("Century Gothic",21,'bold'))
        #
        #LABEL TEXT
        self.lblText=tk.Label(self.window, bg="#f2f4f4",fg='#15a0a5',text="Para calcular las medidas de desempeño y diferentes probabilidades") #bg=
        self.lblText.place(x=35,y=68)
        self.lblText.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        #
        # ------------------- TASA DE LLEGADA - LANDA (λ)  -------------------
        #LABEL 
        self.lblLanda=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Tasa de Llegada (λ):") #bg=
        self.lblLanda.place(x=40,y=110)
        self.lblLanda.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxLanda=tk.Entry(self.window, textvariable=self.landa, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxLanda.place(x=220,y=112)
        self.tboxLanda.configure(font=("Segoe UI Semibold",14,'bold'))
        #self.tboxC=tk.Entry(self.window, textvariable=self.costo, bg="#def3b9", fg='black', width=10)    
        #
        # ------------------- MEDIA - MIU (μ) -------------------
        #LABEL 
        self.lblMiu=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Tasa de Servicio (μ):") #bg=
        self.lblMiu.place(x=482,y=110)
        self.lblMiu.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxMiu=tk.Entry(self.window, bg="#a0d8da", fg='#273746', width=8, textvariable=self.miu) #
        self.tboxMiu.place(x=668,y=112)
        self.tboxMiu.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- CANTIDAD (n) -------------------
        #LABEL
        self.lblnCant=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Nro de clientes¿ (n):") #bg=
        self.lblnCant.place(x=40,y=150)
        self.lblnCant.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxnCant=tk.Entry(self.window, textvariable=self.nCant, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxnCant.place(x=225,y=152)
        self.tboxnCant.configure(font=("Segoe UI Semibold",14,'bold'))

        # ------------------- TIEMPO DE ESPERA (t) -------------------
        #LABEL
        self.lblTiempot=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Tiempo de espera¿ (t):") #bg=
        self.lblTiempot.place(x=40,y=192)
        self.lblTiempot.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxTiempot=tk.Entry(self.window, textvariable=self.tiempoEsp, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxTiempot.place(x=240,y=195)
        self.tboxTiempot.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- RHO (p fea) -------------------
        #LABEL 
        self.lblPrho=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Factor de utilización (ro):") #bg=  ρ
        self.lblPrho.place(x=440,y=150)
        self.lblPrho.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxPrho=tk.Entry(self.window, textvariable=self.pRho, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxPrho.place(x=668,y=152)
        self.tboxPrho.configure(state='disabled',font=("Segoe UI Semibold",14,'bold'))
        #

        # ------------------- K - Cant. a comparar -------------------
        #sea k una variable entera no negativa dada para comparar / nro de clientes para el cual estamos calculando 
        # la probabilidad P ( L > k )
        #LABEL  --- lblKcomp -- kComparacion
        self.lblKcomp=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Valor mayor que, para prob. (k):") #bg=  ρ
        self.lblKcomp.place(x=380,y=190)
        self.lblKcomp.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxKcomp=tk.Entry(self.window, textvariable=self.kCant, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxKcomp.place(x=668,y=193)
        self.tboxKcomp.configure(font=("Segoe UI Semibold",14,'bold'))
        #self.cmbBoxTiempo.place(x=568,y=233)
        #
        # ------------------ MEDIDAS DE TIEMPO - COMBOBOX ----------------
        valueOfM=("horas","minutos","segundos")
        self.varMedidas=tk.StringVar() # --- *
        
        self.cmbBoxTiempo=ttk.Combobox(self.window,values=valueOfM, textvariable=self.varMedidas, font=("Segoe UI Semibold",12,'bold'), width=16)
        self.cmbBoxTiempo.place(x=570,y=273)
        #
        self.cmbBoxTiempo.configure(foreground='#273746',background="#f2f4f4")#

        self.lblMedidaTiempo=tk.Label(self.window, bg="#f2f4f4",fg='#15a0a5',text="Tiempo medido en:") #bg=
        self.lblMedidaTiempo.place(x=565,y=238)
        self.lblMedidaTiempo.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        # ------------------- CANT. DE CLIENTES EN SISTEMA - (L)  -------------------
        #LABEL 
        self.lblLcant=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Cantidad de clientes en el sistema (L):") #bg=
        self.lblLcant.place(x=40,y=240)
        self.lblLcant.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxLcant=tk.Entry(self.window, textvariable=self.Lcant, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxLcant.place(x=380,y=245)
        self.tboxLcant.configure(font=("Segoe UI Semibold",14,'bold'))
        #self.tboxC=tk.Entry(self.window, textvariable=self.costo, bg="#def3b9", fg='black', width=10)    
        #

        # ------------------- CANT. DE CLIENTES EN SISTEMA - (Lq)  -------------------
        #LABEL 
        self.lblLq=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Cantidad de clientes en la cola (Lq):") #bg=
        self.lblLq.place(x=40,y=285)
        self.lblLq.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxLq=tk.Entry(self.window, textvariable=self.Lq, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxLq.place(x=380,y=290)
        self.tboxLq.configure(font=("Segoe UI Semibold",14,'bold')) 
        #
        #
        # ------------------- TIEMPO DEL CLIENTE EN SISTEMA - (W)  -------------------
        #LABEL 
        self.lblW=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Tiempo promedio del cliente en el sistema (W):") #bg=
        self.lblW.place(x=40,y=340)
        self.lblW.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxW=tk.Entry(self.window, textvariable=self.Wprom, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxW.place(x=460,y=345)
        self.tboxW.configure(font=("Segoe UI Semibold",14,'bold')) 
        #
        #
        # ------------------- TIEMPO DEL CLIENTE EN SISTEMA - (Wq)  -------------------
        #LABEL 
        self.lblW=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Tiempo promedio del cliente en la cola (Wq):") #bg=
        self.lblW.place(x=40,y=390)
        self.lblW.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxW=tk.Entry(self.window, textvariable=self.Wq, bg="#a0d8da", fg='#273746', width=8) #
        self.tboxW.place(x=460,y=395)
        self.tboxW.configure(font=("Segoe UI Semibold",14,'bold')) 
        #
        # ------------------- PROBABILIDADES (varias) -------------------
        #LABEL
        self.lblProbs=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Probabilidades asociadas:") #bg=
        self.lblProbs.place(x=40,y=435)
        self.lblProbs.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxProb=tk.Text(self.window, bg="#a0d8da", fg='#273746', height=6, width=60) #
        self.tboxProb.place(x=280,y=450)
        self.tboxProb.configure(font=("Segoe UI Semibold",12,'bold'))
        
        # ------------------------ BUTTONS ---------------------------------------
        #BTN CALC -- MAIN CALC
        self.btnCalc=tk.Button(self.window, bg="#15a0a5",fg='#273746',text="Calcular",command=lambda:self.calcProbs()) #,command=lambda:self.calcProbs()
        self.btnCalc.place(x=205,y=600)
        self.btnCalc.configure(font=("Segoe UI Semibold",14,'bold'), cursor="hand2")

        #BTN CALC -- CLEAN ALL
        self.btnClean=tk.Button(self.window, bg="#15a0a5",fg='#273746',text="Limpiar", command=lambda:self.cleanAll()) #,command=lambda:self.cleanAll()
        self.btnClean.place(x=310,y=600) #with the past one x=490, ifnot, the x of the past one
        self.btnClean.configure(font=("Segoe UI Semibold",14,'bold'), cursor="hand2")
        #
    def cleanAll(self):
        self.miu.set('') #
        self.landa.set('') #
        self.pRho.set('')
        self.kCant.set('')
        self.nCant.set('') #
        self.tiempoEsp.set('') #
        self.Lcant.set('')
        self.Lq.set('') #
        self.Wprom.set('') #
        self.Wq.set('')
        self.tboxProb.delete("1.0",tk.END) # dede 1.0 hasta END; para que limpie desde inicio hasta fin del cont. del textarea
        #
    def calcProbs(self):
        #DATOS DE ENTRADA
        landa = self.landa.get()
        miu = self.miu.get()
        t = self.tiempoEsp.get()
        n = self.nCant.get()
        #
        #smtHere if landa / miu != None else messagebox.showwarning("Error!","Division entre 0")
        # CALCS INICIALES
        #
        if ((landa==0.0) or (miu==0.0)):
            messagebox.showerror("Error!","las tasas deben ser enteros positivos")
            return
        if(landa >= miu):
            messagebox.showwarning("Error!!!","Tasa Llegada debe ser menor que Tasa de servicio (landa<miu)")
            return
        #x = landa/miu
        try:
            pRho = round(landa / miu,2) 
            
            #if (landa / miu != None) else messagebox.showwarning("Error!","Division entre 0")
            self.pRho.set(pRho)
            #
            #
            L= round(landa/(miu-landa),2) 
            #if landa/(miu-landa)!= 0 else messagebox.showerror("Advertencia!", "Division entre 0, vuelva a intentar")
            # L= Cantidad promedio de clientes en el sistema 
            self.Lcant.set(L)

            Lq= round((landa**2)/(miu*(miu-landa)), 2) # Lq= Cantidad promedio de clientes en la cola
            self.Lq.set(Lq)

            W= round(1/(miu-landa),2) # W= Tiempo total del cliente en el sistema hasta ser atendido
            self.Wprom.set(W)

            Wq= round(pRho/(miu-landa),2) # Wq= Tiempo del cliente cuando esta en la cola
            self.Wq.set(Wq)
            # 
            # --- PROBABILIDADES --- POR FORMULA Y POR REQUISITO ESPECIFICO DEL ENUNCIADO
            # PROBS. "GENERALES":
            Po = (1 - pRho) #P0/Po= Promedio cuando no hay clientes en el sistema/para calcular tiempo ocioso
            #
            Pn = (1 - pRho ) * ( pRho ** n) #Pn= Nro. promedio de clientes en el sistema (Promedio de n) "
            #Por ejemplo, si es P1 (Probabilidad de que haya 1 cliente promedio en el sistema):
            #P1 = (1-pRho)* (pRho**1)

            # Para las probs de L usamos Pn
            #ProbL = Probabilidad de que P(L> n) ---> P (L > n) = 1 - sumaDe(P0 + P1 + ... = Pn)
            #entonces, para ProbL se debe primero calcular P0, luego P1, y asi cada Pn por el valor de n, luego 1 - suma de todas
            ProbW = exp((-1 * miu) * (1-pRho) * t)
            # PROBABS. POR REQUISITOS:
            """
                P3
                P(Wq>t) tal que t = 1 hora 
                P(L>5) 
            """
            #probabilidad de que existan tres pacientes en el sistema
            n3 = 3
            Pn3 = (1 - pRho ) * ( pRho ** n3) #Pn= Nro. promedio de clientes en el sistema (Promedio de n) "

            #probabilidad de que hayan más de 5 clientes -- P(L>5) ?
            #probabClientes= 0.0
            #n5 = 5
            # por k -> sea k la variable no negativa para comparar en la Prob de L 
            k = self.kCant.get()
            sumProbs = 0
            for i in range(k + 1):
                probN = (1 - pRho) * (pRho ** i) #por el n de esta probabilidad se calcula cada Pn
                sumProbs += probN #y se acumulan ( P (L > n)) = 1 - sumaDe(P0 + P1 + ... = Pn)
                #print(f"acum:{sumProbs}")
            probabClientes = 1 - sumProbs

            #ProbWq = Probabilidad de que (Wq > t) = pRho * e ^ (-miu * (1-pRho) * t)
            ProbWq = pRho * exp((-1 * miu) * (1-pRho) * t) 
            #
            #Se insertan los valores de las probs calcs en el textarea 
            self.tboxProb.insert(tk.END, f"Tiempo promedio de ocio del sist. (P0): {round(Po,2)}\n") #P0
            # * prueba tal q n por entrada para Pn
            #self.tboxProb.insert(tk.END, f"Si n:{n}, Pn: {round(Pn,2)}\n") #Pn por entrada
            #probabilidad de que existan tres pacientes en el sistema
            self.tboxProb.insert(tk.END, f"Probabilidad de que existan {n} pacientes en el sistema: {round(Pn3,2)}\n") #P3
            #self.tboxProb.insert(tk.END, f"Probabilidad de que existan 3 pacientes en el sistema: {round(Pn3,2)}\n") #P3
            #probabilidad de que el cliente espere más de una hora --- #(en cola)
            self.tboxProb.insert(tk.END, f" Probabilidad de que el cliente espere más de {t} hora(s) en cola: {round(ProbWq,2)}\n") #P(Wq > t) donde t = 1
            self.tboxProb.insert(tk.END, f" Probabilidad de que hayan más de {k} clientes: {round(probabClientes,2)}\n") #P(L > 5)
            #self.tboxProb.insert(tk.END, f" Probabilidad de que hayan más de 5 clientes: {round(probabClientes,2)}\n") #P(L > 5)
            #ProbW = exp((-1 * miu) * (1-pRho) * t)
            self.tboxProb.insert(tk.END, f" Probabilidad de que el cliente perdure más de {t} hora(s) en el sist.: {round(ProbW,2)}\n") #P(Wq > t) donde t = 1
            #   
        except ZeroDivisionError as e:
            messagebox.showerror("Error!", "{e}")
            return
        except ValueError as e:
            messagebox.showerror("Error!", "{e}")
            return
        #
    def runView(self):
        self.window.mainloop()
if (__name__=="__main__"):
    ModeloMM1().runView()


"""
FORMS DE PROBS GENERALES: PARA CUANDO ESTRICTAMENTE POR TIPEO
#Para P(Ls > n)
    #VERS. GENERAL
    for i in range(n + 1):
        probN = (1 - pRho) * (pRho ** i) #si n=5, por c/i(val) de n se calcula cada Pn (i=1, ...)
        sumProbs += probN #y se acumulan ( P (L > n)) = 1 - sumaDe(P0 + P1 + ... = Pn)
        print(f"acum:{sumProbs}")
    probabClientes = 1 - sumProbs
#Para P (W > t)
# P(W > t) = e ^ -miu * (1-pRho) * t
ProbW = exp((-1 * miu) * (1-pRho) * t)
#Para P(Wq > t)
# P(Wq > t) = pRho * e ^ (-miu * (1-pRho) * t)
ProbWq = pRho * exp((-1 * miu) * (1-pRho) * t)

"""

#slayT = "slay" -> prueba inicial con el text area --- self.tboxProb.insert(tk.END, f"Valor 2: {slayT}\n")
#self.tboxProb.insert(tk.END, "Resultados de los cálculos:\n")