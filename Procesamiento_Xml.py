import xml.etree.ElementTree as ET

archivo_xml = ET.parse('santo_domingo.osm')

root = archivo_xml.getroot()


EncontrarNodos = root.findall('node')
nodos = []

for nodo in EncontrarNodos:

    nodos.append(ET.tostring(nodo))


print(len(nodos))   
    

EncontrarVias = root.findall('way')
vias = []

for via in EncontrarVias:

    vias.append(ET.tostring(via))

print(len(vias))