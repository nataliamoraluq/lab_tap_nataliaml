import tkinter as tk
from pruebaMenu import MenuPrincipal

def showMenu():
    ventana_menu = tk.Tk()
    menu = MenuPrincipal(ventana_menu)
    ventana_menu.mainloop()
showMenu()
"""
ventana_app = tk.Tk()
ventana_app.title("Aplicación Principal")

boton_mostrar_menu = tk.Button(ventana_app, text="Mostrar Menú", command=showMenu)
boton_mostrar_menu.pack(pady=20)

ventana_app.mainloop()"""