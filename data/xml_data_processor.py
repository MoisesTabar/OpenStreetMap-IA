import xml.etree.ElementTree as ET
import xmltodict
import json

archivo_xml = ET.parse('santo_domingo.osm')

root = archivo_xml.getroot()


nodes = root.findall('node')
data_nodes = []


def find_nodes() -> None:
    for node in nodes:
        node_values = { 
            'id': node.attrib['id'], 
            'lat': node.attrib['lat'], 
            'lon': node.attrib['lon'] 
        }

        data_nodes.append(node_values)


ways = root.findall('way')
data_ways = []


def find_ways() -> None:
    for way in ways:

        decoded_way = ET.tostring(way)


        data = json.dumps(xmltodict.parse(decoded_way))

        parsed_data = json.loads(data)
        
        way_values = {
            "way": {
                "id": parsed_data["way"]["@id"],
                "nd": parsed_data["way"]["nd"],
                "tag": parsed_data["way"]["tag"]
            }
        }

        print(way_values)

        data_ways.append(way_values)
