import math
pi=3.1416

s=int(input('Ingrese longitud:'))
n=int(input('Ingrese numero de lados:'))

area=(n*(s**2))/(4*(math.tan(pi/n)))

print('El polígono tiene por area: ',area)
