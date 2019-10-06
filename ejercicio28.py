Tair= float(input('Ingrese temperatura air:'))
viento = float(input('Ingrese velocidad viento:'))

wind_chill_index = 13.12 + (0.6215*Tair) - (11.37*(viento**0.16)) + (0.3965*Tair*(viento**0.16))

print('wind chill index is', round(wind_chill_index))
