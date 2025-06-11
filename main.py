# -*- coding: utf-8 -*-

# Se importan las clases definidas en models.py
from models import Pedido, Producto
from utils import *
from io_operations import *



# Lista en memoria para almacenar todos los pedidos registrados durante la sesion.
pedidos_registrados = []

def main():
    """
    Funcion principal que muestra el menu y maneja la logica del programa.
    """
    while True:
        imprimir_menu()
        
        opcion = raw_input("Seleccione una opcion: ")
        
        if opcion == '1':
            pedidos_registrados.append( registrar_nuevo_pedido() )
        elif opcion == '2':
            generar_reporte(pedidos_registrados)
        elif opcion == '3':
            guardar_pedidos(pedidos_registrados)
            print "Saliendo del programa. Adios."
            break
        else:
            print "\nOpcion no valida. Por favor, intente de nuevo."


# Punto de entrada del script.
if __name__ == '__main__':
    main()