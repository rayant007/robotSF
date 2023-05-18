import tkinter as tk
from tkinter import ttk



# Crear una instancia de la ventana
ventana = tk.Tk()

# Personalizar la ventana
ventana.title("RobotController")
ventana.geometry("1080x720")  # ancho x alto en píxeles



#ttk.Label(ventana, text="buton 1").grid(column=0, row=0)
botonW = ttk.Button(ventana, text="W", command=ventana.destroy)
botonW.place(x=150, y=501)
botonS = ttk.Button(ventana, text="S", command=ventana.destroy)
botonS.place(x=150,y=530)
botonA = ttk.Button(ventana, text="A", command=ventana.destroy)
botonA.place(x=58,y=530)
botonD = ttk.Button(ventana, text="D", command=ventana.destroy)
botonD.place(x=242,y=530)



# Ejecutar el bucle principal de la ventana
ventana.mainloop()