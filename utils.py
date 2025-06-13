# -*- coding: utf-8 -*-
from models import Pedido, Producto
from io_operations import *

def generar_reporte(pedidos_sesion):
    """
    Muestra en consola un resumen de todos los pedidos (de archivo y de sesion).
    """
    print "\n--- Reporte de Pedidos Registrados ---"
    
    # La logica de carga y deserializacion ahora esta encapsulada en io_operations
    pedidos_archivo = cargar_pedidos_desde_archivo()
    
    todos_los_pedidos = pedidos_archivo + pedidos_sesion

    if not todos_los_pedidos:
        print "No hay pedidos para mostrar."
        return

    # Imprime cada objeto Pedido de forma unificada
    for numero_pedido, pedido in enumerate(todos_los_pedidos):
        imprimir_pedido(pedido, numero_pedido)
            
    print "\n--- Fin del Reporte ---"


def guardar_pedidos(pedidos):
    """
    Pasa la lista de pedidos a la capa de I/O para ser guardados.
    """
    if not pedidos:
        print "No hay pedidos nuevos en esta sesion para guardar."
        return

    guardar_pedidos_a_archivo(pedidos)


def registrar_nuevo_pedido():
    """
    Flujo para solicitar datos al usuario y crear un nuevo objeto Pedido.
    """
    print "\n--- Registrar Nuevo Pedido ---"
    nombre_cliente = raw_input("Nombre del cliente: ")
    
    pedido = Pedido(nombre_cliente)
    
    while True:
        nombre_producto = leer_nombre_producto()
        tipo_producto = leer_tipo_producto()
        cantidad = leer_cantidad()
        precio = leer_precio()
        
        producto = Producto(nombre_producto, tipo_producto, cantidad, precio)
        pedido.agregar_producto(producto)

        continuar = raw_input("\nDesea agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break

    print "\nPedido para '%s' registrado exitosamente." % nombre_cliente
    return pedido
