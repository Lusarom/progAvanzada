#Exercise 45:What Color is that Square?

while True:  
  oddSet = ['a', 'c', 'e', 'g']
  evenSet = ['b', 'd', 'f', 'h']
  oddNumbers = [1, 3, 5, 7]
  evenNumbers = [2, 4, 6, 8]
  letter = input('Enter the letter:\n')
  while True:  
    try:
      number = int(input('Enter the number:\n'))
      break
    except ValueError:
      print('Number has to be an integer.\n')
  if letter.lower() in oddSet and number in oddNumbers:
    print('The square is black.\n')
  elif letter.lower() in evenSet and number in oddNumbers:
    print('The square is white.\n')
  elif letter.lower() in evenSet and number in evenNumbers:
    print('The square is black.\n')
  elif letter.lower() in oddSet and number in evenNumbers:
    print('The square is white.\n')
  else:
    print('Letter has to be a letter.\n')
