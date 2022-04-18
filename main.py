from data.xml_data_processor import (
    find_nodes,
    find_ways,
    data_nodes,
    data_ways
)
import algoritmo
from data.graph import Graph

def main() -> None:

    print("Starting node search operation")
    find_nodes()
    print("Finishing node search operation successfully")
    print("Starting way search operation")
    find_ways()
    print("Finishing way search operation successfully")
    g = Graph(data_ways)

    ady = g.get_ady()

    #se imprimen todas las adyasencias aqui pueden buscar puntos para poner en el algoritmo
    for i in ady.keys():
        print(i, end= " ")
        for k in ady[i]:
            print("-->", k, end=" ")
        print()
    #aqui se prueba el algoritmo
    algoritmo.prueba_UCS((18.4740672, -69.9098465),(18.4753492, -69.9059964), ady)
if __name__ == '__main__':
    main()