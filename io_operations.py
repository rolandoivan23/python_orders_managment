# -*- coding: utf-8 -*-
from models import Producto, Pedido
import datetime
import json
import io 

# --- Funciones de Salida (Escritura en Consola y Archivo) ---

def imprimir_menu():
    print "\n===== Sistema de Gestion de Pedidos ====="
    print "1. Registrar un nuevo pedido"
    print "2. Generar reporte de todos los pedidos"
    print "3. Guardar pedidos y salir"

def imprimir_pedido(pedido, numero_pedido):
    """
    Imprime un objeto Pedido en un formato consistente.
    """
    plantilla = u"\n No: %d | Cliente: %s | Fecha: %s | Cantidad artículos: %d | Total: $%.2f "
    
    fecha_str = pedido.fecha.strftime('%Y-%m-%d').decode('utf-8')

    print plantilla % (
        numero_pedido + 1,
        pedido.cliente_nombre,
        fecha_str,
        pedido.total_articulos(),
        pedido.calcular_total_pedido()
    )

def guardar_pedidos_a_archivo(pedidos):
    """
    Convierte cada objeto Pedido a una línea JSON y la guarda en el archivo.
    """
    with io.open('pedidos.txt', 'a', encoding='utf-8') as f:
        for pedido in pedidos:
            datos_pedido = {
                'cliente': pedido.cliente_nombre,
                'fecha': pedido.fecha.strftime('%Y-%m-%d %H:%M:%S').decode('utf-8'),
                'total': pedido.calcular_total_pedido(),
                'productos': [p.to_dict() for p in pedido.productos]
            }
            linea_json = json.dumps(datos_pedido, ensure_ascii=False)
            f.write(linea_json + u'\n')
    
    print "\nTodos los pedidos han sido guardados en 'pedidos.txt'."

# --- Funciones de Entrada (Lectura de Consola y Archivo) ---

def leer_nombre_producto():
    print "\nAgregando producto al pedido:"
    return raw_input("  Nombre del producto: ").decode('utf-8')

def leer_tipo_producto():
    while True:
        # 1. Se crea la cadena de opciones, que sera unicode por los valores del diccionario.
        opciones = " | ".join([u"%d)%s" % (k, v) for k, v in sorted(Producto.tipos_productos.items())])
        
        # 2. Se crea la plantilla del prompt como una cadena unicode.
        prompt_unicode = u"  Tipo - %s \n  Selecciona un tipo: " % opciones
        
        # 3. Se codifica el prompt a utf-8 ANTES de pasarlo a raw_input.
        prompt_utf8 = prompt_unicode.encode('utf-8')
        
        tipo_producto_str = raw_input(prompt_utf8)
        
        try:
            tipo_producto_num = int(tipo_producto_str)
            if tipo_producto_num in Producto.tipos_productos:
                # Se devuelve el valor unicode del diccionario ('Libro', 'Electrónico', etc.)
                return Producto.tipos_productos[tipo_producto_num]
            else:
                print "  Error: Tipo de producto no valido. Intente de nuevo."
        except ValueError:
            print "  Introduzca un valor numerico especificado en la lista"

def leer_cantidad():
    while True:
        try:
            return int(raw_input("  Cantidad: "))
        except ValueError:
            print '  Introduzca un valor entero valido'

def leer_precio():
    while True:
        try:
            return float(raw_input("  Precio unitario: "))
        except ValueError:
            print '  Introduzca un valor decimal valido'

def cargar_pedidos_desde_archivo():
    """
    Lee cada linea JSON del archivo y la deserializa en un objeto Pedido.
    """
    pedidos_cargados = []
    try:
        with io.open('pedidos.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                if not linea.strip():
                    continue
                datos = json.loads(linea)
                
                fecha_obj = datetime.datetime.strptime(datos['fecha'], '%Y-%m-%d %H:%M:%S')
                pedido_obj = Pedido(datos['cliente'], fecha=fecha_obj)
                
                for prod_data in datos['productos']:
                    producto_obj = Producto(
                        prod_data['nombre'],
                        prod_data['tipo'],
                        prod_data['cantidad'],
                        prod_data['precio']
                    )
                    pedido_obj.agregar_producto(producto_obj)
                
                pedidos_cargados.append(pedido_obj)
    except (IOError, ValueError, KeyError):
        return []
    return pedidos_cargados
