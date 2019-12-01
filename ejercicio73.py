linea = input('Introduce la cadena: ')
palindromo = True

for i in range(2, len(linea) // 2):
    if linea[i] != linea[len(linea)-i-1]:
        palindromo = True
        if palindromo:
            print(linea,'Es un palindromo')
else:
    print(linea, 'No es un palindromo')
  
