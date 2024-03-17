from subprocess import run
from os import getcwd

from UsefullFunctions import FileManager

man = FileManager()

class IPFunctions:
    def __init__(self):
        self.config_path = man.new_path(getcwd(), 'config')
        self.file_path = man.new_path(self.config_path, 'base.config')
        self.dictionary = self.check_base_config()

    def check_base_config(self):
        dictionary = {}
        return man.dictionary_reader(dictionary, self.file_path)
        
    def command_execute(self, command_sequence):
        return run(command_sequence)

    def normal_config_ip(self, input):
        command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['IP']}{input}', f'{self.dictionary['MASK']}', f'{self.dictionary['GATE']}', 'store=persistent']
        self.command_execute(command)

    def new_config(self, input):
        command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['IP']}{input}', 'store=persistent']
        self.command_execute(command)

    def set_dns(self):
        command_DNS1 = ['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['DNS1']}', 'primary']
        self.command_execute(command_DNS1)
    
    def add_dns(self):
        command_DNS2 = ['netsh', 'interface', 'ipv4', 'add', 'dnsservers', f'{self.dictionary['NAME']}', f'{self.dictionary['DNS2']}']
        self.command_execute(command_DNS2)