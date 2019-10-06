toonie=200
loonie=100
quarter=25
dime=10
nickel=5

centavos=int(input('Ingrese los centavos: '))

print('', centavos // toonie,  'toonies')
centavos=centavos%toonie

print('', centavos // loonie,  'loonies')
centavos=centavos%loonie

print('', centavos // quarter,  'quarters')
centavos=centavos%toonie

print('', centavos // dime,  'dimes')
centavos=centavos%dime

print('', centavos // nickel,  'nickels')
centavos=centavos%nickel
