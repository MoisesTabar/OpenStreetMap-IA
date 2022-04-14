import xml.etree.ElementTree as ET
import xmltodict
import json
from .node import Node 
from .way import Tags, Way


archivo_xml = ET.parse('santo_domingo.osm')

root = archivo_xml.getroot()

nodes = root.findall('node')
data_nodes = []


def find_nodes() -> None:
    for node in nodes:
        nodo = Node(
            node.attrib['id'] , 
            node.attrib['lat'], 
            node.attrib['lon']
        )

        data_nodes.append(nodo)


ways = root.findall('way')
data_ways = []


def find_ways() -> None:
    for way in ways:

        decoded_way = ET.tostring(way)

        data = json.dumps(xmltodict.parse(decoded_way))

        parsed_data = json.loads(data)
        
        via = Way(parsed_data["way"]["@id"])
        
        for nodo in parsed_data["way"]["nd"]:
            nodoRef = filter(lambda busqueda: busqueda.id == nodo['@ref'], data_nodes)

            for nodoData in nodoRef:
                via.nodes.append(nodoData)

        for node in parsed_data["way"]['tag']:

            way_tag = node['@k']
            is_way = node['@v']

            if way_tag == 'oneway' and is_way == 'yes':
                w_tag = Tags(highway='no', oneway=is_way, max_speed=0)


            if way_tag == 'highway' and is_way == 'yes':
                w_tag = Tags(highway='yes', oneway='no', max_speed=0)

                via.tags.append(w_tag)
            
        data_ways.append(via)
