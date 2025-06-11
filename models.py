# -*- coding: utf-8 -*-

# Habilita la division de punto flotante por defecto, crucial para calculos.
from __future__ import division
import datetime
import json

class Producto(object):

    tipos_productos = {1: 'Libro', 2: 'Electrónico', 3: 'Ropa'}
   
    """
    Representa un producto individual con su tipo, cantidad y precio.
    """
    def __init__(self, nombre, tipo, cantidad, precio_unitario):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)

    def calcular_subtotal(self):
        """Calcula el costo total del producto sin impuestos."""
        return self.cantidad * self.precio_unitario

    def calcular_impuesto(self):
        """
        Calcula el impuesto basado en el tipo de producto.
        - Electronicos: 16%
        - Ropa: 8%
        - Libros: 0%
        """
        subtotal = self.calcular_subtotal()
        impuesto = 0.0

        if self.tipo == 'Electrónico':
            impuesto = subtotal * 0.16
        elif self.tipo == 'Ropa':
            impuesto = subtotal * 0.08
        
        return impuesto

    def __str__(self):
        """Representacion en string del producto."""
        return "{ \"nombre\": \"%s\", \"cantidad\": %d, \"tipo\": \"%s\", \"precio\": %f }" % (self.nombre, self.cantidad, self.tipo, self.precio_unitario)


class Pedido(object):
    """
    Representa un pedido completo de un cliente, conteniendo una lista de productos.
    """
    def __init__(self, cliente_nombre):
        self.cliente_nombre = cliente_nombre
        # La fecha se captura automaticamente al crear el pedido.
        self.fecha = datetime.datetime.now()
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un objeto de tipo Producto a la lista del pedido."""
        if isinstance(producto, Producto):
            self.productos.append(producto)

    def total_articulos(self):
        """Calcula el numero total de articulos individuales en el pedido."""
        return sum(p.cantidad for p in self.productos)

    def calcular_total_pedido(self):
        """
        Calcula el gran total del pedido, sumando los subtotales de los
        productos y sus respectivos impuestos.
        """
        total = 0.0
        for producto in self.productos:
            total += producto.calcular_subtotal() + producto.calcular_impuesto()
        return total

    def a_string_para_archivo(self):
        """
        Genera una representacion de una sola linea del pedido para guardarlo
        en un archivo de texto. 
        """
        # Se genera una lista de los nombres de los productos para mostrarla.
        nombres_productos = ', '.join(str(p) for p in self.productos)
        
        formato_fecha = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        total_pedido = self.calcular_total_pedido()

        return 'Cliente: %s | Fecha: %s | Total: %.2f | Productos: [%s]' % (
            self.cliente_nombre, formato_fecha, total_pedido, nombres_productos
        )

    @staticmethod
    def deserializar_linea(linea):
        """
        Toma una linea del archivo de texto y la deserializa en un
        diccionario con los datos principales del pedido.
        Debido al formato simple, los productos no se reconstruyen como objetos.
        """
        datos_pedido = {}

        partes = linea.strip().split(' | ')
        for parte in partes:
            clave, valor = parte.split(': ', 1)
            datos_pedido[clave.strip()] = valor.strip()

            if(clave == 'Productos'):
                datos_pedido['Productos'] = json.loads(datos_pedido['Productos'])

        
        pedido = Pedido(datos_pedido['Cliente'])
        for producto in datos_pedido['Productos']:
            pedido.agregar_producto(Producto(producto['nombre'], producto['tipo'], producto['cantidad'], producto['precio']))
    
        return pedido