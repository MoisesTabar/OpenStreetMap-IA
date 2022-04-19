import heapq
from Folium import draw_location, empty_map

def prueba_UCS(nodoInicial, nodoMeta, adjacency_list):

    # El nodo inicial y el nodoMeta deben ser tuplas con la latitud y la longitud (ojo con esto)
    frontera = []

    #frontera almacena la tupla del los nodos y el costo de todos los nodos que entren a la frontera
    #y frontera_estado se refiere solo al nodo sin el costo en frontera.
    frontera_estado = []
    explorado = []
    ruta = dict()
    ruta[nodoInicial] = nodoInicial

    heapq.heappush(frontera, (nodoInicial, 0))
    frontera_estado.append(nodoInicial)

    costo = dict()

    costo[nodoInicial]= 0

    while len(frontera) > 0:

        estado = heapq.heappop(frontera)
        explorado.append(estado[0])
        # el estado[0] se refiere al primer elemento de la tupla estado, que almacena el nodo y su costo

        if(estado[0] == nodoMeta or estado[0]not in adjacency_list):

            rutaSolucion = []
            n = estado[0]

            #este ciclo añade a la ruta de solucion los padres de los nodos que se encuentran en el estado
            while ruta[n] != n:

                rutaSolucion.append(n)
                n = ruta[n]

            rutaSolucion.append(nodoInicial)
            rutaSolucion.reverse()

            print("Ha llegado a su destino, costo:", costo[estado[0]])
            print(rutaSolucion)

            draw_location(rutaSolucion)

            # Hacer cambios a la condicion
            break

        for (vecino, costoVecino) in adjacency_list[estado[0]]:

            if (vecino not in frontera_estado and vecino not in explorado):
                costo[vecino]= costo[estado[0]] + costoVecino
                heapq.heappush(frontera, (vecino, costoVecino))
                ruta[vecino] = estado[0]
                # Agregar el nodo a la ruta que se está encontrando
                frontera_estado.append(vecino)

            # Se evalua si se debe actualizar el valor del costo del nodo.
            # Si se determina que es más corto ir por el camino actual, pues se modifica el valor del nodo.
            #También se debe actualizar el padre al actualizar el costo
            elif costo[vecino] > costo[estado[0]] + costoVecino:
                costo[vecino] = costo[estado[0]] + costoVecino
                ruta[vecino] = estado[0]

    return