import xml.etree.ElementTree as ET
import xmltodict
import json
from .node import Node 
from .way import Tags, Way


archivo_xml = ET.parse('San Pedro.osm')

root = archivo_xml.getroot()

nodes = root.findall('node')
data_nodes = []


def find_nodes() -> None:
    for node in nodes:
        nodo = Node(
            node.attrib['id'],
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

        if parsed_data["way"]["nd"][0]["@ref"] == parsed_data["way"]["nd"][len(parsed_data["way"]["nd"])-1]["@ref"]: 

            via.open = False

        tags = Tags()
        tags.highway = "residential"
        tags.max_speed = 30


        try:
          
            if via.open:
                for node in parsed_data["way"]['tag']:

                    try:
                        tag = node['@k'] # nombre del valor
                        value = node['@v'] # valor


                        if tag == 'highway':
                            tags.highway = value
                            
                            if value == 'residential':
                                tags.max_speed = 30

                            elif value == 'primary':
                                tags.max_speed = 100

                            elif value == 'secondary':
                                tags.max_speed = 50

                            elif value == 'tertiary':
                                tags.max_speed = 60

                            else:
                                tags.highway = 'residential'
                                tags.max_speed = 30

                        if tag == 'name':
                            tags.name = value
                        

                        if tag == 'oneway' and value in ('yes', 'no'):
                            if value == 'yes':
                                tags.oneway = True
                            else:
                                tags.oneway = False

                    except TypeError:
                        tags.highway = "residential"
                        tags.max_speed = 30

                if tags.highway == "":
                    tags.highway = "residential"
                    tags.max_speed = 30

            data_ways.append(via) 
                
        except:
            data_ways.append(via)
            
        via.tags = tags

