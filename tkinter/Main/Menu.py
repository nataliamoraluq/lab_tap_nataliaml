import tkinter as tk
from tkinter import *

import tkinter as tk
import subprocess
import os

#from tkinter import messagebox
from tkinter import ttk

class Menu: #
    def __init__(self) -> None:
        #------- MAIN WINDOW / CANVAS -------
        self.window = tk.Tk()
        self.window.title("Menu")
        self.window.geometry("600x400") # width x heigth
        self.window.resizable(0,0) #non resizable 0,0
        self.window.config(bg='#d4e6f1') #background color
        #== FONTS ==
        #Bahnschrift SemiBold -- title
        #Segoe UI Semibold",20,'bold'))
        #
        # --- VARS (IF SO) ---
        #
        #LABEL MAIN
        self.lblMain=tk.Label(self.window, bg="#d4e6f1",fg='#3498db',text="Menú:",) #bg = background color, fg= foreground?color, font color basically
        self.lblMain.place(x=30,y=30)
        self.lblMain.configure(font=("Century Gothic",28,'bold'))
        #LABEL
        self.lblText=tk.Label(self.window, bg="#d4e6f1",fg='#1a5276',text="Selecciona una opción para iniciar:",) #bg=
        self.lblText.place(x=35,y=90)
        self.lblText.configure(font=("Segoe UI Semibold",18,'bold'))
        # TEXTS - WELCOMING
        self.lblText2=tk.Label(self.window, bg="#d4e6f1",fg='#1a5276',text="Hola! Bienvenido, gestiona tu inventario ") #bg=
        self.lblText3=tk.Label(self.window, bg="#d4e6f1",fg='#1a5276',text="digital fácil y rápido con nosotros")
        self.lblText2.place(x=260,y=30)
        self.lblText2.configure(font=("Segoe UI Semibold",12,'italic','bold')) #,'bold'
        self.lblText3.place(x=302,y=55)
        self.lblText3.configure(font=("Segoe UI Semibold",12,'italic','bold')) #,'bold'

        #MEDIDAS DE TIEMPO - COMBOBOX
        """
        #valueOfM=("dias","semanas","meses","años")
        valueOfM=("diario","semanal","mensual","anual")
        self.varMedTiempo=tk.StringVar() # --- *
        
        self.cmbBoxMedTiempo=ttk.Combobox(self.window,values=valueOfM, textvariable=self.varMedTiempo, font=("Segoe UI Semibold",10,'bold'), width=16)
        self.cmbBoxMedTiempo.place(x=440,y=60)
        self.cmbBoxMedTiempo.configure(foreground='#1a5276',background="#d4e6f1")#,state='radonly'
        """
        # BUTTONS

        #self.window.add_command(label="Acceder al Menu", command=self.openLote)
        #self.menu_ejercicios.add_command(label="Acceder al Menu", command=self.openMenu)
        # ABC
        self.btnABC=tk.Button(self.window, bg="#d4e6f1",fg='#1a5276',text="Modelo de Clasificación ABC")# ,command=lambda:self.openABC()
        self.btnABC.place(x=50,y=145)
        self.btnABC.configure(font=("Segoe UI Semibold",14,'bold'))
        # DESCUENTO
        self.btnDesc=tk.Button(self.window, bg="#d4e6f1",fg='#1a5276',text="Modelo de Descuento")# ,command=lambda:self.openDescuento()
        self.btnDesc.place(x=320,y=145)

        self.btnDesc.configure(font=("Segoe UI Semibold",14,'bold'))
        # Lote economico
        self.btnLote=tk.Button(self.window, bg="#d4e6f1",fg='#1a5276',text="Modelo de Lote Económico",command=lambda:self.openLote()) #,command=lambda:self.loteEconom()
        self.btnLote.place(x=50,y=200)
        self.btnLote.configure(font=("Segoe UI Semibold",14,'bold'))
        # Probabilidades
        self.btnProbs=tk.Button(self.window, bg="#d4e6f1",fg='#1a5276',text="Modelo Probabilístico",command=lambda:self.openProb())#,command=lambda:self.modeloProb()
        self.btnProbs.place(x=320,y=200)
        self.btnProbs.configure(font=("Segoe UI Semibold",14,'bold'))
        # Tipo de demanda
        self.btnDemandaTipo=tk.Button(self.window, bg="#d4e6f1",fg='#1a5276',text="Met. para determinar tipo de Demanda",command=lambda:self.openTipoDemanda())#,command=lambda:self.tipoDemanda()
        self.btnDemandaTipo.place(x=50,y=255)
        self.btnDemandaTipo.configure(font=("Segoe UI Semibold",14,'bold'))
        # Teoria de Colas M/M/1
        self.btnTeoriaColas=tk.Button(self.window, bg="#d4e6f1",fg='#1a5276',text="Modelo M/M/1 (Teoría de Colas)",command=lambda:self.openMM1())#, command=self.metHere() 
        self.btnTeoriaColas.place(x=50,y=310)
        self.btnTeoriaColas.configure(font=("Segoe UI Semibold",14,'bold'))
        #self.window.mainloop()
    def run(self):
        self.window.mainloop()
    def openABC(self):
        #ruta_suma = os.path.join('dataPruebas', 'suma.py')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_suma = os.path.join(script_dir, 'ModeloABC.py')
        try:
            subprocess.Popen(['python', ruta_suma])
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_suma}")
    def openDescuento(self):
        #ruta_suma = os.path.join('dataPruebas', 'suma.py')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_suma = os.path.join(script_dir, 'ModeloDescuento.py')
        try:
            subprocess.Popen(['python', ruta_suma])
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_suma}")
    def openLote(self):
        #ruta_suma = os.path.join('dataPruebas', 'suma.py')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_suma = os.path.join(script_dir, 'LoteEconomico.py')
        try:
            subprocess.Popen(['python', ruta_suma])
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_suma}")
    def openTipoDemanda(self):
        #ruta_suma = os.path.join('dataPruebas', 'suma.py')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_suma = os.path.join(script_dir, 'TipoDemanda.py')
        try:
            subprocess.Popen(['python', ruta_suma])
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_suma}")
    def openProb(self):
        #ruta_suma = os.path.join('dataPruebas', 'suma.py')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_suma = os.path.join(script_dir, 'ModeloProbabilistico.py')
        try:
            subprocess.Popen(['python', ruta_suma])
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_suma}")
    def openMM1(self):
        #ruta_suma = os.path.join('dataPruebas', 'suma.py')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_suma = os.path.join(script_dir, 'ModeloMM1.py')
        try:
            subprocess.Popen(['python', ruta_suma])
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_suma}")
    """ 
    def loteEconom(self):
        LoteEconom().runView()
    def modeloProb(self):
        ModeloProb().runView()    
    def tipoDemanda(self):
        DemandaTipo().runView()
       
    def modeloABC(self):
        ModeloABC().runView()
    def modeloDesc(self):
        ModeloDcto().runView()
    def modeloMM1(self): #Modelo MM1 de teoria de colas
        TeoriaDeColas().runView()
    """

#--------------------------------%------------------------------%------------------------------%------------------------------
if (__name__=="__main__"):
    Menu().run()
    #main()
    #window.window.mainloop()
    #-----------------------------------------
    #ventanaB = B()
    #ventanaB.ventanaB.mainloop()
    #self.window.mainloop()   
#--------------------------------%------------------------------%------------------------------%------------------------------
"""def main():
    objMenu = Menu()
    #Menu().mainloop()"""

#(dentro de la def __init__ self)
"""
    self.contT = 0
    self.varX2 = tk.StringVar()
#
#
#
        self.lblTryal=tk.Label(self.window, bg="#d4e6f1",fg='#1a5276',text="Aqui va la prueba del acum") #bg=
        self.lblTryal.place(x=50,y=120)
        self.lblTryal.configure(font=("Segoe UI Semibold",18,'bold'))
        #HOW TO GET, SET N USE THE INPUTS AND THEIR VALUES
        # FIRST WE DECLARE? THE VAR (UP THERE) AND THE TYPE OF 
        # WITH textvariable=self.varHere
        self.textTryal = tk.Entry(self.window, background="light gray", width=12, textvariable=self.varX2) 
        self.textTryal.place(x=70,y=110)

        #THEN WITH command=lambda:self.funcHere()
        #!!! *: without the " lambda: " doesn't work for some reason XDDD check this later
        #BUTTONS **
        
        self.btnX=tk.Button(self.window, bg="#a58db8",fg='#ffffff',text="limpiar", command=lambda:self.cleanAll())#, command=self.CreateClient 
        self.btnX.place(x=100,y=235)
        self.btnX.configure(font=("Arial",16,'bold'))

        self.btnY=tk.Button(self.window, bg="#a58db8",fg='#ffffff',text="acumula", command=lambda:self.ChangeNumb())#, command=self.CreateClient 
        self.btnY.place(x=180,y=235)
        self.btnY.configure(font=("Arial",16,'bold'))

        #
    """
    #------------------------------%------------------------------%------------------------------
    #luego fuera del __init__
    #prueba de input y output con acum 
    #then here with a funct/met
"""def ChangeNumb(self):
        #this for example, for a counter
        self.contT = self.contT+1
        self.varX2.set(self.contT)
    #
    def cleanAll(self):
        #and this to clean
        self.contT = 0
        self.varX2.set("")"""