from data.xml_data_processor import ( 
    find_nodes, 
    find_ways,
    data_nodes,
    data_ways
)
from data.node import Node
from data.way import Way


def main() -> None:
    print("Starting node search operation")

    find_nodes()

    print("Finishing node search operation successfully")

    node = Node(data_nodes)
    
    print(len(node.nodes))
    
    print("Starting way search operation")

    find_ways()

    print("Finishing way search operation successfully")

    way = Way(data_ways)
    
    print(way.ways)

if __name__ == '__main__':
    main()
