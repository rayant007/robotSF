import tkinter as tk
from tkinter import ttk
#from PIL import Image
from PIL import Image, ImageTk
#from tkinter import *


# Crear una instancia de la ventana
ventana = tk.Tk()

#cargar imagen
try:
    img1 = Image.open("/home/rayant/Documents/pythonPrograms/robotSF/robotSF/robotPng.png")
    resizeImg = img1.resize((400,300))
    imagen = ImageTk.PhotoImage(resizeImg)
except:
    print('no ha sido posible cargar la imagen 1')



# Personalizar la ventana
ventana.title("RobotController")
ventana.geometry("900x600")  # ancho x alto en píxeles



#cargar imagen convertida
try:
    #imagen = ImageTk.PhotoImage(file="/home/rayant/Documents/pythonPrograms/robotSF/robotSF/robotPng_converted.png")
    robotFondoImg = tk.Label(ventana, image=imagen)
    robotFondoImg.place(x=10,y=10)
except:
    print('No ha sido posible cargar la imagen convertida 2')

#ttk.Label(ventana, text="buton 1").grid(column=0, row=0)
botonW = ttk.Button(ventana, text="W", command=ventana.destroy).place(x=150, y=501)
botonS = ttk.Button(ventana, text="S", command=ventana.destroy).place(x=150,y=530)
botonA = ttk.Button(ventana, text="A", command=ventana.destroy).place(x=58,y=530)
botonD = ttk.Button(ventana, text="D", command=ventana.destroy).place(x=242,y=530)



# Ejecutar el bucle principal de la ventana
ventana.mainloop()