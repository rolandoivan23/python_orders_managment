# -*- coding: utf-8 -*-
from models import Pedido
from io_operations import *

def print_order(pedido, numero_pedido):
	print "\nPedido #%d" % (numero_pedido + 1)	
	print "  Cliente: %s" % pedido.cliente_nombre
	print "  Fecha: %s" % pedido.fecha.strftime('%Y-%m-%d')
	print "  Numero total de productos: %d" % pedido.total_articulos()
	print "  Total del pedido (con impuestos): $%.2f" % pedido.calcular_total_pedido()


#Muestra en consola un resumen de todos los pedidos registrados. 
def generar_reporte(pedidos_registrados):  
    
    print "\n--- Reporte de Pedidos Registrados ---"

    hay_pedidos_mostrados = False #Para saber si se imprimieron pedidos leidos del archivo

    # Primero, se leen, deserializan y muestran los pedidos guardados en el archivo
    try:
       
       	pedidos_archivo = leer_pedidos_de_archivo()
       	if(len(pedidos_archivo) > 0):
       		hay_pedidos_mostrados = True

       	

       	#Por cada línea del archivo(cada pedido) se regresa un diccionario con su información.
        for i, linea in enumerate(pedidos_archivo):        	
        	datos_pedido = Pedido.deserializar_linea(linea)
        	pedido = Pedido(datos_pedido['Cliente'])
        	for producto in datos_pedido['Productos']:
        		pedido.agregar_producto(Producto(producto['nombre'], producto['tipo'], producto['cantidad'], producto['precio']))	
            	print_order(pedido, i)
            
    except IOError:
        # Si el archivo no existe, simplemente no se muestra esta seccion.
        pass


    if not pedidos_registrados and not hay_pedidos_mostrados:
        print "No hay pedidos para mostrar."
        return

    for i, pedido in enumerate(pedidos_registrados):
        print_order(pedido, i + len(pedidos_archivo))

    print "\n--- Fin del Reporte ---"


def guardar_pedidos(pedidos):
    """
    Guarda todos los pedidos en un archivo 'pedidos.txt'. 
    """
    if not pedidos:
        print "No hay pedidos para guardar."
        return

    guardar_pedidos_a_archivo(pedidos)

def registrar_nuevo_pedido():
    """
    Flujo para solicitar datos al usuario y registrar un nuevo pedido. 
    """
    print "\n--- Registrar Nuevo Pedido ---"
    nombre_cliente = raw_input("Nombre del cliente: ")
    
    pedido = Pedido(nombre_cliente)
    
    while True:
        nombre_producto = leer_nombre_producto()
        tipo_producto = leer_tipo_producto()
        cantidad = leer_cantidad()
        precio = leer_precio()
        producto = Producto(nombre_producto, 
                            Producto.tipos_productos[int(tipo_producto)], 
                            cantidad, 
                            precio)
        pedido.agregar_producto(producto)

        continuar = raw_input("\nDesea agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break

    print "\nPedido para '%s' registrado exitosamente." % nombre_cliente
    return pedido
    