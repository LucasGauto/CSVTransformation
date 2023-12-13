import pandas as pd
import os
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo

def transformar(ruta_archivo):
    df = pd.read_csv(ruta_archivo, skiprows=3, delimiter=';')
    dfTransformado = df[['Horario','Nombre', 'Apellido','Edad']]
    dfTransformado['Asistio'] = None
    dfTransformado['Pago'] = None
    return dfTransformado

def guardar(nombre: str, dataframe, ruta_archivo: str):
    # Combina la ruta del escritorio con el nombre del archivo CSV
    ruta_csv_en_escritorio = os.path.join(ruta_archivo, nombre)

    # Guarda el DataFrame en el archivo CSV en el escritorio
    dataframe.to_csv(ruta_csv_en_escritorio, index=False)

def guardarExcel(nombre: str, dataframe, ruta_archivo:str):
    ruta_xlsx_en_escritorio = os.path.join(ruta_archivo, nombre)
    dataframe.to_excel(ruta_xlsx_en_escritorio, index = False)

def transformarExcel(nombre: str, ruta_archivo: str):
    ruta_xlsx_en_escritorio = os.path.join(ruta_archivo, nombre)
    libro = openpyxl.load_workbook(ruta_xlsx_en_escritorio)

    sheet = libro.active
    sheet['H1'] = 'Asistió'
    #sheet['I1'] = '=CONTAR.SI(E:E;"SI")'
    sheet['I1'] = '=COUNTIF(E:E,"SI")'

    sheet['H2'] = 'No asistió'
    #sheet['I2'] = '=CONTAR.SI(E:E;"NO")'
    sheet['I2'] = '=COUNTIF(E:E,"NO")'

    sheet['H3'] = 'Total'
    sheet['I3'] = '=SUM(I1,I2)'

    #/////Validacion de datos///////
    # Crear una lista de valores permitidos ("SI" y "NO")
    valores_permitidos = ["SI", "NO"]

    # Crear la regla de validación de lista
    regla_validacion = openpyxl.worksheet.datavalidation.DataValidation(type="list", formula1='"' + ','.join(valores_permitidos) + '"')

    # Aplicar la regla de validación a una celda específica (por ejemplo, la columna E)
    columna_validacion = "E"
    for fila in range(2, sheet.max_row + 1):
        celda = sheet[f"{columna_validacion}{fila}"]
        sheet.add_data_validation(regla_validacion)
        regla_validacion.add(sheet[f"{columna_validacion}{fila}"])
    
    libro.save(ruta_xlsx_en_escritorio)
    # Cerrar el libro de Excel
    libro.close()
