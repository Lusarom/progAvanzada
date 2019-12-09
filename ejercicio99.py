
from ejercicio98 import *

def dec2n(num, new_base):
    result = ' '
    q = num

    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    while q > 0:
        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base

    return result
def n2dec(num, b):
    decimal = 0
    power = 0

    for i in range(len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])
    return decimal
def main():
    from_base = int (input('Introduce la base convertida por: '))
    from_num = input('Introduce la secuencia de digitos en esta base')

dec = n2dec(from_num, from_base)
print('esto es %d en base 10.' %dec)

to_base = int(input('Introduce la base a convertir a: '))
to_num = dec2n(dec, to_base)
print('esta es %s en base %d ' %(to_num, to_base))