# -*- coding: utf-8 -*-

# Habilita la division de punto flotante por defecto, crucial para calculos.
from __future__ import division
import datetime

class Producto(object):
    """
    Representa un producto individual con su tipo, cantidad y precio.
    Ahora esta clase no se preocupa por el formato de almacenamiento.
    """
    tipos_productos = {1: 'Libro', 2: u'Electrónico', 3: 'Ropa'}
    
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
        """
        subtotal = self.calcular_subtotal()
        impuesto = 0.0

        if self.tipo == 'Electrónico':
            impuesto = subtotal * 0.16
        elif self.tipo == 'Ropa':
            impuesto = subtotal * 0.08
        
        return impuesto

    def to_dict(self):
        """Convierte la instancia del producto a un diccionario simple."""
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "tipo": u"%s" % self.tipo,
            "precio": self.precio_unitario
        }

    def __str__(self):
        """Representacion simple y legible para humanos."""
        return '(%s - %s)' % (self.nombre, self.tipo)


class Pedido(object):
    """
    Representa un pedido completo de un cliente, conteniendo una lista de productos.
    Ahora esta clase no sabe como se guarda o carga desde un archivo.
    """
    def __init__(self, cliente_nombre, fecha=None):
        self.cliente_nombre = cliente_nombre
        # La fecha se puede pasar como argumento para reconstruir un pedido desde archivo
        self.fecha = fecha if fecha is not None else datetime.datetime.now()
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
        Calcula el gran total del pedido.
        """
        total = 0.0
        for producto in self.productos:
            total += producto.calcular_subtotal() + producto.calcular_impuesto()
        return total
