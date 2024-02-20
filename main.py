import os

from time import sleep
from IPFunctions import IPFunctions

method_manager = IPFunctions()

ip_input = input("Ingresa la nueva direccion: ")

method_manager.config_ip(ip_input)
method_manager.config_dns()
input("Presiona ENTER para salir...")