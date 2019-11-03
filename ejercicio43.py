#Exercise 43: Faces on Money

denom = int(input('Ingresa denominacion de billete: $'))

nom = ""

if denom == 1:
	nom = 'George Washington'
if denom == 2:
	nom = 'Thomas Jefferson'
if denom == 5:
	nom = 'Abraham Lincoln'
if denom == 10:
	nom = 'Alexander Hamilton'
if denom == 20:
	nom = 'Andrew Jackson'
if denom == 50:
	nom = 'Ulysses S. Grant'
if denom == 100:
	nom = 'Benjamin Franklin'
	
if nom == '':
	print('Cantidad erronea, ingresa nueva cantidad.')
else:
	print('El personaje en la denomicacion es:',(nom))
