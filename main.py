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

    # node = (data_nodes)
    print(len(data_nodes))

    print("Starting way search operation")

    find_ways()

    print("Finishing way search operation successfully")

    # way = (data_ways)
    # for way in data_ways:
    #     print(way.id)

if __name__ == '__main__':
    main()
