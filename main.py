import subprocess
import os

from time import sleep

dicc_directory = os.path.join(os.getcwd(), "DATA_Inf")
file = "IP_BASE.txt"
directory = f"{dicc_directory}\{file}"
dicctionary = {}

def check_base_config():
    with open(directory, "r") as file:
        for items in file:
            name, data = items.strip().split(": ")
            dicctionary[name] = data

def command_execute(command_sequence):
    subprocess.run(command_sequence, shell=True)

def config_ip(input):
    check_base_config()
    command = ['netsh', 'interface', 'ipv4', 'set', 'address', f'"{dicctionary['NAME']}"', 'static', f'{dicctionary['IP']}{input}', f'{dicctionary['MASK']}', f'{dicctionary['GATE']}', 'store=persistent']
    command_execute(command)

def config_dns():
    check_base_config()
    command_DNS1 = ['netsh', 'interface', 'ipv4', 'set', 'dnsservers', f'{dicctionary['NAME']}', 'static', f'{dicctionary['DNS1']}', 'primary']
    command_execute(command_DNS1)
    command_DNS2 = ['netsh', 'interface', 'ipv4', 'add', 'dnsservers', f'{dicctionary['NAME']}', f'{dicctionary['DNS2']}']
    command_execute(command_DNS2)

value = input("Ingresa la nueva direccion: ")

try:
    config_ip(value)
except Exception as e:
    print(f'Error al ejecutar config_ip: {e}')
    sleep(20)

try:
    config_dns()
except Exception as e:
    print(f'Error al ejecutar config_dns: {e}')
    sleep(20)

input("Presiona ENTER para salir...")