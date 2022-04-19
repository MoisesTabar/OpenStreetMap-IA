import math
class Arista:
        def __init__(self, n1, n2, v, dirigido):

            self.n1 = n1 #nodo 1
            self.n2 = n2 #nodo 2
            self.maxvelocidad = v
            self.__costo = self.costo()
            self.__dirigido = dirigido

        def costo(self):
            # Determinar el costo de la arista
            distancia = math.sqrt((float(self.n1.lon) - float(self.n2.lon))**2 + (float(self.n1.lat) - float(self.n2.lat))**2)
            tiempo = (distancia * 100000) / (self.maxvelocidad/3.6)
            return tiempo

        def get_costo(self):
            return self.__costo

        def dirigido(self) -> bool:
            return self.__dirigido

        def get_node(self, x):
                if x==1:
                    return self.n1
                elif x==2:
                    return self.n2