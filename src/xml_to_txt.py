import xml.etree.ElementTree as ET

def xml_to_txt(xml_file, txt_file):
    # Parsear el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Crear o abrir el archivo TXT
    with open(txt_file, 'w') as f:
        # Recorrer el XML y escribir en el TXT
        for elem in root.iter():
            if elem.text:
                f.write(elem.text + '\n')

# Uso de la función
xml_to_txt('/content/Subred63.xml', 'Subred63.txt')