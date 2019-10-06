inchft = 12
cmin = 2.54

altura = float(input('Inserta tu altura:'))

feet = int(input('Numero en ft:'))
inch = int(input('Numero en inch:'))

cm = (feet * inchft + inch) * cmin

print('Tu altura en centimetros es:', cm)



