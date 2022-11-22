import pandas as pd
import numpy as np

# Función de corrección de valores faltantes
# Pasar como parámetro un Diccionario que contenga cada df como valor y le asigne como key
# el nombre del archivo correspondiente.

def correccion_VF(dicc_df):
    # Elimna las columnas que presentan el 70% o más de valores faltantes
    for key in dicc_df:
        for col in dicc_df[key]:
            if round(len(dicc_df[key][col][dicc_df[key][col].isnull()])/len(dicc_df[key])*100,2) >= 70:
                dicc_df[key].drop([col], axis=1, inplace=True)
    # Reemplaza los valores faltantes de las columnas que presentan menos del 70% de valores faltantes
    # para las columnas del tipo 'object' se utiliza la moda y para las diferentes a 'object' se utiliza la mediana
    for key in dicc_df:
        for col in dicc_df[key]:
            if 0 < round(len(dicc_df[key][col][dicc_df[key][col].isnull()])/len(dicc_df[key])*100,2) < 70:
                if dicc_df[key][col].dtype == object:
                    mode = dicc_df[key][dicc_df[key][col] != np.nan][col].mode()[0]  
                    dicc_df[key][col].replace(np.nan, mode, inplace=True)
                if dicc_df[key][col].dtype != object:  
                    dicc_df[key][col].replace(np.nan,dicc_df[key][col].median(), inplace=True)