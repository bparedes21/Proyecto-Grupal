# Importamos librerías necesarias
import pandas as pd
import glob

from funcionesETL_city_NY import *

from funcionesETL_city_NY import *

csv_files = glob.glob(r'C:\Users\Usuario\Desktop\2- Grupal\House_Market\Datasets - copia\ciudades-NY\*.csv')
lista_data_csv = []
  
# Creamos un bucle que recorre cada archivo csv de la carpeta, crea un df y lo agrega a una lista
for filename in csv_files:
    data = pd.read_csv(filename, encoding='UTF-8')
    lista_data_csv.append(data)

# Diccionario que contiene cada df y le asigna como key el nombre del archivo correspondiente
dicc_df = { 'CiudadesNY':lista_data_csv[0]}


## - Filtro Datos por Fecha
fecha_mayor_2012(dicc_df)


## - Correción de valores faltantes
correccion_VF(dicc_df)


## - Elimino columnas que no se tendrán en cuenta
dicc_df['CiudadesNY'].drop(columns = ['Unique_City_ID', 'County', 'State', 'RegionName'], inplace=True)


## - Creo archivo csv con las correciones
dicc_df['CiudadesNY'].to_csv(r'C:\Users\Usuario\Desktop\2- Grupal\House_Market\Datasets - copia\ciudades-NY\CiudadesNY-correccion.csv', index=False)
