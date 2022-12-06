import pandas as pd
import numpy as np

#Se procede a normalizar algunas columnas y a realizar diferentes joins con el fin de que se pueda
#crear una base de datos con tablas de hechos y dimensiones, y no tener todas las columnas en una sola tabla
def NormalizaciónBD (dicc_df):
    lista_key = ['DimensionEstado','CountyCrossWalk_Zillow','cities_crosswalk','State_time_series','City_time_series','County_time_series']
    for key in lista_key:
        if 'AlphaCode' in dicc_df[key].keys():
            dicc_df[key]['StateAlpha'] = dicc_df[key].State + ', ' + dicc_df[key].AlphaCode
            dicc_df[key] = dicc_df[key][['FIPSState','AlphaCode', 'State', 'StateAlpha']]
        elif 'CountyName'in dicc_df[key].keys().tolist():
            dicc_df[key] = pd.concat([dicc_df[key].FIPS,dicc_df[key].CountyName,dicc_df[key].StateFIPS], axis=1)
            dicc_df[key].rename(columns={'FIPS': 'CountyFIPS'}, inplace=True)
        elif 'City' in dicc_df[key].keys().tolist():
            dicc_df[key]=dicc_df[key].merge(dicc_df['DimensionEstado'], left_on='State', right_on='AlphaCode').merge(dicc_df['CountyCrossWalk_Zillow'], left_on=['FIPSState','County'], right_on=['StateFIPS', 'CountyName'])
            dicc_df[key]['IDCiudad'] = dicc_df[key].index
            dicc_df[key].IDCiudad=dicc_df[key].IDCiudad.shift(periods=-1)
            dicc_df[key].IDCiudad.fillna(25328, inplace=True)
            dicc_df[key].drop(['CountyName','County','State_x','State_y','CountyFIPS'],axis=1, inplace = True)
            dicc_df[key]['CityState'] = dicc_df[key].City + ', ' + dicc_df[key].AlphaCode
            dicc_df[key].drop('AlphaCode', axis = 1, inplace=True)
            dicc_df[key]=dicc_df[key][['IDCiudad','Unique_City_ID','City','CityState','StateFIPS']]
            dicc_df[key].IDCiudad= dicc_df[key].IDCiudad.astype('int')    
        elif len(dicc_df[key]) >= 3762566:
            dicc_df[key] = pd.merge(dicc_df['cities_crosswalk'], dicc_df[key], left_on='Unique_City_ID', right_on='RegionName')
            listaEstado1 = [1, 2, 4, 5, 6, 8, 9, 10,12,56]
            listaEstado2 = [13,15,16,17,18,19,20,21,22,23]
            listaEstado3 = [24,25,26,27,28,29,30,31,32,33]
            listaEstado4 = [34,35,36,37,38,39,40,41,42,44]
            listaEstado5 = [45,46,47,48,49,50,51,53,54,55]
            dicc_df[key][dicc_df[key].StateFIPS.isin(listaEstado1)].drop(['Unique_City_ID', 'RegionName', 'City', 'StateFIPS','CityState'], axis = 1).to_csv('ciudad_1_10.csv' , index = False)
            dicc_df[key][dicc_df[key].StateFIPS.isin(listaEstado2)].drop(['Unique_City_ID', 'RegionName', 'City', 'StateFIPS','CityState'], axis = 1).to_csv('ciudad_11_20.csv', index = False)
            dicc_df[key][dicc_df[key].StateFIPS.isin(listaEstado3)].drop(['Unique_City_ID', 'RegionName', 'City', 'StateFIPS','CityState'], axis = 1).to_csv('ciudad_21_30.csv', index = False)
            dicc_df[key][dicc_df[key].StateFIPS.isin(listaEstado4)].drop(['Unique_City_ID', 'RegionName', 'City', 'StateFIPS','CityState'], axis = 1).to_csv('ciudad_31_40.csv', index = False)
            dicc_df[key][dicc_df[key].StateFIPS.isin(listaEstado5)].drop(['Unique_City_ID', 'RegionName', 'City', 'StateFIPS','CityState'], axis = 1).to_csv('ciudad_41_50.csv', index = False)
        elif len(dicc_df[key]) >= 518791:
            dicc_df[key] = pd.merge(dicc_df['CountyCrossWalk_Zillow'], dicc_df[key], left_on='CountyFIPS', right_on='RegionName').drop(['CountyName','StateFIPS', 'RegionName'], axis = 1)
        elif len(dicc_df[key]) >= 13117:
            lista_state = dicc_df[key].RegionName.unique()
            listaEstado=['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado','Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
            'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana','Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota','Mississippi', 'Missouri', 'Nebraska', 'Nevada', 'New Hampshire',
            'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'Ohio','Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island','South Carolina', 'Tennessee', 'Texas', 'Utah', 'Virginia',
            'Washington', 'West Virginia', 'Wisconsin', 'South Dakota','Vermont', 'Alaska', 'Montana', 'Wyoming', 'District of Columbia','North Dakota', 'United States']
            dicc_df[key].RegionName = dicc_df[key].RegionName.replace(lista_state, listaEstado, regex = True)
            dicc_df[key]=dicc_df[key].drop(dicc_df[key][dicc_df[key].RegionName.isin(['United States'])==True].index).reset_index(drop = True)
            dicc_df[key] = dicc_df['DimensionEstado'].merge(dicc_df[key], left_on='State', right_on='RegionName').sort_values(['Date','State'])
            dicc_df[key].drop(['State','AlphaCode','RegionName','StateAlpha'], axis=1, inplace=True)
    dicc_df['CountyCrossWalk_Zillow'].to_csv('CountyCrossWalk_Zillow_Final.csv', index = False)
    dicc_df['County_time_series'].to_csv('County_time_series_Final.csv', index = False)
    dicc_df['DimensionEstado'].to_csv('DimensionEstado_Final.csv', index = False)
    dicc_df['State_time_series'].to_csv('State_time_series_Final.csv', index = False)
    dicc_df['cities_crosswalk'].to_csv('cities_crosswalk_Final.csv', index = False)   

# fecha_mayor_2012: como indica el nombre, seleciona sólo los registros que presenten
# fechas a partir de '2012_01-01'

def filtro_fecha(dicc_df):
    for key in dicc_df:
        dicc_df[key] = dicc_df[key][dicc_df[key]['Date']>='2012-01-01']


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
                    if 'IDCiudad' in dicc_df[key].columns:
                        states = dicc_df[key].IDCiudad
                        state = dicc_df[key].IDCiudad.unique()
                        for st in state:                        
                            mode = dicc_df[key][(dicc_df[key] != np.nan) & (~out) & (states == st)][col].mode()[0]  
                            dicc_df[key][col][(dicc_df[key][col].isnull()==True) & (states==st)] = mode
                    elif 'CountyFIPS' in dicc_df[key].columns:
                        states = dicc_df[key].CountyFIPS
                        state = dicc_df[key].CountyFIPS.unique()
                        for st in state:                        
                            mode = dicc_df[key][(dicc_df[key] != np.nan) & (~out) & (states == st)][col].mode()[0]  
                            dicc_df[key][col][(dicc_df[key][col].isnull()==True) & (states==st)] = mode
                    elif 'FIPSState' in dicc_df[key].columns:
                        states = dicc_df[key].FIPSState
                        state = dicc_df[key].FIPSState.unique()
                        for st in state:                        
                            mode = dicc_df[key][(dicc_df[key] != np.nan) & (~out) & (states == st)][col].mode()[0]  
                            dicc_df[key][col][(dicc_df[key][col].isnull()==True) & (states==st)] = mode
                if dicc_df[key].loc[:,col].dtype!=object:
                    if 'IDCiudad' in dicc_df[key].columns:
                        states = dicc_df[key].IDCiudad
                        state = dicc_df[key].IDCiudad.unique()
                        for st in state:
                            mediana = dicc_df[key][col][(dicc_df[key][col]!=np.nan) & (~out) & (states == st)].median()   
                            dicc_df[key][col][(dicc_df[key][col].isnull()==True) & (states==st)] = mediana   
                    elif 'CountyFIPS' in dicc_df[key].columns:
                        states = dicc_df[key].CountyFIPS
                        state = dicc_df[key].CountyFIPS.unique()
                        for st in state:
                            mediana = dicc_df[key][col][(dicc_df[key][col]!=np.nan) & (~out) & (states == st)].median()   
                            dicc_df[key][col][(dicc_df[key][col].isnull()==True) & (states==st)] = mediana 
                    elif 'FIPSState' in dicc_df[key].columns:
                        states = dicc_df[key].FIPSState
                        state = dicc_df[key].FIPSState.unique()
                        for st in state:
                            mediana = dicc_df[key][col][(dicc_df[key][col]!=np.nan) & (~out) & (states == st)].median()   
                            dicc_df[key][col][(dicc_df[key][col].isnull()==True) & (states==st)] = mediana 




# En caso de haber alguna columna que no deba ingresarse en la base de datos
# esta funcion la elimina.
def drop_columns(dicc_df):
    for key in dicc_df.keys():
        for col in dicc_df[key].columns:
            lista_col_drop=['Unnamed: 0']        
            if col in lista_col_drop:
                dicc_df[key].drop(columns=[col], inplace=True)


# importar_csv: crea un archivo csv para cada df contenido en el diccionario

def importar_csv(dicc_df):
    for key in dicc_df.keys():
        dicc_df[key].to_csv(key+'_transformado.csv', index = False)



