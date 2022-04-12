import xml.etree.ElementTree as ET

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



""" TODO fix way_values bug. It keeps iterating..."""
def find_ways() -> None:
    for way in ways:
        for child in ways:
            way_values = {
                'id': way.attrib['id'],
                'key': child.attrib.get('k'),
                'val': child.attrib.get('v')
            }

        data_ways.append(way_values)
