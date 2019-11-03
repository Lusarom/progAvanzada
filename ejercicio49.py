#Exercise 49: Richter Scale

magnitude = input('Enter the magnitude of the earthquake')
magnitude = float(magnitude)

kind = 'none'


if  magnitude < 2:
    kind = 'micro'
elif magnitude >= 2 and magnitude < 3:
    kind = 'very minor'
elif magnitude >= 3 and magnitude < 4:
    kind = 'minor'
elif magnitude >= 4 and magnitude < 5:
    kind = 'light'

elif magnitude >= 5 and magnitude < 6:
    kind = 'moderate'
elif magnitude >= 6 and magnitude < 7:
    kind = 'strong'
elif magnitude >= 7 and magnitude < 8:
    kind = 'major'
elif magnitude >= 8 and magnitude < 10:
    kind = 'great'
elif magnitude >= 10:
    kind = 'meteoric'
    
print()
print('Earthquake Type:', kind)
