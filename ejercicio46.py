


month=str(input('Inserta el mes:'))
day=int(input('Inserta el dia:'))

if month =='Enero' or month=='Febrero':
    season='Invierno'
elif month=='Marzo':
    if day<20:
        season='Invierno'
else:
    season='Primavera'

if month == 'Abril' or month == 'Mayo':
    season='Primavera'
elif month=='Junio':
    if day<21:
        season='Primavera'
else:
    season='Verano'
if month=='Julio' or month=='Agosto':
            season="Verano"
elif month=='Septiembre':
            if day<22:
                season='Verano'
else:
    season='Otoño'
if month=='Octubre' or month=='Noviembre':
                season='Otoño'
elif month=='Diciembre':
                if day<21:
                    season='Otoño'
                
else:
    season='Inverno'
                
print(month, day, 'la estacion es', season)
