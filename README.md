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

# **EJERCICIO 1** Dirección postal.
Cree un programa que muestre su nombre y la dirección postal completa formateada en la forma en que normalmente lo verías en el exterior de un sobre. Su programa no necesita leer ninguna entrada del usuario. 
 [EJERCICIO 1](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio01.py).
 ![E1]()

# **EJERCICIO 2** *Hola*.
Escriba un programa que le pida al usuario que ingrese su nombre. El programa debe responda con un mensaje que diga hola al usuario, usando su nombre.
 [EJERCICIO 2](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio02.py).

# **EJERCICIO 3** *Área de una habitación*.
Escriba un programa que le pida al usuario que ingrese el ancho y la longitud de una habitación. Una vez los valores han sido leídos, su programa debe calcular y mostrar el área de habitación. La longitud y el ancho se ingresarán como números de coma flotante. Incluir unidades en su mensaje de solicitud y salida; ya sea pies o metros, dependiendo de qué unidad con la que se siente más cómodo trabajando.
 [EJERCICIO 3](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio03.py).

# **EJERCICIO 4** *Área de un campo*.
Cree un programa que lea la longitud y el ancho del campo de un agricultor del usuario en pies Muestra el área del campo en acres.
 [EJERCICIO 4](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio04.py).

# **EJERCICIO 5** *Depósitos de botellas*.
En muchas jurisdicciones se agrega un pequeño depósito a los envases de bebidas para alentar a las personas para reciclarlos En una jurisdicción particular, beba recipientes de un litro o menos tienen un depósito de $ 0.10, y los recipientes de bebidas que contienen más de un litro tienen, Depósito de $ 0.25. Escriba un programa que lea el número de contenedores de cada tamaño del usuario. Su programa debe continuar calculando y mostrando el reembolso que será recibido por devolver esos contenedores. Formatee la salida para que incluya un dólar firmar y siempre muestra exactamente dos decimales.
 [EJERCICIO 5](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio05.py).

# **EJERCICIO 6** *Impuestos y propina*.
El programa que cree para este ejercicio comenzará leyendo el costo de una comida ordenado en un restaurante del usuario. Luego, su programa calculará el impuesto y propina para la comida. Use su tasa impositiva local cuando calcule la cantidad de impuestos adeudados. Calcule la propina como el 18 por ciento de la cantidad de comida (sin el impuesto). La salida de su programa debe incluir el monto de los impuestos, el monto de la propina y el total general de la comida incluye tanto el impuesto como la propina. Formatee la salida para que todos los valores se muestran con dos decimales.
 [EJERCICIO 6](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio06.py).

# **EJERCICIO 7** *Suma de los primeros n enteros positivos*.
Escriba un programa que lea un entero positivo, n, del usuario y luego muestre el suma de todos los enteros de 1 a n. La suma de los primeros n enteros positivos puede ser calculado usando la fórmula: sum=(n)(n+1)/2.
 [EJERCICIO 7](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio07.py).

# **EJERCICIO 8** *Widgets y gizmos*.
Un minorista en línea vende dos productos: widgets y artilugios. Cada widget pesa 75 gramos Cada artilugio pesa 112 gramos. Escribe un programa que lea el número de widgets y la cantidad de artilugios en un pedido del usuario. Entonces tu programa debe calcular y mostrar el peso total de la orden.
 [EJERCICIO 8](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio08.py).

# **EJERCICIO 9** *Interés compuesto*.
Imagina que acabas de abrir una nueva cuenta de ahorros que genera un interés del 4% por año. El interés que gana se paga al final del año y se agrega al saldo de la cuenta de ahorro. Escriba un programa que comience leyendo el cantidad de dinero depositada en la cuenta del usuario. Entonces su programa debería calcule y muestre el monto en la cuenta de ahorros después de 1, 2 y 3 años. Monitor cada cantidad para que se redondee a 2 decimales.
 [EJERCICIO 9](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio09.py).

# **EJERCICIO 10** *Aritmética*
Cree un programa que lea dos enteros, "a" y "b", del usuario. Su programa debe calcular y mostrar.
##### • La suma de a y b
##### • La diferencia cuando b se resta de a
##### • El producto de a y b
##### • El cociente cuando a se divide por b y b
##### • El resto cuando a se divide por b y b
##### • El resultado de log10 a
##### • El resultado de a ^ b
 [EJERCICIO 10](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio10.py).

# **EJERCICIO 11** *Eficiencia de combustible*.
En los Estados Unidos, la eficiencia del combustible para vehículos normalmente se expresa en millas por galón (MPG). En Canadá, la eficiencia del combustible normalmente se expresa en litros por cien kilómetros (L / 100 km). Usa tus habilidades de investigación para determinar cómo convertir de MPG a L / 100 km. Luego cree un programa que lea un valor del usuario en América unidades y muestra la eficiencia de combustible equivalente en unidades canadienses.
 [EJERCICIO 11](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio11.py).


# **EJERCICIO 12** *Distancia entre dos puntos en la Tierra*.
La superficie de la Tierra es curva y la distancia entre grados de longitud. varía con la latitud. Como resultado, encontrar la distancia entre dos puntos en la superficie de la Tierra es más complicado que simplemente usar el teorema de Pitágoras. Sea (t1, g1) y (t2, g2) la latitud y longitud de dos puntos en la Tierra superficie. La distancia entre estos puntos, siguiendo la superficie de la Tierra, en
kilómetros es: distancia = 6371.01 × arccos (sin (t1) × sin (t2) + cos (t1) × cos (t2) × cos (g1 - g2)). Cree un programa que permita al usuario ingresar la latitud y longitud de dos puntos en la Tierra en grados. Su programa debe mostrar la distancia entre los puntos, siguiendo la superficie de la tierra, en kilómetros.
 [EJERCICIO 12](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio12.py).
 
 # **EJERCICIO 13** *Hacer cambios*.
Considere el software que se ejecuta en una máquina de autopago. Una tarea que debe ser capaz de realizar es determinar cuánto cambio proporcionar cuando el comprador paga para una compra en efectivo Escriba un programa que comience leyendo una cantidad de centavos del usuario como entero. Luego, su programa debe calcular y mostrar las denominaciones de monedas que deberían usarse para dar esa cantidad de cambio al comprador. El cambio debe administrarse utilizando la menor cantidad de monedas posible. Suponga que la máquina está cargada con centavos, monedas de cinco centavos, monedas de diez centavos, cuartos, locos y toonies.
 [EJERCICIO 13](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio13.py).

 # **EJERCICIO 14** *Unidades de altura*.
Muchas personas piensan en su altura en pies y pulgadas, incluso en algunos países que utiliza principalmente el sistema métrico. Escriba un programa que lea un número de pies de el usuario, seguido de varias pulgadas. Una vez que se leen estos valores, su programa debe calcular y mostrar el número equivalente de centímetros.
 [EJERCICIO 14](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio14.py).
 
  # **EJERCICIO 15** *Unidades de distancia*. 
En este ejercicio, creará un programa que comienza leyendo una medida en pies del usuario. Entonces su programa debe mostrar la distancia equivalente en pulgadas, yardas y millas. Use Internet para buscar los factores de conversión necesarios si no los tienes memorizados. 
 [EJERCICIO 15](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio15.py).

  # **EJERCICIO 16** *Área y volúmen*. 
Escriba un programa que comience leyendo un radio, r, del usuario. El programa continúe calculando y mostrando el área de un círculo con radio r y el volumen de una esfera con radio r. Use la constante pi en el módulo matemático en su cálculos.
 [EJERCICIO 16](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio16.py).
 
  # **EJERCICIO 17** *Capacidad de calor*.
 Escriba un programa que lea la masa de un poco de agua y el cambio de temperatura. del usuario Su programa debe mostrar la cantidad total de energía que debe ser agregado o eliminado para lograr el cambio de temperatura deseado.
 [EJERCICIO 17](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio17.py).


  # **EJERCICIO 18** *Volúmen de un cilíndro*.
El volumen de un cilindro se puede calcular multiplicando el área de su circular base por su altura. Escriba un programa que lea el radio del cilindro, junto con su altura, desde el usuario y calcula su volumen. Mostrar el resultado redondeado a uno decimal.
 [EJERCICIO 18](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio18.py).
 
 # **EJERCICIO 19** *Caída libre*.
Cree un programa que determine qué tan rápido viaja un objeto cuando golpea el suelo. El usuario ingresará la altura desde la cual se cae el objeto en metros (m). Debido a que el objeto se cae, su velocidad inicial es de 0 m / s. Supongamos que la aceleración debido a la gravedad es de 9.8 m / s2. Puedes usar la fórmula vf = v2 i + 2ad para calcular el velocidad final, vf, cuando se conoce la velocidad inicial, vi, aceleración, a y distancia, d.
 [EJERCICIO 19](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio19.py).
 
 # **EJERCICIO 20** *Ley del gas ideal*.
Escriba un programa que calcule la cantidad de gas en moles cuando el usuario suministra la presión, el volumen y la temperatura. Prueba tu programa determinando el número de moles de gas en un tanque de buceo. Un tanque de buceo típico contiene 12 litros de gas a una presión de 20,000,000 Pascales (aproximadamente 3,000 PSI). La temperatura ambiente es aproximadamente 20 grados Celsius o 68 grados Fahrenheit.
 [EJERCICIO 20](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio20.py).
 
  # **EJERCICIO 21**  *Área de un triángulo*.
Escriba un programa que permita al usuario ingresar valores para byh. El programa luego debe calcular y mostrar el área de un triángulo con longitud base by altura h.
 [EJERCICIO 21](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio21.py).

# **EJERCICIO 22** *Área de un triángulo (nuevamente)*.
En el ejercicio anterior, creó un programa que calculaba el área de un triángulo cuando se conocía la longitud de su base y su altura. También es posible calcular el área de un triángulo cuando se conocen las longitudes de los tres lados. Deje s1, s2 y s3
ser la longitud de los lados. Sea s = (s1 + s2 + s3) / 2. Entonces el área del triángulo se puede calcular usando la siguiente fórmula: area = s × (s − s1) × (s − s2) × (s − s3)
 [EJERCICIO 22](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio22.py).

# **EJERCICIO 23** *Área de un polígono regular*. 
Un polígono es regular si sus lados tienen la misma longitud y los ángulos entre todos Los lados adyacentes son iguales. El área de un polígono regular se puede calcular usando la siguiente fórmula, donde s es la longitud de un lado yn es el número de lados: area = n × s2/
4 × tan (π / n).
 [EJERCICIO 23](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio23.py).

# **EJERCICIO 24** *Unidades de tiempo*. 
Cree un programa que lea una duración del usuario como un número de días, horas, minutos y segundos. Calcule y muestre el número total de segundos representados por esta duración.
 [EJERCICIO 24](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio24.py).
 
 # **EJERCICIO 25** *Unidades de tiempo (nuevamente)*.
En este ejercicio revertirá el proceso descrito en el ejercicio anterior. Desarrolle un programa que comience leyendo un número de segundos del usuario. Luego, su programa debe mostrar la cantidad de tiempo equivalente en el formulario D: HH: MM: SS, donde D, HH, MM y SS representan días, horas, minutos y segundos respectivamente. Las horas, minutos y segundos deben estar formateados para que ocupan exactamente dos dígitos, con un 0 inicial si es necesario.
 [EJERCICIO 25](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio25.py).
 
  # **EJERCICIO 26** *Hora actual*.
Python incluye una biblioteca de funciones para trabajar con el tiempo, incluida una función llamado asctime en el módulo de tiempo. Lee la hora actual del reloj interno de la computadora y la devuelve en un formato legible para humanos. Escribir un programa que muestra la hora y fecha actuales. Su programa no requerirá ninguna entrada de el usuario.
 [EJERCICIO 26](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio26.py).

  # **EJERCICIO 27** *Índice de masa corporal*.
Escriba un programa que calcule el índice de masa corporal (IMC) de un individuo. El programa debe comenzar leyendo una altura y un peso del usuario. Entonces debería use una de las siguientes dos fórmulas para calcular el IMC antes de mostrarlo. Si lees la altura en pulgadas y el peso en libras, entonces el índice de masa corporal es calculado usando la siguiente fórmula: IMC = peso / altura × altura (703).
 [EJERCICIO 27](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio27.py).

  # **EJERCICIO 28** *Sensación térmica*.
Escriba un programa que comience leyendo la temperatura del aire y la velocidad del viento del usuario. Una vez que se hayan leído estos valores, su programa debería mostrar la sensación térmica índice redondeado al entero más cercano.
 [EJERCICIO 28](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio28.py).
 
   # **EJERCICIO 29** *Celsius a Fahrenheit y Kelvin*.
Escriba un programa que comience leyendo la temperatura del usuario en grados Celsius. Entonces su programa debe mostrar la temperatura equivalente en grados Fahrenheit y grados Kelvin. Los cálculos necesarios para convertir entre diferentes unidades de temperatura se pueden encontrar en internet.
 [EJERCICIO 29](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio29.py).

  # **EJERCICIO 30** *Unidades de presión*.
En este ejercicio creará un programa que lee la presión del usuario en kilopascales. Una vez que se ha leído la presión, su programa debe informar el equivalente presión en libras por pulgada cuadrada, milímetros de mercurio y atmósferas. Utilizar sus habilidades de investigación para determinar los factores de conversión entre estas unidades.
 [EJERCICIO 30](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio30.py).
 
 # **EJERCICIO 31** Suma de los dígitos en un entero. 
Desarrolle un programa que lea un número entero de cuatro dígitos del usuario y muestre la suma de los dígitos en el número. Por ejemplo, si el usuario ingresa 3141, entonces su programa debería mostrar 3 + 1 + 4 + 1 = 9.
 [EJERCICIO 31](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio31.py).
 
  # **EJERCICIO 32** Ordenar 3 enteros.
Cree un programa que lea tres enteros del usuario y los muestre ordenados orden (de menor a mayor). Usa las funciones min y max para encontrar el más pequeño y valores más grandes. El valor medio se puede encontrar calculando la suma de los tres valores, y luego restando el valor mínimo y el valor máximo.
 [EJERCICIO 32](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio32.py).

  # **EJERCICIO 33** Pan de un día.
Una panadería vende hogazas de pan por $ 3.49 cada una. El pan de un día tiene un descuento de 60 por ciento. Escriba un programa que comience leyendo la cantidad de panes de un día pan que se compra al usuario. Entonces su programa debe mostrar el regular precio del pan, el descuento porque tiene un día y el precio total. Toda la los valores deben mostrarse con dos decimales y los puntos decimales en todos
de los números deben alinearse cuando el usuario ingresa valores razonables.
 [EJERCICIO 33](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio33.py).
 
  # **EJERCICIO 34** ¿Par o impar?.
Escriba un programa que lea un número entero del usuario. Entonces su programa debería muestra un mensaje que indica si el entero es par o  impar.
   [EJERCICIO 34](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio34.py).
  
  # **EJERCICIO 35** Años de um perro. 
Escribir un programa que implemente la conversión de años humanos a años de perros. descrito en el párrafo anterior. Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones de dos o más humanos años. Su programa debe mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.
   [EJERCICIO 35](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio35.py).
   
  # **EJERCICIO 36** Vocal o Consonante.
En este ejercicio creará un programa que lee una letra del alfabeto del usuario. Si el usuario ingresa a, e, i, o u, entonces su programa debería mostrar un mensaje indicando que la letra ingresada es una vocal. Si el usuario ingresa y entonces su programa debería mostrar un mensaje que indique que a veces y es una vocal, y a veces y es una consonante. De lo contrario, su programa debería mostrar un mensaje que indica que el La letra es una consonante.
   [EJERCICIO 36](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio36.py).
  
  # **EJERCICIO 37** Nombra esa forma. 
Escriba un programa que determine el nombre de una forma a partir de su número de lados. Leer el número de lados del usuario y luego informa el nombre apropiado como parte de Un mensaje significativo. Su programa debe admitir formas con 3 hasta (e incluyendo) 10 lados. Si se ingresa un número de lados fuera de este rango entonces su programa debería mostrar un mensaje de error apropiado.
   [EJERCICIO 37](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio37.py).
  
  # **EJERCICIO 38** Nombre del mes a número de días.
La duración de un mes varía de 28 a 31 días. En este ejercicio crearás Un programa que lee el nombre de un mes del usuario como una cadena. Entonces tu El programa debe mostrar la cantidad de días en ese mes. Mostrar "28 o 29 días" para febrero para que se aborden los años bisiestos.
   [EJERCICIO 38](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio38.py).
  
  # **EJERCICIO 39** Niveles de sonido.
La siguiente tabla enumera el nivel de sonido en decibelios para varios ruidos comunes.

| NOISE| DECIBEL LEBEL (dB)|
| ----- | ---- |
| Jackhammer | 130|
| as lawnmover|106| 
| Alarm clock| 70 |
| Quiet room | 40 |

Escriba un programa que lea un nivel de sonido en decibelios del usuario. Si el usuario ingresa un nivel de decibelios que coincide con uno de los ruidos en la tabla y luego su programa debería mostrar un mensaje que contenga solo ese ruido. Si el usuario ingresa un número de decibelios entre los ruidos enumerados, entonces su programa debería mostrar un mensaje indicando qué ruidos está entre el nivel.
   [EJERCICIO 39](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio39.py).
  
  # **EJERCICIO 40** Nombra ese triángulo. 
Un triángulo se puede clasificar en función de la longitud de sus lados como isósceles equiláteros o escaleno. Los 3 lados de un triángulo equilátero tienen la misma longitud. Un isósceles el triángulo tiene dos lados que tienen la misma longitud y un tercer lado que es diferente longitud. Si todos los lados tienen diferentes longitudes, entonces el triángulo es escaleno. Escriba un programa que lea las longitudes de 3 lados de un triángulo del usuario. Muestra un mensaje que indica el tipo de triángulo.
   [EJERCICIO 40](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio40.py).
  
  # **EJERCICIO 41** Nota a la frecuencia.
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
  
  # **EJERCICIO 42** Frecuencia a tener en cuenta
En la pregunta anterior, convertiste del nombre de la nota a la frecuencia. En esta pregunta escribirás un programa que invierta ese proceso. Comience leyendo una frecuencia del usuario Si la frecuencia está dentro de un Hertz de un valor listado en la tabla en En la pregunta anterior, informe el nombre de la nota. De lo contrario, informe que el la frecuencia no corresponde a una nota conocida. En este ejercicio solo necesitas considere las notas enumeradas en la tabla. No hay necesidad de considerar notas de otros octavas.
   [EJERCICIO 42](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio42.py).
  
  # **EJERCICIO 43** Caras sobre el dinero.
Las personas que aparecen en los billetes en los Estados Unidos se enumeran en la siguiente Tabla. Escriba un programa que comience leyendo la denominación de un billete del usuario. Luego, su programa debe mostrar el nombre de la persona que aparece en el billete de la cantidad ingresada. Se debe mostrar un mensaje de error apropiado
si no existe tal nota. **TABLA**
   [EJERCICIO 43](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio43.py).
  
  # **EJERCICIO 44** eFcha para el nombre de vacaciones.
Canadá tiene tres feriados nacionales que caen en las mismas fechas cada año. Escriba un programa que lea un mes y un día del usuario. Si el mes y el dia coincidir con uno de los días festivos enumerados anteriormente, entonces su programa debería mostrar el nombre de vacaciones De lo contrario, su programa debe indicar que el mes ingresado y día no corresponde a un día festivo de fecha fija. **TABLA**
   [EJERCICIO 44](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio44.py).
  
  # **EJERCICIO 45** ¿De qué color es ese cuadrado?.
Escriba un programa que lea una posición del usuario. Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. Luego use modular aritmética para informar el color del cuadrado en esa fila. Por ejemplo, si el usuario ingresa a1 entonces su programa debe informar que el cuadrado es negro.
   [EJERCICIO 45](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio45.py).
  
  # **EJERCICIO 46** Temporada del mes y día.
El año se divide en cuatro estaciones: primavera, verano, otoño e invierno. Mientras que la las fechas exactas en que cambian las estaciones varían un poco de un año a otro debido a la de la manera en que se construye el calendario, utilizaremos las siguientes fechas para este ejercicio: **TABLA**
Cree un programa que lea un mes y un día del usuario. El usuario ingresará el nombre del mes como una cadena, seguido del día dentro del mes como un entero. Luego, su programa debe mostrar la temporada asociada con la fecha en que fue ingresado.
   [EJERCICIO 46](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio46.py).
  
  # **EJERCICIO 47** Fecha de nacimiento al signo astrológico.
Los horóscopos comúnmente reportados en los periódicos usan la posición del sol en el momento del nacimiento para intentar predecir el futuro. Este sistema de astrología divide el año en doce signos del zodiaco, como se describe en la tabla a continuación: **TABLA**
Escriba un programa que le pida al usuario que ingrese su mes y día de nacimiento. Luego su programa debe informar el signo del zodiaco del usuario como parte de una salida adecuada mensaje.
   [EJERCICIO 47](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio47.py).
  
  # **EJERCICIO 48** Zodiaco chino.
El zodiaco chino asigna animales a años en un ciclo de 12 años. Un ciclo de 12 años es se muestra en la tabla a continuación. El patrón se repite a partir de ahí, con 2012 siendo otro año del dragón, y 1999 siendo otro año de la liebre. **TABLA**
Escriba un programa que lea un año del usuario y muestre el animal asociado con ese año Su programa debería funcionar correctamente durante cualquier año mayor o igual a cero, no solo los que figuran en la tabla.
   [EJERCICIO 48](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio48.py).
  
  # **EJERCICIO 49** Escala Richter.
La siguiente tabla contiene rangos de magnitud de terremotos en la escala de Richter y
sus descriptores: **TABLA**
Escriba un programa que lea una magnitud del usuario y muestre la información apropiada. descriptor como parte de un mensaje significativo. Por ejemplo, si el usuario ingresa 5.5 entonces su programa debe indicar que un terremoto de magnitud 5.5 se considera terremoto moderado
   [EJERCICIO 49](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio49.py).
  
  # **EJERCICIO 50** Raíces de una función cuadrática. 
Una función cuadrática univariada tiene la forma f (x) = ax2 + bx + c, donde a, by c son constantes y a no es cero. Se pueden encontrar las raíces de una función cuadrática encontrando los valores de x que satisfacen la ecuación cuadrática ax2 + bx + c = 0. A La función cuadrática puede tener 0, 1 o 2 raíces reales. Estas raíces se pueden calcular usando la fórmula cuadrática, que se muestra a continuación:
raíz = −b ± √ b2 - 4ac / 2a 
Escriba un programa que calcule las raíces reales de una función cuadrática. Su programa debe comenzar solicitando al usuario los valores de a, byc. Entonces debería mostrar un mensaje que indica el número de raíces reales, junto con los valores de las raíces reales
   [EJERCICIO 50](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio50.py).
  
  # **EJERCICIO 51** Calificación de letras a puntos de calificación. 
En una universidad en particular, las calificaciones con letras se asignan a puntos de calificación en el siguiente manera: **TABLA** Escriba un programa que comience leyendo una calificación de letra del usuario. Entonces tu El programa debe calcular y mostrar el número equivalente de puntos de calificación. Asegurar que su programa genera un mensaje de error apropiado si el usuario ingresa un mensaje no válido grado de la letra.
   [EJERCICIO 51](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio51.py).
  
  # **EJERCICIO 52**  Puntos de calificación para la calificación de letras.
En el ejercicio anterior, creó un programa que convierte una calificación de letra en número equivalente de puntos de calificación. En este ejercicio creará un programa que invierte el proceso y convierte de un valor de punto de calificación introducido por el usuario a un grado de la letra. Asegúrese de que su programa maneje los valores de calificación que se encuentran entre Grados de letras. Estos deben redondearse al grado de letra más cercano. Su programa debe reportar A + para un promedio de calificaciones de 4.0 (o más).
   [EJERCICIO 52](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio52.py).
  
  # **EJERCICIO 53** Evaluación de empleados.
En una empresa en particular, los empleados son calificados al final de cada año. La escala de calificación comienza en 0.0, con valores más altos que indican un mejor rendimiento y resultados más grandes plantea. El valor otorgado a un empleado es 0.0, 0.4 o 0.6 o más. Valores entre 0.0 y 0.4, y entre 0.4 y 0.6 nunca se usan. El significado asociado con cada calificación se muestra en la siguiente tabla. El monto del aumento de un empleado es $ 2400.00 multiplicado por su calificación. **TABLA**
Escriba un programa que lea una calificación del usuario e indique si el rendimiento fue inaceptable, aceptable o meritorio. El monto del empleado aumento también debe ser reportado. Su programa debe mostrar un error apropiado mensaje si se ingresa una calificación no válida.
   [EJERCICIO 53](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio53.py).
  
  # **EJERCICIO 54** Longitudes de onda de luz visible. 
La longitud de onda de la luz visible varía de 380 a 750 nanómetros (nm). Mientras que la El espectro es continuo, a menudo se divide en 6 colores como se muestra a continuación: **TABLA**
Escriba un programa que lea una longitud de onda del usuario e informe su color. Monitor un mensaje de error apropiado si la longitud de onda ingresada por el usuario está fuera de espectro visible.
   [EJERCICIO 54](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio54.py).
  
  # **EJERCICIO 55** Frecuencia para nombrar.
La radiación electromagnética se puede clasificar en una de las 7 categorías según su frecuencia, como se muestra en la tabla a continuación: **TABLA** Escriba un programa que lea la frecuencia de la radiación del usuario y muestre El nombre apropiado.
   [EJERCICIO 55](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio55.py).
  
  # **EJERCICIO 56** Bill del teléfono celular.
Un plan particular de telefonía celular incluye 50 minutos de tiempo al aire y 50 mensajes de texto. por $ 15.00 al mes. Cada minuto adicional de tiempo en el aire cuesta $ 0.25, mientras que adicional los mensajes de texto cuestan $ 0.15 cada uno. Todas las facturas de teléfonos celulares incluyen un cargo adicional de $ 0.44 para respaldar los centros de llamadas al 911, y la factura completa (incluido el cargo del 911) es sujeto al 5 por ciento de impuesto a las ventas.
Escriba un programa que lea la cantidad de minutos y mensajes de texto utilizados en un mes del usuario. Muestra el cargo base, el cargo por minutos adicionales (si corresponde), cargo adicional por mensaje de texto (si corresponde), la tarifa 911, impuestos y el monto total de la factura. Solamente mostrar los cargos adicionales por minutos y mensajes de texto si el usuario incurrió en costos en Estas categorías. Asegúrese de que todos los cargos se muestren con 2 decimales.
   [EJERCICIO 56](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio56.py).
  
  # **EJERCICIO 57** ¿Es un año bisiesto?.
La mayoría de los años tienen 365 días. Sin embargo, el tiempo requerido para que la Tierra orbita alrededor del Sol
en realidad es un poco más que eso. Como resultado, se incluye un día adicional, el 29 de febrero.
en algunos años para corregir esta diferencia. Dichos años se denominan años bisiestos.
Las reglas para determinar si un año es o no bisiesto son las siguientes:

• Cualquier año que es divisible por 400 es un año bisiesto.
• De los años restantes, cualquier año divisible por 100 no es bisiesto.
• De los años restantes, cualquier año que sea divisible por 4 es un año bisiesto.
• Todos los demás años no son bisiestos.
Escriba un programa que lea un año del usuario y muestre un mensaje que indique
si es o no un año bisiesto.
   [EJERCICIO 57](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio57.py).
  
  # **EJERCICIO 58** Al día siguiente.
Escriba un programa que lea una fecha del usuario y calcule su sucesor inmediato. Por ejemplo, si el usuario ingresa valores que representan 2013-11-18, entonces su programa debería mostrar un mensaje que indique que el día inmediatamente posterior al 2013-11-18 es 2013-11-19. Si el usuario ingresa valores que representan 2013-11-30, entonces el programa debe indicar que al día siguiente es 2013-12-01. Si el usuario ingresa valores que representan 31/12/2013, entonces el programa debe indicar que el día siguiente es 01-01-2014. los la fecha se ingresará en forma numérica con tres declaraciones de entrada separadas; uno para el año, uno para el mes y otro para el día. Asegúrese de que su programa funcione correctamente para los años bisiestos.
   [EJERCICIO 58](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio58.py).
  
  # **EJERCICIO 59**  ¿Es válida una matrícula?.
Escriba un programa que comience leyendo una cadena de caracteres del usuario. Luego su programa debe mostrar un mensaje que indique si los caracteres son válidos para una placa de estilo anterior o una placa de estilo más nueva. Su programa debe mostrar un mensaje apropiado si la cadena ingresada por el usuario no es válida para Estilo de matrícula.
   [EJERCICIO 59](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio59.py).
  
  # **EJERCICIO 61**  *Promedio*.
En este ejercicio creará un programa que calcula el promedio de una colección de valores ingresados ​​por el usuario. El usuario ingresará 0 como valor centinela para indicar que no se proporcionarán más valores. Su programa debe mostrar un apropiado mensaje de error si el primer valor introducido por el usuario es 0.
   [EJERCICIO 61](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio61.py).
   
  # **EJERCICIO 62**  *Tabla de descuento*.
Un minorista en particular está teniendo un 60 por ciento de descuento en una variedad de productos descontinuados. productos El minorista desea ayudar a sus clientes a determinar el precio reducido. De la mercancía al tener una tabla de descuento impresa en el estante que muestra el precios originales y los precios posteriores a la aplicación del descuento. Escribe un programa que usa un bucle para generar esta tabla, que muestra el precio original, el monto del descuento, y el nuevo precio para compras de $ 4.95, $ 9.95, $ 14.95, $ 19.95 y $ 24.95. Asegurar que los descuentos y los nuevos precios se redondean a 2 decimales cuando se muestran. 
   [EJERCICIO 62](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio62.py).
   
  # **EJERCICIO 63**  *Tabla de conversión de temperatura*.
Escriba un programa que muestre una tabla de conversión de temperatura para grados Celsius y grados Fahrenheit. La tabla debe incluir filas para todas las temperaturas entre 0 y 100 grados centígrados que son múltiplos de 10 grados centígrados. Incluir apropiado encabezados en sus columnas. La fórmula para convertir entre grados Celsius y grados Fahrenheit se pueden encontrar en internet.
   [EJERCICIO 63](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio63.py).
   
  # **EJERCICIO 64**  *No más centavos*.
Escriba un programa que lea los precios del usuario hasta que se ingrese una línea en blanco. Muestra el costo total de todos los artículos ingresados en una línea, seguido del monto debido si el cliente paga con efectivo en una segunda línea. El monto adeudado por un efectivo
el pago debe redondearse al níquel más cercano. Una forma de calcular el efectivo el monto del pago comenzará determinando cuántos centavos serían necesarios para pagar el total Luego calcule el resto cuando este número de centavos se divide por 5. Finalmente, ajuste el total hacia abajo si el resto es inferior a 2.5. De lo contrario, ajuste el total.
   [EJERCICIO 64](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio64.py).
    
  # **EJERCICIO 65**  *Calcular el perímetro de un polígono*.
Escribe un programa que calcule el perímetro de un polígono. Comience leyendo los valores x e y para el primer punto en el perímetro del polígono del usuario. Luego, continúe leyendo pares de valores x e y hasta que el usuario ingrese una línea en blanco para coordenada x.
   [EJERCICIO 65](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio65.py).
  
  # **EJERCICIO 66**  *Calcular promedio de calificaciones*.
  
El ejercicio 51 incluyó una tabla que muestra la conversión de calificaciones de letras a calificaciones puntos en una institución académica particular. En este ejercicio calcularás el promedio de calificaciones de un número arbitrario de calificaciones de letras ingresadas por el usuario. los el usuario ingresará una línea en blanco para indicar que se han proporcionado todas las calificaciones. por ejemplo, si el usuario ingresa A, seguido de C +, seguido de B, seguido de un espacio en blanco línea, entonces su programa debe reportar un promedio de calificaciones de 3.1. Puede encontrar útil su solución para el ejercicio 51 al completar este ejercicio. Su programa no necesita hacer ninguna comprobación de errores. Puede suponer que cada valor ingresado por el usuario siempre será una calificación de letra válida o una línea en blanco.
   [EJERCICIO 66](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio66.py).
  
  # **EJERCICIO 67**  *Precio de admisión*.
Cree un programa que comience leyendo las edades de todos los invitados en un grupo del usuario, con una edad ingresada en cada línea. El usuario ingresará una línea en blanco para indica que no hay más invitados en el grupo. Entonces su programa debería mostrar el costo de admisión para el grupo con un mensaje apropiado. El costo debe ser se muestra con dos decimales.
   [EJERCICIO 67](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio67.py).
  
  # **EJERCICIO 68**  *Bits de paridad*.
Escriba un programa que calcule el bit de paridad para grupos de 8 bits ingresados por usuario usando paridad par. Su programa debe leer cadenas que contengan 8 bits hasta que el usuario ingresa una línea en blanco. Después de que el usuario ingrese cada cadena, su programa debería mostrar un mensaje claro que indica si el bit de paridad debe ser 0 o 1. Pantalla un mensaje de error apropiado si el usuario ingresa algo diferente a 8 bits.
   [EJERCICIO 68](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio68.py).
  
 
  # **EJERCICIO 69**  *Aproximado π*.
Escriba un programa que muestre 15 aproximaciones de π. La primera aproximación debe utilizar solo el primer término de la serie infinita. Cada aproximación adicional mostrada por su programa debe incluir un término más en la serie, haciendo es una mejor aproximación de π que cualquiera de las aproximaciones mostradas anteriormente.
   [EJERCICIO 69](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio69.py).
  
  # **EJERCICIO 70**  *Cifrado César*.
Escriba un programa que implemente un cifrado César. Permitir al usuario suministrar el mensaje y la cantidad de turno, y luego mostrar el mensaje desplazado. Asegurarse de que su programa codifica letras mayúsculas y minúsculas. Su programa debe también admite valores de desplazamiento negativos para que pueda usarse tanto para codificar mensajes como para decodificar mensajes.
   [EJERCICIO 70](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio70.py).
 
  # **EJERCICIO 71**  *Raíz cuadrada*.
Escriba un programa que implemente el método de Newton para calcular y mostrar el cuadradoraíz de un número ingresado por el usuario. El algoritmo para el método de Newton sigue: Leer x del usuario Inicializar adivinar a x / 2 Mientras que adivinar no es lo suficientemente bueno Actualizar conjetura para que sea el promedio de conjetura y x / conjetura Cuando se completa este algoritmo, supongo que contiene una aproximación del cuadrado raíz. La calidad de la aproximación depende de cómo se defina "lo suficientemente bueno". En la solución del autor, la conjetura se consideraba suficientemente buena cuando el valor absoluto de la diferencia entre adivinar ∗ adivinar y x fue menor o igual a 10^12.
   [EJERCICIO 71](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio71.py).
   
  # **EJERCICIO 72**  *¿Es una cuerda un palíndromo?*.
Una cadena es un palíndromo si es idéntica hacia adelante y hacia atrás. Por ejemplo "anna", "Civic", "level" y "hannah" son ejemplos de palabras palindrómicas. Escribe un programa que lee una cadena del usuario y usa un bucle para determinar si es o no un palíndromo. Muestra el resultado, incluido un mensaje de salida significativo.
   [EJERCICIO 72](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio72.py).
   
  # **EJERCICIO 73**  *Palíndromos de palabras múltiples*.
   [EJERCICIO 73](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio73.py).
Existen numerosas frases que son palíndromos cuando se ignora el espacio. Ejemplos incluyen "ir perro", "huir a mí elfo remoto" y "algunos hombres interpretan nueve notas", Entre muchos otros. Extienda su solución al Ejercicio 72 para que ignore el espaciado mientras determina si una cuerda es o no un palíndromo. Para un desafío adicional, extienda su solución para que también ignore los signos de puntuación y trate las mayúsculas y letras minúsculas como equivalentes.
  # **EJERCICIO 74**  *Tabla de multiplicación*.
  
En este ejercicio creará un programa que muestra una tabla de multiplicación que
muestra los productos de todas las combinaciones de enteros desde 1 por 1 hasta
10 veces 10. Su tabla de multiplicar debe incluir una fila de etiquetas en la parte superior
contiene los números del 1 al 10. También debe incluir etiquetas a la izquierda
lado que consiste en los números del 1 al 10.
  
   [EJERCICIO 74](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio74.py).
   
  # **EJERCICIO 75**  *Máximo común divisor*.
  Escriba un programa que lea dos enteros positivos del usuario y use este algoritmo para determinar e informar su mayor divisor común.
   [EJERCICIO 75](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio75.py).
  
  # **EJERCICIO 76**  *Factores primos*.
Escriba un programa que lea un número entero del usuario. Si el valor ingresado por el el usuario tiene menos de 2, entonces su programa debería mostrar un mensaje de error apropiado. De lo contrario, su programa debería mostrar los números primos que se pueden multiplicar juntos para calcular "n", con un factor que aparece en cada línea.
   [EJERCICIO 76](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio76.py).
   
  # **EJERCICIO 77**  *Binario a decimal*.
Escriba un programa que convierta un número binario (base 2) a decimal (base 10). Tu El programa debe comenzar leyendo el número binario del usuario como una cadena. Luego debe calcular el número decimal equivalente procesando cada dígito en el número binario. Finalmente, su programa debe mostrar el número decimal equivalente con un mensaje apropiado
   [EJERCICIO 77](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio77.py).

  # **EJERCICIO 78**  *Decimal a binario*.
  Escriba un programa que convierta un número decimal (base 10) a binario (base 2). Leer el número decimal del usuario como un entero y luego use el algoritmo de división que se muestra a continuación para realizar la conversión. Cuando se completa el algoritmo, el resultado contiene la representación binaria del número. Mostrar el resultado, junto con un mensaje.
   [EJERCICIO 78](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio78.py).
   
  # **EJERCICIO 79**  *Número entero máximo*.
Crear un programa que comienza seleccionando un número entero aleatorio entre 1 y 100. Guarde esto entero como el número máximo encontrado hasta ahora. Después de que el entero inicial ha sido seleccionado, generar 99 enteros aleatorios adicionales entre 1 y 100. Verifique cada
entero, ya que se genera para ver si es mayor que el número máximo encontrado hasta aquí.
   [EJERCICIO 79](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio79.py).


  # **EJERCICIO 80**  *Coin Flip Simulation*.
Cree un programa que use el generador de números aleatorios de Python para simular el volteo una moneda varias veces La moneda simulada debe ser justa, lo que significa que la probabilidad de caras es igual a la probabilidad de colas. Tu programa debe voltearse simulado monedas hasta que ocurran 3 caras consecutivas de 3 colas consecutivas. Mostrar una H cada cada vez que el resultado es cara y una T cada vez que el resultado es cruz, con todos los resultados mostrados en la misma línea. Luego muestre la cantidad de vueltas necesarias para alcanzar 3 lanzamientos consecutivos con el mismo resultado.
   [EJERCICIO 80](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio80.py).


  # **EJERCICIO 81**  *Calcule la hipotenusa*.
Escribe una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros Devuelve la hipotenusa del triángulo, calculada usando Pitágoras teorema, como resultado de la función. Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, usa su función para calcular el longitud de la hipotenusa, y muestra el resultado.  
   [EJERCICIO 81](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio81.py).

  # **EJERCICIO 82**  *Tarifa taxi*.
Escriba una función que tome la distancia recorrida (en kilómetros) como su único parámetro y devuelve la tarifa total como su único resultado. Escribe un programa principal que demuestra la función.
   [EJERCICIO 82](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio82.py).




  # **EJERCICIO 83** *Calculadora de envío*.
Un minorista en línea ofrece envío expreso para muchos de sus artículos a una tarifa de $ 10.95 para el primer artículo y $ 2.95 por cada artículo posterior. Escribe una función que tome el número de elementos en el pedido como único parámetro. Devuelva los gastos de envío de
el orden como resultado de la función. Incluya un programa principal que lea el número de artículos comprados al usuario y muestra los gastos de envío.
   [EJERCICIO 83](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio83.py).




  # **EJERCICIO 84**  *Mediana de tres valores*.
Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. Incluya un programa principal que lea tres valores de el usuario y muestra su mediana.
   [EJERCICIO 84](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio84.py).




  # **EJERCICIO 85**  *Convierta un número entero en su número ordinal*.
En este ejercicio escribirás una función que toma un número entero como su único parámetro y devuelve un cadena que contiene el número ordinal inglés apropiado como único resultado.
   [EJERCICIO 85](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio79.py).




  # **EJERCICIO 86**  *Los doce días de navidad*.
Su tarea es escribir un programa que muestre la letra completa de The Twelve Días de navidad. Escribe una función que tome el número del verso como su único parámetro y muestra el verso especificado de la canción. Luego llame a esa función 12 veces con enteros que aumentan de 1 a 12.
   [EJERCICIO 86](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio86.py).




  # **EJERCICIO 87**  *Centrar una cadena en la terminal*.
Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de el terminal en caracteres como su segundo parámetro. Su función debería devolver un nuevo cadena que consta de la cadena original y el número correcto de espacios iniciales para que la cadena original aparezca centrada dentro del ancho proporcionado cuando está impreso.
   [EJERCICIO 87](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio87.py).




  # **EJERCICIO 88**  *¿Es un triángulo válido?*.
Escribe una función que determine si tres longitudes pueden o no formar un triángulo. La función tomará 3 parámetros y devolverá un resultado booleano. Además, escribe un programa que lee 3 longitudes del usuario y demuestra el comportamiento de este función.
   [EJERCICIO 88](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio88.py).




  # **EJERCICIO 89**  *Capitalizarlo*.
En este ejercicio, escribirás una función que capitaliza Los caracteres apropiados en una cadena. Una "i" minúscula debe ser reemplazada por una "I" mayúscula si está precedido y seguido por un espacio.
   [EJERCICIO 89](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio89.py).




  # **EJERCICIO 90**  *¿Una cadena representa un número entero?*.
Escriba un programa principal que lea una cadena del usuario e informe si o No representa un número entero. Asegúrese de que el programa principal no se ejecutará si el archivo que contiene su solución se importa a otro programa.
   [EJERCICIO 90](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio90.py).




  # **EJERCICIO 91**  *Precedencia del operador*.
Escriba una función llamada precedencia que devuelva un número entero que represente la precedencia de un operador matemático. Una cadena que contiene el operador se pasará a la función como único parámetro
   [EJERCICIO 91](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio91.py).




  # **EJERCICIO 92**  *¿Es un número primo?*.
Escriba una función que determine si su parámetro es primo o no, devolviendo Verdadero si es así, y falso de lo contrario. Escribe un programa principal que lea un número entero del usuario y muestra un mensaje que indica si es primo o no. Asegurar que el programa principal no se ejecutará si se importa el archivo que contiene su solución en otro programa.
   [EJERCICIO 92](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio92.py).




  # **EJERCICIO 93**  *Próximo siguiente*.
En este ejercicio creará una función llamada nextPrime que encuentra y devuelve el primer número primo más grande que un número entero, n. El valor de n se pasará a la función como su único parámetro. Incluya un programa principal que lea un número entero de el usuario y muestra el primer número primo mayor que el valor ingresado.
   [EJERCICIO 93](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio93.py).




  # **EJERCICIO 94**  *Contraseña Aleatoria*.
Escribe una función que genere una contraseña aleatoria. La contraseña debe tener un longitud aleatoria de entre 7 y 10 caracteres. Cada personaje debe ser al azar seleccionado de las posiciones 33 a 126 en la tabla ASCII. 
   [EJERCICIO 94](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio94.py).




  # **EJERCICIO 95**  *Número entero máximo*.
   [EJERCICIO 95](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio95.py).




  # **EJERCICIO 96**  *Número entero máximo*.
   [EJERCICIO 96](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio96.py).




  # **EJERCICIO 97**  *Número entero máximo*.
   [EJERCICIO 97](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio97.py).




  # **EJERCICIO 98**  *Número entero máximo*.
   [EJERCICIO 98](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio98.py).




  # **EJERCICIO 99**  *Número entero máximo*.
   [EJERCICIO 99](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio99.py).




  # **EJERCICIO 100**  *Número entero máximo*.
   [EJERCICIO 100](https://github.com/Lusarom/progAvanzada/blob/master/ejercicio100.py).













  
 
































