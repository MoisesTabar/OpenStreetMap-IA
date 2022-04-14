import xml.etree.ElementTree as ET
import xmltodict
import json
from data.node import Node 
from data.way import Way

archivo_xml = ET.parse('santo_domingo.osm')

root = archivo_xml.getroot()


nodes = root.findall('node')
data_nodes = []


def find_nodes() -> None:
    for node in nodes:
        #node_values = { 
          #  'id': node.attrib['id'], 
          # 'lat': node.attrib['lat'], 
           # 'lon': node.attrib['lon'] 
       # }
        
        nodo = Node(node.attrib['id'] , 
        node.attrib['lat'], 
        node.attrib['lon'])



        data_nodes.append(nodo)


ways = root.findall('way')
data_ways = []


def find_ways() -> None:
    for way in ways:

        decoded_way = ET.tostring(way)


        data = json.dumps(xmltodict.parse(decoded_way))

        parsed_data = json.loads(data)
        
        # way_values = {
        #     "way": {
        #         "id": parsed_data["way"]["@id"],
        #         "nd": parsed_data["way"]["nd"],
        #         "tag": parsed_data["way"]["tag"]
        #     }
        # }

        via = Way(parsed_data["way"]["@id"])
        
        for nodo in parsed_data["way"]["nd"]:
            nodoRef = filter(lambda busqueda: busqueda.id == nodo['@ref'], data_nodes)

            for nodoData in nodoRef:

                print(nodoData.lon)

                via.nodos.append(nodoData)
       

        data_ways.append(via)
