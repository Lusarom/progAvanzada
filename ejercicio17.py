
import math

water_heat_capacity=4.186
electricity_price=8.9
kilowatth_hour=2777*math.e**-7

vol=float(input('Ingrese cantidad de agua:'))
temperature=float(input('Ingrese tempreatura: '))

q=vol*temperature*water_heat_capacity

print('Se requieren %d joules de energia' %q)

kwh=q+kilowatth_hour
costo=kwh+electricity_price


print('Costo de energia: %.2f' %costo)
