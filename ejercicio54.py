VIOLET = 380
BLUE = 450
GREEN = 495
YELLOW = 570
ORANGE = 590
RED = 620
TOP = 750

WAVELENGTH = 'The color is %s.'

times = int(input('How many times do you wish to run this program?:\n'))

for count in range(1, times + 1):
  while True:
    print('\nTime %d\n' % (count))
  
    wavelength = int(input('Enter the wavelength in nanometers. Choose 380 - 750:\n'))
    
    if VIOLET <= wavelength < BLUE:
      print(WAVELENGTH % ('Violet'))
      break
    
    elif BLUE <= wavelength < GREEN:
      print(WAVELENGTH % ('Blue'))
      break
    
    elif GREEN <= wavelength < YELLOW:
      print(WAVELENGTH % ('Green'))
      break
    
    elif YELLOW <= wavelength < ORANGE:
      print(WAVELENGTH % ('Yellow'))
      break
    
    elif ORANGE <= wavelength < RED:
      print(WAVELENGTH % ('Orange'))
      break
    
    elif RED <= wavelength < TOP:
      print(WAVELENGTH % ('Red'))
      break
    
    else:
      print('Choose 380 - 750.\n')
