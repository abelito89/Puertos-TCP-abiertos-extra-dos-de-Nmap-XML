import re

def parse_txt(file_path):
    '''
    Analiza un archivo de texto y extrae información sobre las direcciones IP y los números de puerto.

    Parámetros:
    file_path (str): La ruta al archivo de texto que se va a analizar. Este archivo debe ser la salida de la función txt_to_IP.txt_to_IP

    Devuelve:
    dict: Un diccionario donde las claves son los números de puerto y los valores son listas de direcciones IP.
    '''
    with open(file_path, 'r') as file:
        data = file.read().split('\n')

    ip_dict = {'default': []}  # Agrega una entrada predeterminada a ip_dict
    blank_lines = 0
    for line in data:
        # Si la línea está vacía, incrementa el contador de líneas en blanco
        if not line.strip():
            blank_lines += 1
            # Si hay tres líneas en blanco consecutivas, detiene la lectura
            if blank_lines == 3:
                break
            continue
        else:
            blank_lines = 0

        # Busca 'IP: ' en la línea para identificar las direcciones IP
        if 'IP: ' in line:
            ip = line.split(': ')[1]
        # Busca la barra en la línea para identificar los números de puerto
        elif '/' in line and 'open' in line:  
            port = line.split('/')[0]
            if port not in ip_dict:
                ip_dict[port] = [ip]
            else:
                ip_dict[port].append(ip)
    return ip_dict




def write_to_txt(ip_dict, output_path):
    '''
    Escribe un diccionario de direcciones IP y números de puerto en un archivo de texto.

    Parámetros:
    ip_dict (dict): Un diccionario donde las claves son los números de puerto y los valores son listas de direcciones IP.
    output_path (str): La ruta al archivo de texto donde se va a escribir la información.

    Devuelve:
    None
    '''
    with open(output_path, 'w') as file:
        for port, ips in ip_dict.items():
            file.write(f'Port: {port}\n')
            for ip in ips:
                file.write(f'IP: {ip}\n')
            file.write('\n')