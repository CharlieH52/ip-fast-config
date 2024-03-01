from time import sleep
from IPFunctions import IPFunctions

method_manager = IPFunctions()

def show_dictionary():
    for name, dir in method_manager.dictionary.items():
        print(f'{name} {dir}')

#show_dictionary()
if __name__ == '__main__':
    while True:
        ip_input = input("Ingresa la nueva direccion:")
        if ip_input.isdigit():
            if (int(ip_input) > 0 and int(ip_input) < 255):
                method_manager.config_ip(ip_input)
                sleep(1)
                method_manager.config_dns()
                sleep(1)
                break
input("Presiona ENTER para salir...")