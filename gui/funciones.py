from tkinter import filedialog
from logica import acciones
from tkinter import ttk
from tkinter import *

def seleccionarArchivo(nombre, root):
    # Configurar tipos de archivos permitidos (solo archivos CSV)
    tipos_archivos = [("Archivos CSV", "*.csv")]

    # Examinador de archivos con filtro
    ruta_archivo = filedialog.askopenfilename(filetypes=tipos_archivos)

    if ruta_archivo:
        # Procesar el archivo CSV (ejemplo con pandas)
        try:
            #llamar a funcion que hace las transformaciones
            df = acciones.transformar(ruta_archivo= ruta_archivo)
            guardarArchivo(df, nombre)
            
            #////Ventana emergente/////
            ventana = Toplevel()
            ventana.title("Guardado exitoso")
            ventana.geometry("300x200")

            texto = ttk.Label(master=ventana, text=f"El archivo {nombre} fue guardado con éxito.")
            texto.pack(anchor='center')

            boton_cerrar = ttk.Button(
                ventana,
                text="Cerrar",
                command=ventana.destroy
            )
            boton_cerrar.pack(pady=20)
            #/////////////////////////
            

        except Exception as e:
            print(f"No se pudo cargar el archivo XLSX: {e}")

def guardarArchivo(df, nombre):
    #guardar el nuevo documento en una carpeta específica
    ruta_directorio = filedialog.askdirectory()
    
    input_entry = ttk.Entry()

    #llamar a funcion que guarda el archivo
    #acciones.guardar(nombre,df, ruta_archivo=ruta_directorio)
    acciones.guardarExcel(nombre, df, ruta_archivo=ruta_directorio)
    acciones.transformarExcel(nombre, ruta_directorio)