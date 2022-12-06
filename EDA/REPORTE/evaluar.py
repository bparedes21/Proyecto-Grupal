# Importamos librerías necesarias

import pandas as pd


def fecha_mayor_2012(dicc_df):
    for key in dicc_df:
        if 'Date' not in dicc_df[key].columns:  
            continue
        else:  
            dicc_df[key] = dicc_df[key][dicc_df[key]['Date']>='2012-01-01']

# Valores faltantes
def val_null(dicc_df):
    valores_nulos = []
    len_col = []
    for key in dicc_df:
        col = dicc_df[key].columns
        len_col.append(len(col))
        for e in col:
            val_n = round(len(dicc_df[key][e][dicc_df[key][e].isnull()])/len(dicc_df[key])*100,2)
            valores_nulos.append(val_n)
    return(sum(valores_nulos)/sum(len_col))

# Registros duplicados
def reg_dup(dicc_df):
    lis_dup = []
    len_df = []
    for key in dicc_df:
        len_df.append(len(dicc_df[key]))
        lis_dup.append(dicc_df[key].duplicated().sum())
    return(sum(lis_dup)/sum(len_df))

    
def cantidad_outliers(dicc_df):
    outliers = []
    len_col = []

    for key in dicc_df:
        col = dicc_df[key].columns
        len_col.append(len(col))

        for columna in dicc_df[key].columns:
            
            if dicc_df[key].loc[:,columna].dtype!=object:

                Q1 = dicc_df[key][columna].quantile(0.25)
                Q3 = dicc_df[key][columna].quantile(0.75)
                IQR = Q3 - Q1
                BI = Q1 - 1.5*IQR
                BS = Q3 + 1.5*IQR

                out = (dicc_df[key][columna] < BI) | (dicc_df[key][columna] > BS)
                
                outliers = round((len(dicc_df[key][columna][(out)])/(len(dicc_df[key])))*100,2)

    return(outliers)       
                        
