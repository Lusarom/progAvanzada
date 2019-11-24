# **PROGRAMACION AVANZADA**

### *Objetivo*
Aporta al perfil del Ingeniero Mecatrónico la capacidad de análisis, desarrollo e implementación de software de aplicación, orientado a objetos y visual, con el fin de apoyar la productividad y competitividad de los sitemas mecatrónicos.

### *Temario*
1. Introducción.
2. Objetos y clases.
3. Herencia.
4. Poliformismo.
5. Programación visual.
6. Formas, controles, eventos.

### *Lenguaje de programación*
* Python (Versión 3)

### *Bibliografía*
* The Python Woorbook: A Brief Introduction with Exercises and Solutions. 
* Raúl González Duque, Python para todos.

# *PYTHON*
Lenguaje de programación **creado** por **Guido Van Rossum** en los **90's**. Favorece **sitaxis amplia**, y un **código legible**.
Se trata de un **lenguaje interpretado o de script**, con tipado **dinámico fuertemente tipado**, multiplataforma y **orientado a objetos**.
Un lenguaje interpretado o de script es aquel que se ejecuta utilizando un programa intermedio llamado **"interprete"**. Su ventaja de ejecución es más rápida. Sin embargo los lenguajes interpretados son más flexibles o más cortados.
Python es un ejemplo de lenguaje de alto nivel como: **C++, C#, PHP, Pascal, Java**. Los lenguajes de bajo nivel se refieren a lenguajes máquina o ensamblador, sin embargo lo lenguajes de alto nivel siepre tienen que ser convertidos a lenguajes de bajo nivel para que se puedan correr.
Python guarda sus **"scripts"** con terminación **".py"**

## *Sistema Tipado Dinámico*
Su característica se refiere a que no es necesario declarar el tipo de dato que contendrá una determinada variable, sino que sus tipos se determinarán en tiempo de ejecución que según el que se asigne, y el tipo de esta puede cambiar si se le asigna valor de otro tipo.

## *Fuertemente Tipado*
No se permite tratar una variable como si fuera de tipo distinto al que tiene, es necesario convertir explícita dicha variable al nuevo tipo previamente, ejemplo: *Sí se tiene una variable que contiene un tipo de texto "tipo cadena o script"* no podemos tratarla como un número **(sumar la cadena "9"+ 8)** *int ("9")+8.*

## *Multiplataforma*
El intérprete de Python está disponible en multitud de pltaforma **(unix, solaris, linux, DOS, Windows, OS/2, Mac OS)** por lo que si usamos librerías específicas nuestro programa podrá correr en los sistemas.

## *Sistema Orientado a Objetos*
Es un paradigma de programación en el que los conceptos del mundo real, relevantes a nuestro problema se trasladan a clases y objetos en nuestro programa. Su ejecución consiste en una serie de interacciones entre varios objetos.

## *¿Por qué Python?*
El software es el núcleo de todas las herramientas que utilizamos hoy en día: Casi tosos usamos redes sociales para comunicarnos, muchas personas están conectadas a internet hoy en día, y la mayoría de los trabajos siempre se efctúa con una computadora para tener el trabajo hecho. Como resultado la demanda que sepa programar ha aumentado. Python es un lenguaje que con su sintaxis simple, clara y sencilla puede automatizar simples tareas como:

* Mover y reenombrar miles de archivos y clasificarlos en folder.
* Llenar de forma automática formularios en internet.
* Descargar archivos o extraer información de páginas de internet de forma masiva.
* Hacer que la computadora envíe al teléfono información de quien lo usa.
* Checar e-mail y contestar automaticamente.

# *COMANDOS*
  #### • **print**
Imprime el mensaje en la pantalla o dispositivo de salida. El mensaje puede ser una cadena de caracteres o cualquier objeto que sea convertible a cadena de caracteres.
  #### • **input**
Permite al usuario introducir información, utilizando el teclado en la variable donde se guarda dicha información, que es de tipo cadena de caracteres.
  

Sí un programa no fuera más que una lista de órdenes a ejecutar de forma secuencial una a una, no tendrá mucha utilidad; las sentencias condicionales nos permiten comprobar condiciones y hacer que nuestro programa se conforme una de otra.
Aquí es donde cobran su importancia tipo booleano y operaciones.

#### Condicional *if*
La forma más simple de una sentencia condicional es un *if* (del inglés sí) seguido de la condición a evaluar dos puntos (*:*) y en la siguiente línea e identado el código o ejecutar en caso de que se cumpla dicha condición.
La identación del código se realiza con 4 espacios.

#### Estructura *if else* 
Permite añadir el comportamiento en caso de que la condición no resulte cierta, por ejemplo:

#### Estrutura *elif elif else*
El comando *elif* es la contracción de *else if*, en español "sí, no" ejemplo:

# **EJERCICIO 1**
Cree un programa que muestre su nombre y la dirección postal completa formateada en la forma en que normalmente lo verías en el exterior de un sobre. Su programa no necesita leer ninguna entrada del usuario. 
 [EJERCICIO 1](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio01.py).

# **EJERCICIO 2**
Escriba un programa que le pida al usuario que ingrese su nombre. El programa debe responda con un mensaje que diga hola al usuario, usando su nombre.
 [EJERCICIO 2](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio02.py).

# **EJERCICIO 3**
Escriba un programa que le pida al usuario que ingrese el ancho y la longitud de una habitación. Una vez los valores han sido leídos, su programa debe calcular y mostrar el área de habitación. La longitud y el ancho se ingresarán como números de coma flotante. Incluir unidades en su mensaje de solicitud y salida; ya sea pies o metros, dependiendo de qué unidad con la que se siente más cómodo trabajando.
 [EJERCICIO 3](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio03.py).

# **EJERCICIO 4**
Cree un programa que lea la longitud y el ancho del campo de un agricultor del usuario en pies Muestra el área del campo en acres.
 [EJERCICIO 4](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio04.py).

# **EJERCICIO 5**
En muchas jurisdicciones se agrega un pequeño depósito a los envases de bebidas para alentar a las personas para reciclarlos En una jurisdicción particular, beba recipientes de un litro o menos tienen un depósito de $ 0.10, y los recipientes de bebidas que contienen más de un litro tienen, Depósito de $ 0.25. Escriba un programa que lea el número de contenedores de cada tamaño del usuario. Su programa debe continuar calculando y mostrando el reembolso que será recibido por devolver esos contenedores. Formatee la salida para que incluya un dólar firmar y siempre muestra exactamente dos decimales.
 [EJERCICIO 5](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio05.py).

# **EJERCICIO 6**
El programa que cree para este ejercicio comenzará leyendo el costo de una comida ordenado en un restaurante del usuario. Luego, su programa calculará el impuesto y propina para la comida. Use su tasa impositiva local cuando calcule la cantidad de impuestos adeudados. Calcule la propina como el 18 por ciento de la cantidad de comida (sin el impuesto). La salida de su programa debe incluir el monto de los impuestos, el monto de la propina y el total general de la comida incluye tanto el impuesto como la propina. Formatee la salida para que todos los valores se muestran con dos decimales.
 [EJERCICIO 6](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio06.py).

# **EJERCICIO 7**
Escriba un programa que lea un entero positivo, n, del usuario y luego muestre el suma de todos los enteros de 1 a n. La suma de los primeros n enteros positivos puede ser calculado usando la fórmula: sum=(n)(n+1)/2.
 [EJERCICIO 7](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio07.py).

# **EJERCICIO 8**
Un minorista en línea vende dos productos: widgets y artilugios. Cada widget pesa 75 gramos Cada artilugio pesa 112 gramos. Escribe un programa que lea el número de widgets y la cantidad de artilugios en un pedido del usuario. Entonces tu programa debe calcular y mostrar el peso total de la orden.
 [EJERCICIO 8](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio08.py).

# **EJERCICIO 9**
Imagina que acabas de abrir una nueva cuenta de ahorros que genera un interés del 4% por año. El interés que gana se paga al final del año y se agrega al saldo de la cuenta de ahorro. Escriba un programa que comience leyendo el cantidad de dinero depositada en la cuenta del usuario. Entonces su programa debería calcule y muestre el monto en la cuenta de ahorros después de 1, 2 y 3 años. Monitor cada cantidad para que se redondee a 2 decimales.
 [EJERCICIO 9](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio09.py).

# **EJERCICIO 10**
Cree un programa que lea dos enteros, "a" y "b", del usuario. Su programa debe calcular y mostrar.
## • The sum of a and b
## • The difference when b is subtracted from a
## • The product of a and b
## • The quotient when a is divided b y b
## • The remainder when a is divided b y b
## • The result of log10 a
## • The result of a^b
 [EJERCICIO 10](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio10.py).




















