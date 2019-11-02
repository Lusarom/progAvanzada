nombre = input('Inserta el nombre de la nota: ')


nota = nombre[0].upper()

octave = int(nombre[1])

frequencia = -1

if nota == "C":
	frequencia = 261.63
elif nota == "D":
	frequencia = 293.66
elif nota == "E":
	frequencia = 329.63
elif nota == "F":
	frequencia = 349.23
elif nota == "G":
	frequencia = 392.00
elif nota == "A":
	frequencia = 440.00
elif nota == "B":
	frequencia = 493.88
	
frequencia /= 2 ** (4 - octave) 
	
print('La nota es:' ,nota, 'frequencia es ',(frequencia), 'Hz')
42
