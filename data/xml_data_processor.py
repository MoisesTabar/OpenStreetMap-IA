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
            try:
                tag = node['@k'] # nombre del valor
                value = node['@v'] # valor


                if tag == 'highway':
                    highway_tag = Tags(highway=value)
                    
                    if value == 'residential':
                        highway_tag.max_speed = 40

                    elif value == 'primary':
                        highway_tag.max_speed = 100

                    elif value == 'secondary':
                        highway_tag.max_speed = 50

                    elif value == 'tertiary':
                        highway_tag.max_speed = 60

                    else:
                        highway_tag.highway = 'residential'
                        highway_tag.max_speed = 40

                    via.tags = highway_tag
                 

                if tag == 'oneway' and value in ('yes', 'no'):
                    if value == 'yes':
                        highway_tag.oneway = True
                    else:
                        highway_tag.oneway = False

            except TypeError:
                print("Error degraciao")
            except KeyError:
                print("Maldita baina")

        # print(via.tags)
        data_ways.append(via)
