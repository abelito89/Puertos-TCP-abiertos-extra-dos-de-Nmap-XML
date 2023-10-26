import re

def txt_to_IP(text, output_file):
    lines = text.split('\n')
    result = ''
    for line in lines:
        if 'Nmap scan report for' in line:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]
            result += '\n\n' + f'IP: {ip}\n'
        elif 'PORT' in line and 'STATE' in line and 'SERVICE' in line and 'VERSION' in line:
            result += line.strip() + '\n'
        elif re.match(r'\d+/tcp', line):
            result += line.strip() + '\n'
    with open(output_file,'w') as f:
        f.write(result)
    return output_file