import pandas as pd
import glob
import os

from funcionesETL_version_final_DB import *


csv_files = glob.glob('./*Final.csv')
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


dicc_df={}
for e in range(len(lst_keys)):
    key = lst_keys[e]
    df = lista_data[e] 
    dicc_df[key] = df


dicc_county = {}
dicc_county['County_time_series_Final'] = dicc_df['County_time_series_Final']
filtro_fecha(dicc_county)
correccion_VF(dicc_county)
importar_csv(dicc_county)


dicc_state = {}
dicc_state['State_time_series_Final'] = dicc_df['State_time_series_Final']
filtro_fecha(dicc_state)
correccion_VF(dicc_state)
importar_csv(dicc_state)


dicc_1 = {}
dicc_1['ciudad_31_40'] = dicc_df['ciudad_31_40']
filtro_fecha(dicc_1)
correccion_VF(dicc_1)
importar_csv(dicc_1)


dicc_41 = {}
dicc_41['ciudad_41_50'] = dicc_df['ciudad_41_50']
filtro_fecha(dicc_41)
correccion_VF(dicc_41)
importar_csv(dicc_41)


dicc_21 = {}
dicc_21['ciudad_21_30'] = dicc_df['ciudad_21_30']
filtro_fecha(dicc_21)
correccion_VF(dicc_21)
importar_csv(dicc_21)


dicc_11 = {}
dicc_11['ciudad_11_20'] = dicc_df['ciudad_21_30']
filtro_fecha(dicc_11)
correccion_VF(dicc_11)
importar_csv(dicc_11)


dicc_10 = {}
dicc_10['ciudad_1_10'] = dicc_df['ciudad_1_10']
filtro_fecha(dicc_10)
correccion_VF(dicc_10)
importar_csv(dicc_10)