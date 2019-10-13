#Exercise 37: Name that Shape

#Write a program that determines the name of a shape from its number of sides. Read
#the number of sides from the user and then report the appropriate name as part of
#a meaningful message. Your program should support shapes with anywhere from 3
#up to (and including) 10 sides. If a number of sides outside of this range is entered
#then your program should display an appropriate error message.


while True:
  s = int(input('Enter number off 3 - 10:\n'))
  a = 'Polygon with %d sides  a%s.\n'
  if s == 3:
    print(a % (3, ' Triangle'))
  elif s == 4:
    print(a % (4, ' Quadrilateral'))
  elif s == 5:
    print(a % (5, ' Pentagon'))
  elif s == 6:
    print(a % (6, ' Hexagon'))
  elif s == 7:
    print(a % (7, ' Heptagon and a septagon'))
  elif s == 8:
    print(a % (8, ' Octagon'))
  elif s == 9:
    print(a % (9, ' Nonagon'))
  elif s == 10:
    print(a % (10, ' Decagon'))
  else:
    print('Error number.\n')
