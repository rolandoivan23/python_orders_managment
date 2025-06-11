README.txt=========================================
Sistema de Gestion de Pedidos - README
=========================================

Este proyecto es una aplicacion de consola para gestionar pedidos de una tienda virtual, desarrollada en Python 2.7.

---
Diseño General
---

La solucion esta disenada siguiendo principios de Programacion Orientada a Objetos (POO) y con una estructura modular para separar responsabilidades:

1.  **models.py**: Contiene las clases que modelan los datos del sistema.
    * `Producto`: Representa un articulo individual. Contiene la logica para calcular su subtotal y los impuestos correspondientes segun su tipo (electronico, ropa, libro).
    * `Pedido`: Representa una orden completa de un cliente. Contiene una lista de objetos `Producto` y metodos para calcular el total del pedido, contar los articulos y formatear la informacion para su almacenamiento.

2.  **main.py**: Es el punto de entrada de la aplicacion. Se encarga de:
    * Mostrar un menu interactivo al usuario en la consola.
    * Orquestar el flujo de la aplicacion: registrar pedidos, generar reportes y guardar los datos antes de salir.
    * Mantener una lista en memoria de todos los pedidos registrados durante la sesion.

3.  **utils.py**: Nos ayuda con tareas generales como generar los reportes:

4.  **io_operations.py**: Contiene funciones para leer de consola, leer del archivo de pedidos e imprimir en pantalla
    

---
Suposiciones Tomadas
---
* **Tipos de Producto**: El sistema espera que los tipos de producto sean escritos mediante las opciones 1, 2 y 3 para 'Libros', 'Electrónica' y 'Ropa'
* **Persistencia de Datos**: Los datos se guardan en el archivo 'pedidos.txt' únicamente cuando el usuario selecciona la opcion "Guardar y salir".
* **Validez de la Entrada**: El manejo de errores para entradas invalidas o información repetida es mínimo (inicialmente).

---
Instrucciones para Correr el Programa
---

Este proyecto esta pensado para correr con una versión de python 2.7, para el desarrollo inicial se utilizo una máquina virtual con un ubuntu 18.04 para 
cuestiones de compatibilidad, esto para evitar problemas con las instalaciones mediante compilación en versiones mas modernas de las distribuciones de 
linux principales.

Pasos para poder correr el programa

	sudo apt update
	sudo apt upgrade
	sudo apt-get install python2.7


	Abra una terminal o linea de comandos en ese directorio.
	Ejecute el siguiente comando:

	    python2.7 main.py

	 Siga las instrucciones que aparecen en el menu de la consola.

Nota: Lo recomendable es siempre usar un entorno virtual para evitar problemas entre versiónes de librerías o paquetes cuando estemos trabajando con otro proyecto.
Para este caso con fines prácticos y como es una instalación completamente limpia se uso el interprete directamente.


	Alternativa usando IDE PyCharm

		 Prerequisitos, tener preinstado python
		 	-Windows: bajar el ejecutable e instalarlo (recordar el path de instalación)

		 Instalar el IDE, se recomienda la versión comunity edition
		 Abrir la carpeta del proyecto
		 En settings (File -> Settings), sección del proyecto:
		 	-Click en agregar interprete
		 	-Seleccionar opción de virtualenv
		 	-Seleccionar la carpeta deonde se instala python 2.7

		 Ya con esto podremos correr nuestro archivo main.py (click derecho y play)
