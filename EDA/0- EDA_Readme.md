
Para el desarrollo del análisis exploratorio de datos se busco poder automatizar el proceso debido a que se dispuso de 4 carpetas con un total de 53 archivos.


Procedimiento:

Se trabajo cada carpeta por separado y los archivos contenidos en ellas en conjunto.

Se utilizó la función glob con la que se puede acceder a la ruta de todos los archivos de una carpeta que presenten cierto patrón el cual debe ser ingresado como parámetro, en este caso se paso '*.csv' para indicar que seleccione todos los archivos con formato csv. Una vez obtenida la ruta de estos archivos, por medio de una sentencia for se creó un dataframe para cada uno de estos archivos y se los agregó como elementos en una lista. Para que los DF no pierdan la referencia de su origen se elaboró un diccionario donde las claves representan los nombres de los archivos cuyos datos están contenidos en cada DF y logicamente para cada clave se asigno un elemento de la lista, es decir el DF que corresponde a la key.

Una vez logrado esto, se aplicaron sentencias for simples y anidadas al diccionario con lo cual se logró optimizar el EDA, ya que se procesaron varios archivos al mismo tiempo y se evaluaron de esta manera la cantidad de valores nulos, registros duplicados y outliers, entre otros. Además se tuvo en cuenta que siempre que se fuera a imprimir el resultado de la evaluación de un DF que se imprimiera tambien la 'key' con lo cual tener identificado el dataset de origen.
