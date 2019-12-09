#Amazon provee envio express para muchos de sus productos a un coste de: $195.00 por el primer producto y de $29.50 para cada producto subsecuente. Escriba una funcion que tome el numero de porductos y los ordene como su unico argumento, regrese el costo de envio total como el resultado de la funcion. Incluya un programa principal que lea el numero de productos comprados por el usuario y que desplegue el costo total de envio.

def costo(articulos):
    total = 195.00 + (articulos-1)*29.50
    if d == 1:
        print('195.00: ')
    elif d > 1:
        print('El costo del envio es: ' , total)
    return total
    
d = float(input('Inserte numero de articulos:'))
final = costo(d)

