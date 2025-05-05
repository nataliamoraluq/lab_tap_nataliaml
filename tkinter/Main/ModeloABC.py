import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import *
#from scipy.stats import norm
#import matplotlib.pyplot as plt


class ModeloABC():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("MODELO DE CLASIFICACION ABC")
        self.window.geometry("870x690") # width x heigth
        self.window.resizable(0,0) #non resizable 0,0
        self.window.config(bg='#f2f4f4') #background 

        #83df8e
        
        # ----- FONTS & COLORS -----
            #Bahnschrift SemiBold -- title
            #Segoe UI Semibold",20,'bold'))
            #bg="#f2f4f4",fg='#273746' #base

            #dark green color #f2f4f4
        #
        # --- VARS ---

        #LABEL MAIN
        self.lblMain=tk.Label(self.window, bg="#f2f4f4",fg='#273746',text="Modelo | Clasificación ABC de productos:",) #bg = background color, fg= foreground?color, font color basically
        self.lblMain.place(x=30,y=30)
        self.lblMain.configure(font=("Century Gothic",21,'bold'))
        #
        #LABEL TEXT
        self.lblText=tk.Label(self.window, bg="#f2f4f4",fg='#138d75',text="Para clasificar los productos de una base de datos dada (csv)") #bg=
        self.lblText.place(x=35,y=68)
        self.lblText.configure(font=("Segoe UI Semibold",14,'bold'))
        #
        #
        # ------------------- -------------------
    def runView(self):
        self.window.mainloop()
if (__name__=="__main__"):
    ModeloABC().runView()
