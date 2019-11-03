#Exercise 42: Frequency To Note


frecuencia = float(input('Inserta frecuencia en Hz:'))

nota = ''

if frecuencia > 261.63 - 1 and frecuencia < 261.63 + 1:
	nota = 'C'
elif frecuencia > 293.66 - 1 and frecuencia < 293.66 + 1:
	nota = 'D'
elif frecuencia > 329.63 - 1 and frecuencia < 329.63 + 1:
	nota = 'E'
elif frecuencia > 349.23 - 1 and frecuencia < 349.23 + 1:
	nota = 'F'
elif frecuencia > 392.00 - 1 and frecuencia < 392.00 + 1:
	nota = 'G'
elif frecuencia > 440.00 - 1 and frecuencia < 440.00 + 1:
	nota = 'A'
elif frecuencia > 493.88 - 1 and frecuencia < 493.88 + 1:
	nota = 'B'
if nota == '':
	print('Esta no es una nota que corresponda con la frecuencia')
else:
	print('La frecuencia es',(Nota))
