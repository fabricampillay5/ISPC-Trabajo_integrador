"""" EVIDENCIA 3 """

from menu import mostrar_menu
from ingreso import ingresos
from egreso import egresos
from cmensual import cmensuals
from fin import fins


mostrar_menu()
comando = input("Ingresa la opcion correspondiente: ")
while comando != '4':
    if comando == "1":
        ingresos()
    elif comando == "2":
        egresos()
    elif comando == "3":
        cmensuals()
    else: 
        print("No ingresaste una opcion valida")
        
    comando = input("Ingresa la opcion correspondiente: ")
 
fins()