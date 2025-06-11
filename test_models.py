# -*- coding: utf-8 -*-

import unittest
from models import Producto, Pedido

class TestCalculosPedidos(unittest.TestCase):
    """
    Suite de pruebas para validar los cálculos de impuestos y totales
    en las clases Producto y Pedido.
    """

    # ===============================================
    # == Pruebas para la clase Producto            ==
    # ===============================================

    def test_impuesto_libro_es_cero(self):
        """Verifica que el impuesto para un producto de tipo 'Libro' es 0%."""
        libro = Producto('El Quijote', 'Libro', 1, 100.0)
        self.assertEqual(libro.calcular_impuesto(), 0.0, "El impuesto para libros debe ser 0")

    def test_impuesto_ropa_es_8_porciento(self):
        """Verifica que el impuesto para un producto de tipo 'Ropa' es 8%."""
        playera = Producto('Playera', 'Ropa', 2, 150.0) # Subtotal = 300
        impuesto_esperado = 300.0 * 0.08 # 24.0
        self.assertAlmostEqual(playera.calcular_impuesto(), impuesto_esperado, "El impuesto para ropa debe ser 8%")

    def test_impuesto_electronico_es_16_porciento(self):
        """Verifica que el impuesto para un producto de tipo 'Electrónico' es 16%."""
        teclado = Producto('Teclado Mecanico', 'Electrónico', 1, 1000.0) # Subtotal = 1000
        impuesto_esperado = 1000.0 * 0.16 # 160.0
        self.assertAlmostEqual(teclado.calcular_impuesto(), impuesto_esperado, "El impuesto para electronicos debe ser 16%")

    # ===============================================
    # == Pruebas para la clase Pedido              ==
    # ===============================================

    def test_total_pedido_un_producto(self):
        """Verifica el calculo del total de un pedido con un solo producto."""
        pedido = Pedido("Cliente A")
        playera = Producto('Playera', 'Ropa', 1, 100.0) # Subtotal 100, Impuesto 8
        pedido.agregar_producto(playera)
        total_esperado = 100.0 + 8.0 # 108.0
        self.assertAlmostEqual(pedido.calcular_total_pedido(), total_esperado)

    def test_total_pedido_multiples_productos(self):
        """Verifica el calculo del total de un pedido con productos de distintos tipos."""
        pedido = Pedido("Cliente B")
        
        # Producto 1: Libro (sin impuesto)
        # Subtotal: 200.0, Impuesto: 0.0
        libro = Producto('Libro de Python', 'Libro', 2, 100.0)
        pedido.agregar_producto(libro)

        # Producto 2: Electronico (16% impuesto)
        # Subtotal: 500.0, Impuesto: 80.0
        mouse = Producto('Mouse Gamer', 'Electrónico', 1, 500.0)
        pedido.agregar_producto(mouse)

        # Producto 3: Ropa (8% impuesto)
        # Subtotal: 300.0, Impuesto: 24.0
        sudadera = Producto('Sudadera', 'Ropa', 1, 300.0)
        pedido.agregar_producto(sudadera)

        # Total esperado = (200+0) + (500+80) + (300+24) = 200 + 580 + 324 = 1104.0
        total_esperado = 1104.0
        self.assertAlmostEqual(pedido.calcular_total_pedido(), total_esperado)

    def test_total_pedido_vacio_es_cero(self):
        """Verifica que el total de un pedido sin productos es cero."""
        pedido_vacio = Pedido("Cliente C")
        self.assertEqual(pedido_vacio.calcular_total_pedido(), 0.0)

# Esto permite correr el archivo directamente como un script
if __name__ == '__main__':
    unittest.main()
