# -*- coding: utf-8 -*-
from models import Producto

def imprimir_menu():
	print "\n===== Sistema de Gestion de Pedidos ====="
	print "1. Registrar un nuevo pedido"
	print "2. Generar reporte de todos los pedidos"
	print "3. Guardar pedidos y salir"

def imprimir_pedido(pedido, numero_pedido):
	print "\n No: %d | Cliente: %s | Fecha: %s | Cantidad artículos: %d | Total: $%.2f " % (numero_pedido + 1, 
																							pedido.cliente_nombre, 
																							pedido.fecha.strftime('%Y-%m-%d'), 
																							pedido.total_articulos(), 
																							pedido.calcular_total_pedido())	
    
def leer_nombre_producto():
	print "\nAgregando producto al pedido:"
	nombre_producto = raw_input("  Nombre del producto: ")
	return nombre_producto

def leer_tipo_producto():
	while True:
		tipo_producto = raw_input("  Tipo - 1)Libro, 2)Electrónico, 3)Ropa \n Selecciona un tipo: ")
		# Se valida que el tipo de producto sea uno de los permitidos.
		try:
		    if int(tipo_producto) in Producto.tipos_productos.keys():
		        break
		    else:
		        print "  Error: Tipo de producto no valido. Intente de nuevo."
		except ValueError:
			print "Introduzca un valor númerico especificado en la lista"

	return tipo_producto

def leer_cantidad():
	while True:
		try:
			cantidad = int(raw_input("  Cantidad: "))
			return cantidad
		except ValueError:
			print 'Introduzca un valor entero valido'

def leer_precio():
	while True:
		try:
			precio = float(raw_input("  Precio unitario: "))
			return precio
		except ValueError:
			print 'Introduzca un valor decimal valido'


def leer_pedidos_de_archivo():
	try:
	    with open('pedidos.txt', 'r') as f:
	        lineas_archivo = f.readlines()
	        if lineas_archivo:
	            return lineas_archivo
	except IOError:
	    # Si el archivo no existe, simplemente no se muestra esta seccion.
	    pass
	return []
		
def guardar_pedidos_a_archivo(pedidos):

    # Se utiliza 'with' para garantizar que el archivo se cierre correctamente.
    with open('pedidos.txt', 'a') as f:
        for pedido in pedidos:
            linea = pedido.a_string_para_archivo()
            f.write(linea + '\n')
    
    print "\nTodos los pedidos han sido guardados en 'pedidos.txt'."
