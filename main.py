from time import sleep
from subprocess import run
import os

class IPAutomatron:
    def __init__(self):
        self.file_path = os.path.join(os.getcwd(), 'base.config')
        self.dictionary = self.check_base_config()

    def check_base_config(self):
        dictionary = {}
        try:
            with open(self.file_path, 'r') as file:
                for items in file.readlines():
                    key, name = items.strip().split('= ')
                    dictionary[key] = name
                return dictionary
            
        except FileNotFoundError as e:
            print("Ocurrio un problema al leer el archivo '.config'")
        
    def command_execute(self, command_sequence):
        return run(command_sequence)

    def normal_config_ip(self, input):
        command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['IP']}{input}', f'{self.dictionary['MASK']}', f'{self.dictionary['GATE']}', 'store=persistent']
        print("Estableciendo configuracion...")
        print(f"Direccion IP: {self.dictionary['IP']}")
        print(f"Mascara de subred: {self.dictionary['MASK']}")
        print(f"Puerta de enlace predeterminada: {self.dictionary['IP']}")
        self.command_execute(command)

    def new_config(self, input):
        command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['IP']}{input}', 'store=persistent']
        self.command_execute(command)

    def set_dns(self):
        command_DNS1 = ['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'{self.dictionary['NAME']}', 'static', f'{self.dictionary['DNS1']}', 'primary']
        print(f"Servidor DNS1: {self.dictionary['DNS1']}")
        self.command_execute(command_DNS1)
    
    def add_dns(self):
        command_DNS2 = ['netsh', 'interface', 'ipv4', 'add', 'dnsservers', f'{self.dictionary['NAME']}', f'{self.dictionary['DNS2']}']
        print(f"Servidor DNS2: {self.dictionary['DNS2']}")
        self.command_execute(command_DNS2)
    
    def first_configuration(self, input):
        self.normal_config_ip(ip)
        sleep(1)
        self.set_dns()
        sleep(1)
        self.add_dns()
        sleep(1)

if __name__ == '__main__':
    ipa = IPAutomatron()

    PRODUCTION_MODE = True
    if PRODUCTION_MODE == True:
        while True:
            try:
                if not os.path.isfile(ipa.file_path):
                    with open(ipa.file_path, 'w') as file:
                        file.write(
                            'NAME= \n'
                            'IP= \n'
                            'MASK= \n'  
                            'GATE= \n' 
                            'DNS1= \n'
                            'DNS2= '
                        )
                    print(f"Se ha creado el archivo con exito el archivo '{ipa.file_path}'.")
                    print("Agrega los valores base de tu configuracion.")
                    print("No olvides dejar vacio el ultimo campo de la direccion IP.")
                    print("Ejemplo: 192.168.0. ")
                    break

                if os.path.isfile(ipa.file_path):
                    break

            except PermissionError:
                print("Ocurrio un problema al crear el archivo '.config'")

        ip = input("Ingresa el ultimo campo de la direccion IP: ")
        ipa.first_configuration(ip)

        while True:
            new_change = input('Quieres cambiar la dirección de nuevo? (Y/N)').upper()
            if new_change == 'Y':        
                ip = input("Ingresa la nueva direccion: ")
                ipa.new_config(ip)

            elif new_change == 'N':
                break
            else:
                print('Entrada no valida. Por favor, ingresa "Y" para si o "N" para no.')

    if PRODUCTION_MODE == False:
        # Revision del diccionario:
        # La clave IP (para este caso) debe ser en este formato 192.168.0.
        for key in ipa.dictionary:
            print(key, ipa.dictionary[f'{key}'])