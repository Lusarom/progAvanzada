
import math

s1=int(input('Ingresa primer distancia triangulo:'))
s2=int(input('Ingresa segunda distancia triangulo:'))
s3=int(input('Ingresala tercer distancia triangulo:'))

s=(s1+s2+s3)/2

a=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print('El triangulo tiene por area: ',a)
