import subprocess
import os

class IPFunctions():
    def __init__(self):
        self.dictionary = self.check_base_config()

    def check_base_config(self):
        dictionary = {}
        file_config = 'IP_BASE.txt'
        directory = os.path.join(os.getcwd(), file_config)
        try:
            with open(directory, 'r') as file:
                for items in file:
                    name, data = items.strip().split(': ')
                    dictionary[name] = data
        except FileNotFoundError as e:
            print(f'Ocurrio un problema al leer el archivo: {file_config}\n'
                  f'{e}\n'
                  )
        return dictionary
        
    def command_execute(self, command_sequence):
        subprocess.run(command_sequence, shell=True)

    def config_ip(self, input):
        dictionary = self.dictionary()
        command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{dictionary['NAME']}', 'static', f'{dictionary['IP']}{input}', f'{dictionary['MASK']}', f'{dictionary['GATE']}', 'store=persistent']
        self.command_execute(command)

    def config_dns(self, dictionary):
        self.check_base_config()
        command_DNS1 = ['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'{dictionary['NAME']}', 'static', f'{dictionary['DNS1']}', 'primary']
        self.command_execute(command_DNS1)
        command_DNS2 = ['netsh', 'interface', 'ipv4', 'add', 'dnsservers', f'{dictionary['NAME']}', f'{dictionary['DNS2']}']
        self.command_execute(command_DNS2)