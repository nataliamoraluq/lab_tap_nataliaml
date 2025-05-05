import tkinter as tk
import subprocess
import os

#check all this out again, it does work already but as we already  
#have a menu we just know need to make it better
#this for the end, first all models working and then this :D

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Menú Principal (Clase)")

        self.barra_menu = tk.Menu(master)
        self.menu_ejercicios = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="PROYECTO LAB TOPICOS", menu=self.menu_ejercicios)

        #self.menu_ejercicios.add_command(label="Abrir Ventana Textarea", command=self.abrir_ventana_textarea)
        self.menu_ejercicios.add_command(label="Acceder al Menu", command=self.openMenu)
        self.menu_ejercicios.add_separator()
        self.menu_ejercicios.add_command(label="Salir", command=master.quit)

        master.config(menu=self.barra_menu)

    def openMenu(self):
        #ruta_suma = os.path.join('dataPruebas', 'suma.py')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_suma = os.path.join(script_dir, 'Menu.py')
        try:
            subprocess.Popen(['python', ruta_suma])
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_suma}")

if __name__ == '__main__':
    root = tk.Tk()
    menu_principal = MenuPrincipal(root)
    root.mainloop()