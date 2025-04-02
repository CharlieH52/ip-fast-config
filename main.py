from subprocess import run
base_config = {
    'NAME': 'Ethernet', # Default interface name.
    'IP': '192.168.0.0',
    'MASK': '255.255.255.0',
    'GATE': '192.168.0.1',
    'DNS1': '0.0.0.0',
    'DNS2': '0.0.0.0'
}

if __name__ == '__main__':
    while True:
        addr = input()

        if addr.isnumeric():
            break
        
        print(f'{addr} el valor ingresado es incorrecto...' )
        input()

    def normal_base_config_ip(addr):
        command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{base_config['NAME']}', 'static', f'{base_config['IP']}{addr}', f'{base_config['MASK']}', f'{base_config['GATE']}', 'store=persistent']
        print(f"Direccion IP: {base_config['IP']}")
        print(f"Mascara de subred: {base_config['MASK']}")
        print(f"Puerta de enlace predeterminada: {base_config['IP']}")
        run(command)

    def set_dns():
        command_DNS1 = ['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'{base_config['NAME']}', 'static', f'{base_config['DNS1']}', 'primary']
        print(f"Servidor DNS1: {base_config['DNS1']}")
        run(command_DNS1)
    
    def add_dns():
        command_DNS2 = ['netsh', 'interface', 'ipv4', 'add', 'dnsservers', f'{base_config['NAME']}', f'{base_config['DNS2']}']
        print(f"Servidor DNS2: {base_config['DNS2']}")
        run(command_DNS2)