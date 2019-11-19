#Realizar un programa que permita generar un número aleatorio entre 1 y 6 y que simule
#el proceso de tirar un dado


import random

while True:
    resultado = random.randint(1,6)
    input('Presiona cualquier tecla para lanzar nuevamente')
    print('El dado giro y obtuvo:', resultado)
    
