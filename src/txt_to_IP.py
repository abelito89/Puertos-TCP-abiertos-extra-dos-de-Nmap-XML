import re

with open('/content/Subred63.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if 'Nmap scan report for' in line:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]
            print('\n\n')
            print(f'IP: {ip}')
        elif 'PORT' in line and 'STATE' in line and 'SERVICE' in line and 'VERSION' in line:
            print(line.strip())
        elif re.match(r'\d+/tcp', line):
            print(line.strip())