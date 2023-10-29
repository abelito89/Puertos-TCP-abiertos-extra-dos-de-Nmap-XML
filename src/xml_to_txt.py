import xml.etree.ElementTree as ET

def xml_to_txt(xml_file, txt_file):
    """
    Analiza un archivo XML y extrae el texto de cada elemento.

    Parámetros:
    xml_file (str): La ruta al archivo XML que se va a analizar.
    txt_file (str): La ruta al archivo de texto donde se va a escribir la información.

    Devuelve:
    str: Una cadena de texto que contiene el texto de cada elemento del archivo XML, separado por saltos de línea.
    """
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