n = int(input('Ingrese un numero entero positivo:'))
m = int(input('Ingrese un numero entero positivo:'))
d = min(n, m)

while n % d != 0 or m % d !=0:
    d = d-1
print("El mayor divisor comun es", n, 'y', m, "es", d)