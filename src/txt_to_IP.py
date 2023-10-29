import re

def txt_to_IP(text, output_file):
    """
    Procesa un texto que contiene informes de escaneo de Nmap, extrae las direcciones IP y los detalles de los puertos TCP abiertos, y escribe esta información en un archivo de salida.

    Parámetros:
    text (str): El texto que se va a procesar, que debe contener informes de escaneo de Nmap y que debe ser la salida de la función xml_to_txt.xml_to_txt
    output_file (str): La ruta al archivo de texto donde se va a escribir la información.

    Devuelve:
    str: La ruta al archivo de texto donde se ha escrito la información.
    """
    lines = text.split('\n')
    result = ''
    ip_lines = []
    for line in lines:
        if 'Nmap scan report for' in line:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]
            ip_lines.append(len(result.split('\n')) - 1)  # Guarda la línea donde se encuentra la IP
            result += '\n\n' + f'IP: {ip}\n'
        elif 'PORT' in line and 'STATE' in line and 'SERVICE' in line and 'VERSION' in line:
            result += line.strip() + '\n'
        elif re.match(r'\d+/tcp', line):
            result += line.strip() + '\n'
    
    # Elimina las IPs sin puertos TCP abiertos
    result_lines = result.split('\n')
    for ip_line in reversed(ip_lines):  # Revisa las líneas de IP en orden inverso
        if ip_line + 3 < len(result_lines) and result_lines[ip_line + 3] == '':
            del result_lines[ip_line:ip_line + 3]  # Elimina la IP y las dos líneas en blanco
    
    result = '\n'.join(result_lines)
    
    with open(output_file,'w') as f:
        f.write(result)
    
    return output_file