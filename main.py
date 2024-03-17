from time import sleep
from UsefullFunctions import FileManager
from IPFunctions import IPFunctions

ifun = IPFunctions()
man = FileManager()

def first_configuration(input):
    ifun.normal_config_ip(ip)
    sleep(1)
    ifun.set_dns()
    sleep(1)
    ifun.add_dns()
    sleep(1)

if __name__ == '__main__':
    PRODUCTION_MODE = True
    if PRODUCTION_MODE == True:
        if not man.is_valid_directory(ifun.config_path):
            man.make_new_directory(ifun.config_path)
            with open(ifun.file_path, 'w') as file:
                file.write(
                    'NAME= \n'
                    'IP= \n'
                    'MASK= \n'  
                    'GATE= \n' 
                    'DNS1= \n'
                    'DNS2= '
                )


        ip = input("Ingresa la nueva direccion: ")
        first_configuration(ip)

        while True:
            new_change = input('Quieres cambiar la dirección de nuevo? (Y/N)').upper()
            if new_change == 'Y':        
                ip = input("Ingresa la nueva direccion: ")
                ifun.new_config(ip)

            elif new_change == 'N':
                break
            else:
                print('Entrada no valida. Por favor, ingresa "Y" para si o "N" para no.')

    if PRODUCTION_MODE == False:
        # Revision del diccionario:
        # La clave IP (para este caso) debe ser en este formato 192.168.0.
        for key in ifun.dictionary:
            print(key, ifun.dictionary[f'{key}'])