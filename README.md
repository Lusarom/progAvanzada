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
 
 # **EJERCICIO 20** 
Escriba un programa que calcule la cantidad de gas en moles cuando el usuario suministra la presión, el volumen y la temperatura. Prueba tu programa determinando el número de moles de gas en un tanque de buceo. Un tanque de buceo típico contiene 12 litros de gas a una presión de 20,000,000 Pascales (aproximadamente 3,000 PSI). La temperatura ambiente es aproximadamente 20 grados Celsius o 68 grados Fahrenheit.
 [EJERCICIO 20](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio20.py).
 
  # **EJERCICIO 21**
Escriba un programa que permita al usuario ingresar valores para byh. El programa luego debe calcular y mostrar el área de un triángulo con longitud base by altura h.
 [EJERCICIO 21](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio21.py).

# **EJERCICIO 22**
En el ejercicio anterior, creó un programa que calculaba el área de un triángulo cuando se conocía la longitud de su base y su altura. También es posible calcular el área de un triángulo cuando se conocen las longitudes de los tres lados. Deje s1, s2 y s3
ser la longitud de los lados. Sea s = (s1 + s2 + s3) / 2. Entonces el área del triángulo se puede calcular usando la siguiente fórmula: area = s × (s − s1) × (s − s2) × (s − s3)
 [EJERCICIO 22](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio22.py).

# **EJERCICIO 23**
Un polígono es regular si sus lados tienen la misma longitud y los ángulos entre todos Los lados adyacentes son iguales. El área de un polígono regular se puede calcular usando la siguiente fórmula, donde s es la longitud de un lado yn es el número de lados: area = n × s2/
4 × tan (π / n).
 [EJERCICIO 23](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio23.py).

# **EJERCICIO 24**
Cree un programa que lea una duración del usuario como un número de días, horas, minutos y segundos. Calcule y muestre el número total de segundos representados por esta duración.
 [EJERCICIO 24](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio24.py).
 
 # **EJERCICIO 25**
En este ejercicio revertirá el proceso descrito en el ejercicio anterior. Desarrolle un programa que comience leyendo un número de segundos del usuario. Luego, su programa debe mostrar la cantidad de tiempo equivalente en el formulario D: HH: MM: SS, donde D, HH, MM y SS representan días, horas, minutos y segundos respectivamente. Las horas, minutos y segundos deben estar formateados para que ocupan exactamente dos dígitos, con un 0 inicial si es necesario.
 [EJERCICIO 25](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio25.py).
 
  # **EJERCICIO 26**
Python incluye una biblioteca de funciones para trabajar con el tiempo, incluida una función llamado asctime en el módulo de tiempo. Lee la hora actual del reloj interno de la computadora y la devuelve en un formato legible para humanos. Escribir un programa que muestra la hora y fecha actuales. Su programa no requerirá ninguna entrada de el usuario.
 [EJERCICIO 26](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio26.py).

  # **EJERCICIO 27**
Escriba un programa que calcule el índice de masa corporal (IMC) de un individuo. El programa debe comenzar leyendo una altura y un peso del usuario. Entonces debería use una de las siguientes dos fórmulas para calcular el IMC antes de mostrarlo. Si lees la altura en pulgadas y el peso en libras, entonces el índice de masa corporal es calculado usando la siguiente fórmula: IMC = peso / altura × altura (703).
 [EJERCICIO 27](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio27.py).

  # **EJERCICIO 28**
Escriba un programa que comience leyendo la temperatura del aire y la velocidad del viento del usuario. Una vez que se hayan leído estos valores, su programa debería mostrar la sensación térmica índice redondeado al entero más cercano.
 [EJERCICIO 28](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio28.py).
 
   # **EJERCICIO 29**
Escriba un programa que comience leyendo la temperatura del usuario en grados Celsius. Entonces su programa debe mostrar la temperatura equivalente en grados Fahrenheit y grados Kelvin. Los cálculos necesarios para convertir entre diferentes unidades de temperatura se pueden encontrar en internet.
 [EJERCICIO 29](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio29.py).

  # **EJERCICIO 30**
En este ejercicio creará un programa que lee la presión del usuario en kilopascales. Una vez que se ha leído la presión, su programa debe informar el equivalente presión en libras por pulgada cuadrada, milímetros de mercurio y atmósferas. Utilizar sus habilidades de investigación para determinar los factores de conversión entre estas unidades.
 [EJERCICIO 30](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio30.py).
 
 # **EJERCICIO 31**
Desarrolle un programa que lea un número entero de cuatro dígitos del usuario y muestre la suma de los dígitos en el número. Por ejemplo, si el usuario ingresa 3141, entonces su programa debería mostrar 3 + 1 + 4 + 1 = 9.
 [EJERCICIO 31](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio31.py).
 
  # **EJERCICIO 32**
Cree un programa que lea tres enteros del usuario y los muestre ordenados orden (de menor a mayor). Usa las funciones min y max para encontrar el más pequeño y valores más grandes. El valor medio se puede encontrar calculando la suma de los tres valores, y luego restando el valor mínimo y el valor máximo.
 [EJERCICIO 32](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio32.py).

  # **EJERCICIO 33**
Una panadería vende hogazas de pan por $ 3.49 cada una. El pan de un día tiene un descuento de 60 por ciento. Escriba un programa que comience leyendo la cantidad de panes de un día pan que se compra al usuario. Entonces su programa debe mostrar el regular precio del pan, el descuento porque tiene un día y el precio total. Toda la los valores deben mostrarse con dos decimales y los puntos decimales en todos
de los números deben alinearse cuando el usuario ingresa valores razonables.
 [EJERCICIO 33](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio33.py).
 
  # **EJERCICIO 34**
Escriba un programa que lea un número entero del usuario. Entonces su programa debería muestra un mensaje que indica si el entero es par o  impar.
   [EJERCICIO 34](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio34.py).
  
  # **EJERCICIO 35**
Escribir un programa que implemente la conversión de años humanos a años de perros. descrito en el párrafo anterior. Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones de dos o más humanos años. Su programa debe mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.
   [EJERCICIO 35](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio35.py).
   
  # **EJERCICIO 36**
En este ejercicio creará un programa que lee una letra del alfabeto del usuario. Si el usuario ingresa a, e, i, o u, entonces su programa debería mostrar un mensaje indicando que la letra ingresada es una vocal. Si el usuario ingresa y entonces su programa debería mostrar un mensaje que indique que a veces y es una vocal, y a veces y es una consonante. De lo contrario, su programa debería mostrar un mensaje que indica que el La letra es una consonante.
   [EJERCICIO 36](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio36.py).
  
  # **EJERCICIO 37**
Escriba un programa que determine el nombre de una forma a partir de su número de lados. Leer el número de lados del usuario y luego informa el nombre apropiado como parte de Un mensaje significativo. Su programa debe admitir formas con 3 hasta (e incluyendo) 10 lados. Si se ingresa un número de lados fuera de este rango entonces su programa debería mostrar un mensaje de error apropiado.
   [EJERCICIO 37](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio37.py).
  
  # **EJERCICIO 38**
La duración de un mes varía de 28 a 31 días. En este ejercicio crearás Un programa que lee el nombre de un mes del usuario como una cadena. Entonces tu El programa debe mostrar la cantidad de días en ese mes. Mostrar "28 o 29 días" para febrero para que se aborden los años bisiestos.
   [EJERCICIO 38](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio38.py).
  
  # **EJERCICIO 39**
La siguiente tabla enumera el nivel de sonido en decibelios para varios ruidos comunes.

| NOISE| DECIBEL LEBEL (dB)|
| ----- | ---- |
| Jackhammer | 130|
| as lawnmover|106| 
| Alarm clock| 70 |
| Quiet room | 40 |

Escriba un programa que lea un nivel de sonido en decibelios del usuario. Si el usuario ingresa un nivel de decibelios que coincide con uno de los ruidos en la tabla y luego su programa debería mostrar un mensaje que contenga solo ese ruido. Si el usuario ingresa un número de decibelios entre los ruidos enumerados, entonces su programa debería mostrar un mensaje indicando qué ruidos está entre el nivel.
   [EJERCICIO 39](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio39.py).
  
  # **EJERCICIO 40**
Un triángulo se puede clasificar en función de la longitud de sus lados como isósceles equiláteros o escaleno. Los 3 lados de un triángulo equilátero tienen la misma longitud. Un isósceles el triángulo tiene dos lados que tienen la misma longitud y un tercer lado que es diferente longitud. Si todos los lados tienen diferentes longitudes, entonces el triángulo es escaleno. Escriba un programa que lea las longitudes de 3 lados de un triángulo del usuario. Muestra un mensaje que indica el tipo de triángulo.
   [EJERCICIO 40](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio40.py).
  
  # **EJERCICIO 41**
La siguiente tabla enumera una octava de notas musicales, comenzando con C central, a lo largo
con sus frecuencias:

| NOTE| FREQUENCY (Hz)|
| ----- | ---- |
| C4 | 261.63|
| D4 | 293.66| 
| E4 | 329.63 
| F4 | 349.23|
| G4 | 392.00|
| A4 | 440.00|
| B4 | 493.88|

Comience escribiendo un programa que lea el nombre de una nota del usuario y
muestra la frecuencia de la nota. Su programa debe admitir todas las notas enumeradas
previamente.
   [EJERCICIO 41](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio41.py).
  
  # **EJERCICIO 42**
   [EJERCICIO 42](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio42.py).
  
  # **EJERCICIO 43**
   [EJERCICIO 43](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio43.py).
  
  # **EJERCICIO 44**
   [EJERCICIO 44](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio44.py).
  
  # **EJERCICIO 45**
   [EJERCICIO 45](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio45.py).
  
  # **EJERCICIO 46**
   [EJERCICIO 46](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio46.py).
  
  # **EJERCICIO 47**
   [EJERCICIO 47](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio47.py).
  
  # **EJERCICIO 48**
   [EJERCICIO 48](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio48.py).
  
  # **EJERCICIO 49**
   [EJERCICIO 49](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio49.py).
  
  # **EJERCICIO 50**
   [EJERCICIO 50](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio50.py).
  
  # **EJERCICIO 51**
   [EJERCICIO 51](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio51.py).
  
  # **EJERCICIO 52**
   [EJERCICIO 52](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio52.py).
  
  # **EJERCICIO 53**
   [EJERCICIO 53](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio53.py).
  
  # **EJERCICIO 54**
   [EJERCICIO 54](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio54.py).
  
  # **EJERCICIO 55**
   [EJERCICIO 55](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio55.py).
  
  # **EJERCICIO 56**
   [EJERCICIO 56](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio56.py).
  
  # **EJERCICIO 57**
   [EJERCICIO 57](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio57.py).
  
  # **EJERCICIO 58**
   [EJERCICIO 58](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio58.py).
  
  # **EJERCICIO 59**
   [EJERCICIO 59](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio59.py).
  

  
  
  
  
  
  
  




































  
 
































