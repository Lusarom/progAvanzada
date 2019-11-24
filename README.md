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
 ![E1]()

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
##### • La suma de a y b
##### • La diferencia cuando b se resta de a
##### • El producto de a y b
##### • El cociente cuando a se divide por b y b
##### • El resto cuando a se divide por b y b
##### • El resultado de log10 a
##### • El resultado de a ^ b
 [EJERCICIO 10](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio10.py).

# **EJERCICIO 11**
En los Estados Unidos, la eficiencia del combustible para vehículos normalmente se expresa en millas por galón (MPG). En Canadá, la eficiencia del combustible normalmente se expresa en litros por cien kilómetros (L / 100 km). Usa tus habilidades de investigación para determinar cómo convertir de MPG a L / 100 km. Luego cree un programa que lea un valor del usuario en América unidades y muestra la eficiencia de combustible equivalente en unidades canadienses.
 [EJERCICIO 11](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio11.py).


# **EJERCICIO 12**
La superficie de la Tierra es curva y la distancia entre grados de longitud. varía con la latitud. Como resultado, encontrar la distancia entre dos puntos en la superficie de la Tierra es más complicado que simplemente usar el teorema de Pitágoras. Sea (t1, g1) y (t2, g2) la latitud y longitud de dos puntos en la Tierra superficie. La distancia entre estos puntos, siguiendo la superficie de la Tierra, en
kilómetros es: distancia = 6371.01 × arccos (sin (t1) × sin (t2) + cos (t1) × cos (t2) × cos (g1 - g2)). Cree un programa que permita al usuario ingresar la latitud y longitud de dos puntos en la Tierra en grados. Su programa debe mostrar la distancia entre los puntos, siguiendo la superficie de la tierra, en kilómetros.
 [EJERCICIO 12](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio12.py).
 
 # **EJERCICIO 13**
Considere el software que se ejecuta en una máquina de autopago. Una tarea que debe ser capaz de realizar es determinar cuánto cambio proporcionar cuando el comprador paga para una compra en efectivo Escriba un programa que comience leyendo una cantidad de centavos del usuario como entero. Luego, su programa debe calcular y mostrar las denominaciones de monedas que deberían usarse para dar esa cantidad de cambio al comprador. El cambio debe administrarse utilizando la menor cantidad de monedas posible. Suponga que la máquina está cargada con centavos, monedas de cinco centavos, monedas de diez centavos, cuartos, locos y toonies.
 [EJERCICIO 13](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio13.py).

 # **EJERCICIO 14**
Muchas personas piensan en su altura en pies y pulgadas, incluso en algunos países que utiliza principalmente el sistema métrico. Escriba un programa que lea un número de pies de el usuario, seguido de varias pulgadas. Una vez que se leen estos valores, su programa debe calcular y mostrar el número equivalente de centímetros.
 [EJERCICIO 14](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio14.py).
 
  # **EJERCICIO 15**
En este ejercicio, creará un programa que comienza leyendo una medida en pies del usuario. Entonces su programa debe mostrar la distancia equivalente en pulgadas, yardas y millas. Use Internet para buscar los factores de conversión necesarios si no los tienes memorizados. 
 [EJERCICIO 15](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio15.py).

  # **EJERCICIO 16**
Escriba un programa que comience leyendo un radio, r, del usuario. El programa continúe calculando y mostrando el área de un círculo con radio r y el volumen de una esfera con radio r. Use la constante pi en el módulo matemático en su cálculos.
 [EJERCICIO 16](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio16.py).
 
  # **EJERCICIO 17**
 Escriba un programa que lea la masa de un poco de agua y el cambio de temperatura. del usuario Su programa debe mostrar la cantidad total de energía que debe ser agregado o eliminado para lograr el cambio de temperatura deseado.
 [EJERCICIO 17](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio17.py).


  # **EJERCICIO 18**
El volumen de un cilindro se puede calcular multiplicando el área de su circular base por su altura. Escriba un programa que lea el radio del cilindro, junto con su altura, desde el usuario y calcula su volumen. Mostrar el resultado redondeado a uno decimal.
 [EJERCICIO 18](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio18.py).
 
 # **EJERCICIO 19**
Cree un programa que determine qué tan rápido viaja un objeto cuando golpea el suelo. El usuario ingresará la altura desde la cual se cae el objeto en metros (m). Debido a que el objeto se cae, su velocidad inicial es de 0 m / s. Supongamos que la aceleración debido a la gravedad es de 9.8 m / s2. Puedes usar la fórmula vf = v2 i + 2ad para calcular el velocidad final, vf, cuando se conoce la velocidad inicial, vi, aceleración, a y distancia, d.
 [EJERCICIO 19](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio19.py).








