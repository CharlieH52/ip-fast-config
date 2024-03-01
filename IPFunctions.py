import subprocess
import os

class IPFunctions:
    def __init__(self):
        self.dictionary = self.check_base_config()

    def check_base_config(self):
        dictionary = {}
        file_config = 'IP_BASE.txt'
        file_directory = 'DATA_Inf'
        dir_route = os.path.join(os.getcwd(), file_directory)
        file_route = os.path.join(dir_route, file_config)
        try:
            with open(file_route, 'r') as file:
                for items in file:
                    name, data = items.strip().split(': ')
                    dictionary[name] = data
        except FileNotFoundError as e:
            print(f'Ocurrio un problema al leer el archivo: {file_config}\n'
                  f'{e}\n'
                  )
        return dictionary
        
    def command_execute(self, command_sequence):
        subprocess.run(command_sequence)

    def config_ip(self, input):
        command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['IP']}{input}', f'{self.dictionary['MASK']}', f'{self.dictionary['GATE']}', 'store=persistent']
        self.command_execute(command)

    def config_dns(self):
        command_DNS1 = ['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['DNS1']}', 'primary']
        self.command_execute(command_DNS1)
        command_DNS2 = ['netsh', 'interface', 'ipv4', 'add', 'dnsservers', f'{self.dictionary['NAME']}', f'{self.dictionary['DNS2']}']
        self.command_execute(command_DNS2)