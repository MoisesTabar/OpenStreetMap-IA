from .arista import Arista

class Graph:
    def __init__(self, data_ways) -> None:
   
        self.__aristas = []
        self.__adyacencia = {}

        for way in data_ways:

            if way.open:
                for n in range(len(way.nodes)):

                    try:
                        maxvelocidad = way.tags.max_speed
                        dirigido = way.tags.oneway
                        arista = Arista(way.nodes[n], way.nodes[n+1], maxvelocidad, dirigido) 
                        #Creamos la arista
                        self.agregar(arista)
                    except:
                        pass

            
    def agregar(self, arista: Arista):
        #Agrega aristas
        if arista not in self.__aristas:
            self.__aristas.append(arista)
            self.agregar_ady(arista)

    def get_ady(self): 
        # Devuelve el diccionario de adyacencia
        return self.__adyacencia


    def agregar_ady(self, arista):
        """Esta función añade los adyasentes"""
        n1 = arista.get_node(1).get_coord() #este es el el nodo 1 de la arista
        n2 = arista.get_node(2).get_coord() #este es el nodo 2 de la arista

        if n1 in self.__adyacencia:

            self.__adyacencia[n1].append([n2, arista.get_costo()])
            if not arista.dirigido():
                if n2 not in self.__adyacencia:

                    self.__adyacencia.setdefault(n2, [[n1, arista.get_costo()]])
                else:

                    self.__adyacencia[n2].append([n1, arista.get_costo()])

        else:
            if arista.dirigido():
                self.__adyacencia.setdefault(n1, [[n2, arista.get_costo()]])
            else:

                self.__adyacencia.setdefault(n1, [[n2, arista.get_costo()]])
                if n2 not in self.__adyacencia:

                    self.__adyacencia.setdefault(n2, [[n1, arista.get_costo()]])
                else:

                    self.__adyacencia[n2].append([n1, arista.get_costo()])