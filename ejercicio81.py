#funciones
#Las funciones ayudan al programador a partir un problema en piezas que pueden ser reusadas. Tambien ayudan al programador a concentrarse y solo una parte del problema como resultado el escribir funciones es una parte importante del desarrollo de programas grandes. Para definir una funcion se utiliza reservada "def" seguido del nombre de la funcion y sus argumentos separados por comas, el cuerpo de la funcion lleva una identacion y generalmente una funcion devuelve un resultado usando la palabra reservada"return"

# def nombre_de_la_funcion(argumento1,argumento2,...)
#cuerpo_de_la_funcion.
#return resultado
#ejercicio81.
#escribir una funcion que tome la longitud de los dos lados mas cortos de un triangulo rectangulo como argumentos. La funcion deve de regresar la hipotenusa del triangulo calculado utilizando el teorema de pitagoras como el resultado de la funcion.
#Incluya un programa principal que lea las longitudes de los lados mas cortos de un triangulo rectangulo insertados por el usuario, usando la funcion para calcular la longitud de la hipotenusa y que tambien se despliegue el resultado.

def calcular_hipotenusa(lado1, lado2):
    hipotenusa = (lado1**2 + lado2**2)**(0.5)
    return hipotenusa
L1 = float(input('Inserte el valor del lado 1: '))
L2 = float(input('Inserte el valor del lado 2: '))
hip = calcular_hipotenusa(L1, L2)
print('La hipotenusa es: ',hip)