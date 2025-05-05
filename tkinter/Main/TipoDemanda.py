import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import *

class DemandaTipo():
    def __init__(self) -> None:
        #------- MAIN WINDOW / CANVAS -------
        self.window = tk.Tk()
        self.window.title("METODO TIPO DE DEMANDA")
        self.window.geometry("510x335") # width x heigth
        self.window.resizable(0,0) #non resizable 0,0
        self.window.config(bg='#f2f4f4') #background 
        
        # ----- FONTS & COLORS -----
            #Bahnschrift SemiBold -- title
            #Segoe UI Semibold",20,'bold'))
            #bg="#f2f4f4",fg='#273746'
        #
        # --- VARS ---
        #
        self.demanda = tk.DoubleVar() #valor i en vectorD
        self.vectorD = []
        #self.barraD = # d barra, promedio, barraD = sum(demanda)/n
        self.pValue = tk.DoubleVar() #valor de la probabilidad
        #n = len(barraD)
        #self.sVal = tk.DoubleVar() #desviac. estandar calculada
        self.tipoDemanda = tk.StringVar()
        
        #
        #LABEL MAIN
        self.lblMain=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Clasificación de Demanda:",) #bg = background color, fg= foreground?color, font color basically
        self.lblMain.place(x=30,y=30)
        self.lblMain.configure(font=("Century Gothic",20,'bold'))
        #
        #LABEL TEXT
        self.lblText=tk.Label(self.window, bg="#f2f4f4",fg='#76448a',text="Para determinar si la demanda es DETERMINISTICA o PROBABILISTICA: ") #bg=
        self.lblText.place(x=35,y=68)
        self.lblText.configure(font=("Segoe UI Semibold",10,'bold'))
        #
        #LABEL TEXT 2
        self.lblText2=tk.Label(self.window, bg="#f2f4f4",fg='#76448a',text="Ingresa cada valor de la lista Demanda y el valor de la probabilidad") #bg=
        self.lblText2.place(x=35,y=88)
        self.lblText2.configure(font=("Segoe UI Semibold",10,'bold'))
        #
        #
        # # ------------------ MEDIDAS DE TIEMPO - COMBOBOX ----------------
        """
        valueOfM=("dias","semanas","meses","años")
        self.varMedidas=tk.StringVar() # --- *
        
        self.cmbBoxTiempo=ttk.Combobox(self.window,values=valueOfM, textvariable=self.varMedidas, font=("Segoe UI Semibold",12,'bold'), width=16)
        self.cmbBoxTiempo.place(x=380,y=120)
        #self.lblTiempoL.place(x=120,y=150)
        self.cmbBoxTiempo.configure(foreground='#273746',background="#f2f4f4")#

        self.lblMedidaTiempo=tk.Label(self.window, bg="#83df8e",fg='#ff5731',text="Todos los valores en:") #bg=
        self.lblMedidaTiempo.place(x=380,y=90)
        self.lblMedidaTiempo.configure(font=("Segoe UI Semibold",12,'bold')) 
        """

        # ------------------- VALOR DEMANDA -------------------
        #LABEL 
        self.lblDemanda=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Demanda (d):") #bg=
        self.lblDemanda.place(x=40,y=125)
        self.lblDemanda.configure(font=("Segoe UI Semibold",13,'bold'))
        #TEXTBOX 
        self.tboxD=tk.Entry(self.window, textvariable=self.demanda, bg="#e8daef", fg='#273746', width=10,) #
        self.tboxD.place(x=180,y=130)
        self.tboxD.configure(font=("Segoe UI Semibold",13,'bold'))
        # ------------------- BUTTON ADD -------------------
        self.btnAdd=tk.Button(self.window, bg="#d7bde2",fg='#273746',text="Agregar",command=lambda:self.addToArray())#, command=self.metHere() 
        self.btnAdd.place(x=285,y=125)
        self.btnAdd.configure(font=("Segoe UI Semibold",12,'bold'), cursor="hand2")
        # ------------------- BUTTON LIMPIAR -------------------
        self.btnAdd=tk.Button(self.window, bg="#d7bde2",fg='#273746',text="Limpiar todo",command=lambda:self.cleanAll())#, command=self.metHere() 
        self.btnAdd.place(x=370,y=125)
        self.btnAdd.configure(font=("Segoe UI Semibold",12,'bold'), cursor="hand2")
        # ------------------- VALOR P - PROBABILIDAD -------------------
        #LABEL 
        self.lblProb=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Probabilidad (p):") #bg=
        self.lblProb.place(x=40,y=165)
        self.lblProb.configure(font=("Segoe UI Semibold",13,'bold'))
        #TEXTBOX 
        self.tboxP=tk.Entry(self.window, textvariable=self.pValue, bg="#e8daef", fg='#273746', width=10,) #
        self.tboxP.place(x=180,y=170)
        self.tboxP.configure(font=("Segoe UI Semibold",13,'bold'))
        #
        # ------------------- BUTTON TIPO DEMANDA -------------------
        self.btnDet=tk.Button(self.window, bg="#d7bde2",fg='#273746',text="Determinar",command=lambda:self.typeOfD()) #
        self.btnDet.place(x=310,y=170)
        self.btnDet.configure(font=("Segoe UI Semibold",12,'bold'), cursor="hand2")
        #
        # ------------------- TIPO DE DEMANDA -------------------
        #LABEL 
        self.lblTipoD=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="La lista Demanda dada es:") #bg=
        self.lblTipoD.place(x=40,y=225)
        self.lblTipoD.configure(font=("Segoe UI Semibold",14,'bold'))
        #TEXTBOX 
        self.tboxTipoD=tk.Entry(self.window, textvariable=self.tipoDemanda, bg="#e8daef", fg='#273746', width=32) #
        self.tboxTipoD.place(x=44,y=268)
        self.tboxTipoD.configure(font=("Segoe UI Semibold",14,'bold'))

        #self.window.mainloop()   
    def runView(self):
        #este metodo es solo para llamar la instancia con el mainloop que 
        #generara la ventana / carga la ventana
        #se hace por cada ventana para que se muestre solo al momento de llamarlo en el Menu
        self.window.mainloop() 
    def cleanAll(self):
        self.demanda.set('')
        self.pValue.set('')
        self.tipoDemanda.set('')
    def addToArray(self):
        try:
            self.vectorD.append(self.demanda.get())
        except Exception:
            messagebox.showerror("Error! Valor demanda", "el valor de la demanda debe ser de tipo numerico!")
            return
        self.demanda.set('')
    def typeOfD(self):
        try:
            if(self.vectorD!=NONE):
                #
                arrayD = self.vectorD.copy()
                n = len(arrayD)
                #n = self.vectorD.count()
                p = self.pValue.get()
                #self.vectorD.get()
                barraD = sum(self.vectorD)/n

                """
                        #
                    self.demanda = tk.DoubleVar() #valor i en vectorD
                    self.vectorD = []
                    #self.barraD = # d barra, promedio, barraD = sum(demanda)/n
                    self.pValue = tk.DoubleVar() #valor de la probabilidad
                    #n = len(barraD)
                    #self.sVal = tk.DoubleVar() #desviac. estandar calculada
                    self.tipoDemanda = tk.StringVar()
                """
                #dBar = sum(D) / n
                des = ((sum([x ** 2 for x in arrayD])) - n*(pow(barraD,2))) / n - 1
                s = pow(des,2)/(pow(barraD,2))
                if(s<p):
                    self.tipoDemanda.set("tipo deterministica")
                    print(f"la demanda es deterministica")
                    print(f"demanda = {arrayD}")
                else:
                    self.tipoDemanda.set("tipo probabilistica")
                    print(f"la demanda es probabilistica")
                    print(f"demanda = {arrayD}")
                print("\n")
            else:
                messagebox.showerror("Error! Lista vacía", "Llena la lista de demanda!")
                #
        except Exception:
            messagebox.showerror("Error!", "Ningun valor debe estar vacío!")
            return
        
#--------------------------------%------------------------------%------------------------------%------------------------------
if (__name__=="__main__"):
    DemandaTipo().runView()

#--------------------------------%------------------------------%------------------------------%------------------------------
"""
#si fuera una sola ventana esto es una opcion
#pero cm ahora estamos usando menu, unicamente 
#usamos esto en el menu y un poco mas directo
#main
def main():
    DemandaTipo()
#main - llamado de la clase
if (__name__=="__main__"):
    main()
"""