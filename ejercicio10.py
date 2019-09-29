import math
a=float(input('Ingresa un número:'))
b=float(input('Ingresa un número:'))

suma=a+b
print('La suma de los números ingresados es:',a, '+',b,'=',suma)
resta=b-a
print('La diferencia de los números ingresados es:',b, '-',a,'=',resta)
multiplicacion=a*b
print('El producto de los números ingresados es:',a,'*',b,'=',multiplicacion)
cociente=a/b
print('El cociente de los números ingresados es:',a,'/',b,'=',cociente)
residuo=a%b
print('El residuo del cociente de los números ingresados es:',residuo)
print('El resultado logaritmico del primer número ingresado es:',math.log(a, 10))
print('El resultado del primer número elevado al segundo número ingresado es:',pow(a, b))
