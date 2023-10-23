import xml.etree.ElementTree as ET

def xml_to_txt(xml_file):
    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Crear una lista para almacenar las líneas de texto
    lines = []

    # Recorrer el XML y añadir a la lista
    for elem in root.iter():
        if elem.text:
            lines.append(elem.text)

    # Unir las líneas con saltos de línea y devolver
    return '\n'.join(lines)