import pandas as pd
import numpy as np


# correccion_VF: Función de corrección de valores faltantes
# Pasar como parámetro Diccionario que contenga cada df como valor y le asigna como key el nombre
# del archivo correspondiente

def correccion_VF(dicc_df):

# Determina si hay outliers para separarlos y poder imputar los valores faltantes de manera que no se vean afectados
# por los valores atípicos
    for key in dicc_df:
        for col in dicc_df[key].columns:
            if dicc_df[key].loc[:,col].dtype!=object:

                Q1 = dicc_df[key][col].quantile(0.25)
                Q3 = dicc_df[key][col].quantile(0.75)
                IQR = Q3 - Q1
                BI = Q1 - 1.5*IQR
                BS = Q3 + 1.5*IQR

                out = (dicc_df[key][col] < BI) | (dicc_df[key][col] > BS)

# Elimna las columnas que presentan el 70% o más de valores faltantes
    for key in dicc_df:
        for col in dicc_df[key]:
            if round(len(dicc_df[key][col][dicc_df[key][col].isnull()])/len(dicc_df[key])*100,2) >= 70:
                dicc_df[key].drop([col], axis=1, inplace=True)

# Reemplaza los valores faltantes de las columnas que presentan menos del 70% de valores faltantes
# para las columnas del tipo 'object' se utiliza la moda y para las diferentes a 'object' se utiliza la mediana
# para imputar los valores se aplican filtros como seleccion por RegionName, quitar outliers y no contemplar np.nan
    for key in dicc_df:
        for col in dicc_df[key].columns:
            if 0 < round(len(dicc_df[key][col][dicc_df[key][col].isnull()])/len(dicc_df[key])*100,2) < 70:
                if dicc_df[key].loc[:,col].dtype==object:
                
                                    
                    mode = dicc_df[key][(dicc_df[key] != np.nan) & (~out)][col].mode()[0]  
                    dicc_df[key][col].fillna( mode, inplace=True)

                if dicc_df[key].loc[:,col].dtype!=object:
                
                    median = dicc_df[key][col][(dicc_df[key][col] != np.nan) & (~out)].median()                 
                    dicc_df[key][col].fillna( median, inplace=True)     



# fecha_mayor_2012: como indica el nombre, seleciona sólo los registros que presenten
# fechas a partir de '2012_01-01'

def fecha_mayor_2012(dicc_df):
    for key in dicc_df:
        dicc_df[key] = dicc_df[key][dicc_df[key]['Date']>='2012-01-01']