Dias=float(input('Inserta Dias'))
Horas=float(input('Inserta Horas'))
Minutos=float(input('Inserta Minutos'))
Segundos=float(input('Inserta Segundos'))

Dias=Dias*86400
Hora=Horas*3600
Minuto=Minutos*60
Segundos=Segundos

Total=Dias+Horas+Minutos+Segundos
print('Total de segundos:',Total)