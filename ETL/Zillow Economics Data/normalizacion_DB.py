import pandas as pd
import glob
import os

from funcionesETL_version_final_DB import *

csv_files = glob.glob('./*.csv')
lista_data = []
  
# Creamos un bucle que recorre cada archivo csv de la carpeta, crea un df y lo agrega a una lista
for filename in csv_files:
    data = pd.read_csv(filename)
    lista_data.append(data)


lst_keys = []
for path in csv_files:
    filename = os.path.split(path)[1]
    filename_mod = filename.split('.')[0]
    lst_keys.append(filename_mod)

# Diccionario que contiene cada df y le asigna como key el nombre del archivo correspondiente
dicc_df={}
for e in range(len(lst_keys)):
    key = lst_keys[e]
    df = lista_data[e] 
    dicc_df[key] = df


NormalizaciónBD(dicc_df)

dicc_df['CountyCrossWalk_Zillow'].to_csv('CountyCrossWalk_Zillow_Final.csv', index = False)
dicc_df['County_time_series'].to_csv('County_time_series_Final.csv', index = False)
dicc_df['DimensionEstado'].to_csv('DimensionEstado_Final.csv', index = False)
dicc_df['State_time_series'].to_csv('State_time_series_Final.csv', index = False)
dicc_df['cities_crosswalk'].to_csv('cities_crosswalk_Final.csv', index = False)