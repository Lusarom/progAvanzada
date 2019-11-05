#Exercise 55: Frequency to Name


frequency = float(input('Enter the prequency:'))

category = ''

if frequency < 3e9:
	category = 'radio waves'
elif frequency >= 3e9 and frequency < 3e12:
	category = 'microwave'
elif frequency >= 3e12 and frequency < 4.3e14:
	category = 'infrared light'
elif frequency >= 4.3e14 and frequency< 7.5e14:
	categoria = 'visible light'
elif frequency >= 7.5e14 and frequency < 3e17:
	category = 'ultraviolet light'
elif frequency >= 3e17 and frequency < 3e19:
	category = 'X-rays'
elif frequency >= 3e19:
	category = 'gamma rays'
	
if category != '':
	print('The frequency is category:',(category))
else:
	print('The frequency entered is invalid.')
