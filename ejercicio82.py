#En la ciudad de mexico la tarifa de taxi-uber consiste en un precio base de $44.00 + $12.00 por cada kilometro recorrido. Escriba una funcion que tome la distancia viajada en (km) el cual deve ser el unico argumento y regrese la tarifa total como resultado. Escriba un programa principal que demuestre la funcion
def tarifa(distancia):
    total = 44.00 + distancia*12.00
    return total
dist = float(input('Inserte la distancia manejada (km):'))
cuota = tarifa(dist)
print('El costo del viaje es: ' ,cuota)