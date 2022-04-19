# Open Street Map



## Arquitectura del Proyecto

En este proyecto utilizamos la programación orientada a objetos, en la cual dividimos el sistema en diferentes clases con sus atributos y métodos correspondientes. 

Contamos con un archivo main, a partir del cual se realizará la ejecución. Este llama la clase que procesa el archivo osm. El archivo main será quien llame a la clase Graph y también será quien ejecute la interfaz gráfica. 

La clase que procesa el xml tiene conexión con la clase node, la cual representa los nodos y con la clase way, la cual representa las vías.

La clase Graph además de tener conexión con las clases node y way respectivamente también tiene conexión con las aristas que se va a armar el grafo.

En la UI  se recibirán los datos de entrada  y a su vez este es quien llamará al algoritmo de búsqueda. 

Cuando el algoritmo se termina de procesar, se llamará al método de Folium que se encargará de trazar la ruta del mapa para ser mostrada en la interfaz gráfica.

## Diagrama de Procesos

![Diagram](Diagrama.jpeg)
