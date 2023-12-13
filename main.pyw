import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from gui import funciones

# Crear la ventana principal
root = tk.Tk()
root.title("Transformacion de csv")
root.geometry("700x500")
root.resizable(0, 0)

#color
root.configure(bg="#A69CAC")

# Crear un frame principal
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill="both")

# Crear un frame superior (1/6 de la ventana hacia arriba)
top_frame = ttk.Frame(main_frame)
top_frame.grid(row=0, column=0, sticky="nsew")

# Crear un frame inferior (5/6 de la ventana hacia abajo)
bottom_frame = ttk.Frame(main_frame)
bottom_frame.grid(row=1, column=0, sticky="nsew")

# Configurar el peso de las filas para que el top_frame ocupe 1/6 de la ventana
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=5)

# Configurar el peso de las columnas para que los frames se expandan horizontalmente
main_frame.grid_columnconfigure(0, weight=1)

# Agregar contenido al top_frame
bienvenido = ttk.Label(top_frame, font=("Arial",24,'bold','italic'), background="#0D0C1D", foreground="#F1DAC4",
                       text="> Bienvenido a la app de Transformación :)")
bienvenido.pack(expand=True, fill='both')


#--------------------------------------------------
frame_intermedio = ttk.Frame(top_frame)
texto = ttk.Label(frame_intermedio, font=("Arial",12,"bold","italic"), text="La aplicación tiene como objetivo la transformación de los documentos .csv descargados desde el sistema de turnos a un formato que sea apto para su utilización en Excel", wraplength=600, anchor='w')
#texto.place(x=40, y=40)
texto.pack()
frame_intermedio.pack(padx=60 ,pady=10, anchor='w')

#--------------------------------------------------
input_frame = ttk.Frame(top_frame)

guardarComo = ttk.Label(master=input_frame, text="> Guardar como: ", foreground="#474973",font=("Arial",20,'bold','italic'))
guardarComo.pack(side='left')

entrada = ttk.Entry(input_frame, width=50)
entrada.pack(side='left')

input_frame.pack(padx=60, pady=30, anchor='w')

# Configurar el peso de las filas para que los widgets en top_frame se expandan verticalmente
top_frame.grid_rowconfigure(0, weight=1)

#-------------------------------------------------------------

transform_frame = ttk.Frame(bottom_frame)

seleccionarArchivo = ttk.Label(transform_frame, text="> Seleccione el archivo que desea transformar...", foreground="#474973", font=('Arial',20,'bold', 'italic'),wraplength=600, anchor='w')
seleccionarArchivo.pack(pady=15)

transform_frame.pack(padx=60, pady=20, anchor= 'w')

#--------------------------------------------------------------
boton_frame = ttk.Frame(bottom_frame)

#imagen boton
boton_img = PhotoImage(file='C:/Users/Lucas/OneDrive/Escritorio/AppMuni/Imagenes/examinar.png')

#Boton examinar
btn_mostrar_tabla = tk.Button(boton_frame, image=boton_img,
                              borderwidth=0, text="Examinar", fg='#F4E9CD',
                              command=lambda: funciones.seleccionarArchivo(entrada.get() + '.xlsx', transform_frame))
btn_mostrar_tabla.pack(pady=10)

boton_frame.pack(anchor='center')

# Iniciar el bucle de eventos
root.mainloop()
