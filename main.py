from IPFunctions import IPFunctions

# Compilation code:
# COPY: pyinstaller --clean --onefile --distpath="D:\Documentos\Portfoil-Programacion\OUTPUT-FILES\CONFIGURADOR-IP" --name=Configurar-IP-x64 main.py

method_manager = IPFunctions()
ip_input = input("Ingresa la nueva direccion: ")
time_reboot = 0

def firstConfig():
    method_manager.config_ip(ip_input, time_reboot)
    method_manager.config_dns()

firstConfig()

while True:
    new_change = input('Quieres cambiar la dirección de nuevo? (Y/N)').upper()
    if new_change == 'Y':        
        time_reboot = 1
        ip_input = input("Ingresa la nueva direccion: ")
        method_manager.config_ip(ip_input, time_reboot)
    elif new_change == 'N':
        break
    else:
        print('Entrada no valida. Por favor, ingresa "Y" para si o "N" para no.')