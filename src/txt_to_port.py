import re

def parse_txt(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split('\n\n')

    ip_dict = {}
    for block in data:
        lines = block.split('\n')
        if ': ' in lines[0]:
            ip = lines[0].split(': ')[1]
            for line in lines[1:]:
                if 'open' in line:
                    port = line.split('/')[0]
                    if port not in ip_dict:
                        ip_dict[port] = [ip]
                    else:
                        ip_dict[port].append(ip)
    return ip_dict

def write_to_txt(ip_dict, output_path):
    with open(output_path, 'w') as file:
        for port, ips in ip_dict.items():
            file.write(f'Port: {port}\n')
            for ip in ips:
                file.write(f'IP: {ip}\n')
            file.write('\n')

file_path = '/content/Subred63_puertos_abiertos_por_cada_IP.txt'  # Ruta del archivo de entrada
output_path = '/content/Subred63_IP_por_cada_puerto_abierto.txt'  # Ruta del archivo de salida

ip_dict = parse_txt(file_path)
write_to_txt(ip_dict, output_path)