from math import radians, cos, sin, asin, sqrt

print('Introduce Latitud y Longitud:')
Latit1= float(input('Latitud 1:'))
Long1= float(input('Longitud 1:'))
Latit2= float(input(' Latitud 2:'))

Long2= float(input('Longitud 2:'))
 
Long1= radians(Long1)
Long2= radians(Long2)
Latit1= radians(Latit1)
Latit2= radians(Latit2)
 
DistLong= Long2 - Long1 
DistLatit= Latit2 - Latit1

a= sin(DistLatit/2)**2 + cos(Latit1) * cos(Latit2) * sin(DistLong/2)**2
c= 2 * asin(sqrt(a)) 
r= 6371 
 

print('Distancia es: %.2f.' %(c*r),'kilometros')


