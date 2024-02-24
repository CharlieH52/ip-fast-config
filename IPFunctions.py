import subprocess
import os

class IPFunctions():
    def __init__(self):
        self.dictionary = self.check_base_config()

    def route_searcher(self, directory_name, file_name):
        directory_route = os.path.join(os.getcwd(), directory_name)
        file_route = os.path.join(directory_route, file_name)
        dir_list = [directory_route, file_route]
        return dir_list

    def check_base_config(self):
        dictionary = {}
        directory_name = 'DATA_Inf'
        file_name = 'IP_BASE.txt'
        directory = self.route_searcher(directory_name, file_name)
        try:
            with open(directory[1], 'r') as file:
                for items in file:
                    name, data = items.strip().split(': ')
                    dictionary[name] = data
        except FileNotFoundError as e:
            print(f'Ocurrio un problema al leer el archivo {file_name}:\n'
                  f'{e}\n'
                  )
        return dictionary
        
    def command_execute(self, command_sequence):
        subprocess.run(command_sequence, shell=True)

    def config_ip(self, input, reboot):
        dictionary = self.dictionary()
        
        if reboot == 0:
            command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{dictionary['NAME']}', 'static', f'{dictionary['IP']}{input}', f'{dictionary['MASK']}', f'{dictionary['GATE']}', 'store=persistent']
            self.command_execute(command)

        if reboot == 1:
            command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{dictionary['NAME']}', 'static', f'{dictionary['IP']}{input}', 'store=persistent']
            self.command_execute(command)

    def config_dns(self, dictionary):
        self.check_base_config()
        command_DNS1 = ['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'{dictionary['NAME']}', 'static', f'{dictionary['DNS1']}', 'primary']
        self.command_execute(command_DNS1)
        command_DNS2 = ['netsh', 'interface', 'ipv4', 'add', 'dnsservers', f'{dictionary['NAME']}', f'{dictionary['DNS2']}']
        self.command_execute(command_DNS2)