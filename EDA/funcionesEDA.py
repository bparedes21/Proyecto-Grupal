## Nota: todas las funciones presentan como parámetro a pasar un diccionario cuyos valores deben ser dataframes 
# y las claves los nombres de archivo del cual proviene el df.

import pandas as pd
import numpy as np

## VALORES FALTANTES

# valores_faltantes: determina el porcentaje de valores faltantes por columna

def valores_faltantes(dicc_df):
    for key in dicc_df:
        col = dicc_df[key].columns
        print(key,'\n')
        for e in col:
            print(e,'\t',round(len(dicc_df[key][e][dicc_df[key][e].isnull()])/len(dicc_df[key])*100,2),'%')
        print('\n\n')


# REGISTROS DUPLICADOS

# registros_duplicados: determina el porcentaje de registros duplicados

def registros_duplicados(dicc_df):
    for key in dicc_df:
        print(key,':',dicc_df[key].duplicated().sum())


## OUTLIERS

# outliers: determina la cantidad de outliers por columna

def cantidad_outliers(dicc_df):

    for key in dicc_df:
        
        for columna in dicc_df[key].columns:
            
            if dicc_df[key].loc[:,columna].dtype!=object:

                Q1 = dicc_df[key][columna].quantile(0.25)
                Q3 = dicc_df[key][columna].quantile(0.75)
                IQR = Q3 - Q1
                BI = Q1 - 1.5*IQR
                BS = Q3 + 1.5*IQR

                out_sup = dicc_df[key][dicc_df[key][columna] > BS].index
                out_inf = dicc_df[key][dicc_df[key][columna] < BI].index
                outliers = []
                for i in out_sup:
                    outliers.append(i)
                    for j in out_inf:
                        outliers.append(j)
                size = len(pd.Series(outliers).unique())


                if size > 0: 
                    print('\n')
                    print(key)
                    print(columna)
                    print('Q1: ',Q1)
                    print('Q3: ',Q3)
                    print('IQR: ',IQR)
                    print('BI: ',BI)
                    print('BS: ',BS)
                    print (f'Hay {size} valores atípicos en la variable {columna}')