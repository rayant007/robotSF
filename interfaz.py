import math
import serial
from tkinter import *

arduino_port = "COM4"  # Reemplaza con el puerto correcto en el que está conectado tu Arduino
arduino_baudrate = 9600  # Reemplaza con la velocidad de comunicación correcta

arduino = None  # Variable para almacenar la conexión serial con Arduino


raiz=Tk()

raiz.title("Interfaz")

raiz.configure(bg="#7092BE")

def calcular_md():
    q1 = float(texto_q1.get())
    q2 = float(texto_q2.get())
    q3 = float(texto_q3.get())
    z=q2-3.1
    tanr2 = 2/(q3+10.3)
    t2_rad = math.atan(tanr2)
    t2 = math.degrees(t2_rad)
    y=2/math.tan(t2)
    rx=q3**2
    rx2=(20.6*q3)
    rx3=y**2
    rx4=rx+rx2+110.09-rx3
    x=math.sqrt(rx4)
    tanr1= y/x
    t1_grados = math.atan(tanr1)
    t1 = math.degrees(t1_grados)
    texto_x.delete(0, END)
    texto_x.insert(0, float(x))
    texto_y.delete(0, END)
    texto_y.insert(0, float(y))
    texto_z.delete(0, END)
    texto_z.insert(0, float(z))
    texto_t1.delete(0, END)
    texto_t1.insert(0, float(t1))
    texto_t2.delete(0, END)
    texto_t2.insert(0, float(t2))
    actualizar_matrices(q1, q2, q3)
    pass

def calcular_mi():
    x = float(texto_x.get())
    y = float(texto_y.get())
    z = float(texto_z.get())
    t1 = float(texto_t1.get())
    t2 = float(texto_t2.get())
    rr=(x*x)+(y*y)-4
    q1=t1+t2
    q2=z+3.1
    rr2=math.sqrt(rr)
    q3=rr2-10.3
    texto_q1.delete(0, END)
    texto_q1.insert(0, float(q1))
    texto_q2.delete(0, END)
    texto_q2.insert(0, float(q2))
    texto_q3.delete(0, END)
    texto_q3.insert(0, float(q3))
    calcular_md()
    pass

def phome():
    pass

def actualizar_matrices(q1, q2, q3):

    q1 = math.radians(q1)
    q2=q2
    q3=q3
    cos_q1 = math.cos(q1)
    sen_q1 = math.sin(q1)
    sr1=q3+10.3
    sr2=q2-3.1
    r1 = (-sr1*cos_q1)-(2*sen_q1)
    r2 = (-sr1*sen_q1)+(2*cos_q1)
    r3= (-sr2*cos_q1)+(2*sen_q1)
    

    if abs(cos_q1) < 1e-10:
        cos_q1 = 0
    if abs(sen_q1) < 1e-10:
        sen_q1 = 0

     # Matriz 1
    matriz1_labels = matriz1.winfo_children()  # Obtener las etiquetas dentro de la matriz1
    matriz2_labels = matriz2.winfo_children()
    matriz3_labels = matriz3.winfo_children() 
    matriz4_labels = matriz4.winfo_children() 
    matriz1_labels[0].config(text="{:.2f}".format(-cos_q1))
    matriz1_labels[1].config(text="{:.2f}".format(sen_q1))
    matriz1_labels[4].config(text="{:.2f}".format(-sen_q1))
    matriz1_labels[5].config(text="{:.2f}".format(-cos_q1))
    matriz1_labels[9].config(text="{:.2f}".format(-sen_q1))
    matriz1_labels[10].config(text="{:.2f}".format(-cos_q1))
    matriz2_labels[11].config(text="{:.2f}".format(q2+4.3))
    matriz3_labels[11].config(text="{:.2f}".format(q3+10.3))
    matriz4_labels[2].config(text="{:.2f}".format(-cos_q1))
    matriz4_labels[3].config(text="{:.2f}".format(r1))
    matriz4_labels[6].config(text="{:.2f}".format(-sen_q1))
    matriz4_labels[7].config(text="{:.2f}".format(r2))
    matriz4_labels[8].config(text="{:.2f}".format(cos_q1))
    matriz4_labels[11].config(text="{:.2f}".format(r3))
    pass

def conectar_robot():
    # Aquí puedes implementar la lógica para conectar al robot
    global arduino
    
    try:
        arduino = serial.Serial(arduino_port, arduino_baudrate)
        print("Conexión con Arduino establecida")
    except serial.SerialException:
        print("Error al conectar con Arduino")
    pass

# Crear el contenedor principal

# Título: Modelo Directo
contenedor = Frame(raiz)
contenedor.grid(row=0, column=0, padx=10, pady=10)
contenedor.configure(bg="#7092BE")

contenedor2 = Frame(raiz)
contenedor2.grid(row=0, column=1, padx=10, pady=10)
contenedor2.configure(bg="#7092BE")

contenedor_matrices = Frame(raiz)
contenedor_matrices.grid(row=0, column=2, padx=10, pady=10)
contenedor_matrices.configure(bg="#7092BE")

contenedor_conectar_robot = Frame(raiz)
contenedor_conectar_robot.grid(row=3, column=0, padx=10, pady=10)

contenedor_home = Frame(raiz)
contenedor_home.grid(row=4, column=0, padx=10, pady=10)


titulo = Label(contenedor, text="Modelo Directo", font=("Arial", 16, "bold"))
titulo.pack()
titulo.configure(bg="#7092BE")

# Textos q1 y q2
label_q1 = Label(contenedor, text="q1:")
label_q1.pack()
label_q1.configure(bg="#7092BE")
texto_q1 = Entry(contenedor)
texto_q1.pack()

label_q2 = Label(contenedor, text="q2:")
label_q2.pack()
label_q2.configure(bg="#7092BE")
texto_q2 = Entry(contenedor)
texto_q2.pack()

# Texto q3
label_q3 = Label(contenedor, text="q3:")
label_q3.pack()
label_q3.configure(bg="#7092BE")
texto_q3 = Entry(contenedor)
texto_q3.pack()

# Botón Calcular MD
boton_calcular = Button(contenedor, text="Calcular MD", command=calcular_md)
boton_calcular.pack()
boton_calcular.configure(bg="#3F48CC")

# Título: Modelo Inverso
titulo2 = Label(contenedor2, text="Modelo Inverso", font=("Arial", 16, "bold"))
titulo2.pack()
titulo2.configure(bg="#7092BE")

label_x = Label(contenedor2, text="x:")
label_x.pack()
label_x.configure(bg="#7092BE")
texto_x = Entry(contenedor2)
texto_x.pack()

label_y = Label(contenedor2, text="y:")
label_y.pack()
label_y.configure(bg="#7092BE")
texto_y = Entry(contenedor2)
texto_y.pack()

label_z = Label(contenedor2, text="z:")
label_z.pack()
label_z.configure(bg="#7092BE")
texto_z = Entry(contenedor2)
texto_z.pack()

label_t1 = Label(contenedor2, text="θ1:")
label_t1.pack()
label_t1.configure(bg="#7092BE")
texto_t1 = Entry(contenedor2)
texto_t1.pack()

label_t2 = Label(contenedor2, text="θ2:")
label_t2.pack()
label_t2.configure(bg="#7092BE")
texto_t2 = Entry(contenedor2)
texto_t2.pack()

# Botón Calcular MI
boton_calcular2 = Button(contenedor2, text="Calcular MI", command=calcular_mi)
boton_calcular2.pack()
boton_calcular2.configure(bg="#3F48CC")

boton_home = Button(contenedor_home, text="Posicion Home", command=phome)
boton_home.pack()
boton_home.configure(bg="#3F48CC")

# Matriz 1
matriz1_frame = Frame(contenedor_matrices, borderwidth=1, relief="solid")
matriz1_frame.pack(side=LEFT, padx=5, pady=5)
matriz1_frame.configure(bg="#7092BE")

label_matriz1 = Label(matriz1_frame, text="A1")
label_matriz1.pack()
label_matriz1.configure(bg="#7092BE")

matriz1 = Frame(matriz1_frame, borderwidth=1, relief="solid")
matriz1.pack()

for i in range(4):
    for j in range(4):
        label = Label(matriz1, text="0", width=4, height=2, borderwidth=1, relief="solid")
        label.grid(row=i, column=j)

label15m1=matriz1.winfo_children()[15]
label15m1.config(text="1")

# Matriz 2
matriz2_frame = Frame(contenedor_matrices, borderwidth=1, relief="solid")
matriz2_frame.pack(side=LEFT, padx=5, pady=5)
matriz2_frame.configure(bg="#7092BE")

label_matriz2 = Label(matriz2_frame, text="A2")
label_matriz2.pack()
label_matriz2.configure(bg="#7092BE")

matriz2 = Frame(matriz2_frame, borderwidth=1, relief="solid")
matriz2.pack()

for i in range(4):
    for j in range(4):
        label = Label(matriz2, text="0", width=4, height=2, borderwidth=1, relief="solid")
        label.grid(row=i, column=j)
label2m2=matriz2.winfo_children()[2]
label2m2.config(text="1")

label4m2=matriz2.winfo_children()[4]
label4m2.config(text="-1")

label7m2=matriz2.winfo_children()[7]
label7m2.config(text="-2")

label9m2=matriz2.winfo_children()[9]
label9m2.config(text="-1")

label15m2=matriz2.winfo_children()[15]
label15m2.config(text="1")

# Matriz 3
matriz3_frame = Frame(contenedor_matrices, borderwidth=1, relief="solid")
matriz3_frame.pack(side=LEFT, padx=5, pady=5)
matriz3_frame.configure(bg="#7092BE")

label_matriz3 = Label(matriz3_frame, text="A3")
label_matriz3.pack()
label_matriz3.configure(bg="#7092BE")

matriz3 = Frame(matriz3_frame, borderwidth=1, relief="solid")
matriz3.pack()

for i in range(4):
    for j in range(4):
        label = Label(matriz3, text="0", width=4, height=2, borderwidth=1, relief="solid")
        label.grid(row=i, column=j)

label4m3=matriz3.winfo_children()[4]
label4m3.config(text="1")

label7m3=matriz3.winfo_children()[7]
label7m3.config(text="7.5")

label10m3=matriz3.winfo_children()[10]
label10m3.config(text="1")

label15m3=matriz3.winfo_children()[15]
label15m3.config(text="1")

# Matriz 4
matriz4_frame = Frame(contenedor_matrices, borderwidth=1, relief="solid")
matriz4_frame.pack(side=LEFT, padx=5, pady=5)
matriz4_frame.configure(bg="#7092BE")

label_matriz4 = Label(matriz4_frame, text="T")
label_matriz4.pack()
label_matriz4.configure(bg="#7092BE")

matriz4 = Frame(matriz4_frame, borderwidth=1, relief="solid")
matriz4.pack()

for i in range(4):
    for j in range(4):
        label = Label(matriz4, text="0", width=4, height=2, borderwidth=1, relief="solid")
        label.grid(row=i, column=j)

label15m4=matriz4.winfo_children()[15]
label15m4.config(text="1")

# Botón Conectar al Robot
boton_conectar_robot = Button(contenedor_conectar_robot, text="Conectar al Robot", command=conectar_robot)
boton_conectar_robot.configure(bg="#3F48CC")
boton_conectar_robot.pack()

raiz.mainloop()
