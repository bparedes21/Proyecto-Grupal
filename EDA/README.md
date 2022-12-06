Contamos con datasets provenientes de Zillow, una de las plataformas del mercado inmobiliario
de USA más importantes, con lo que nos aseguramos que los datos son confiables y representativos
del problema.

Estos datasets están presentados en carpetas segun las temáticas que comprenden.

Al momento de efectuar el analisis exploratorio adoptamos
la estrategia de automatizar la etapa de procesamiento y evaluacion de los datos
debido al gran numero de archivos a utilizar (53 archivos en 4 carpetas). Con esto conseguimos optimizar el tiempo
y el costo del trabajo.

Los pasos de este análisis fueron:

    * Explorar algunos registros de cada dataset, con el fin de conocer 
	la distribucion y las variables presentes.

    * Obtener información de los tipos de datos, cantidad de filas y columnas

    * Conseguir medidas estadísticas de los mismos, para conocer su comportamiento.

	Determinar cantidad de:

    * Valores Faltantes

    * Registros Duplicados

    * Outliers

	
 En los notebooks de la carpeta REPORTE se analiza de manera global cuales son los problemas que contiene cada carpeta.


Conclusiones:
	
	- Se determino que los archivos contenidos en las carpetas Zillow House Price Data y
	Zillow Rent Index no presentan información relevante, ya que lo que aportan está contenido
	en los archivos time series de la carpeta Zillow Economics Data, por lo que no será utilizados.


	- Eliminar columnas con:
		 valores nulos >= 70%

	- Aplicar filtro por RegionName y completar con una medida de tendencia central las columnas que presenten
	 	0% < valores nulos < 70%
		
	Con esto se busca que al reemplazar los valores faltantes el valor imputado se lo más representativo
	posible de la zona.

	Tener en cuenta que hay regiones que no presentan ningún valor en determinadas columnas para el total de años
	comprendidos, lo que presenta un inconveniente al imputar faltantes de esta manera, ya que hay que tener en cuenta
	al filtrar por region no se presentaran valores con lo cual calcular la medida para completarlos. Se presentan dos
	alternativas para tratarlos, la primera es dejarlos vacíos y la segunda imputarlos con una medida que sea general 
	para el set de datos, no se recomienda eliminarlos debido a que perderiamos registros con información valiosa.

