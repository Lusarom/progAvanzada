#Exercise 50: Roots of a Quadratic Function

import math

times = int(input('Enter the number of times:\n'))

for count in range(times):
  while True:  
    try:
      a = int(input('Enter the a value:\n'))
      b = int(input('Enter the b value:\n'))
      c = int(input('Enter the c value:\n'))
      discriminant = b ** 2 - 4 * a * c
      if discriminant < 0:
        print('Number of roots: 0\n')
      elif discriminant == 0:
        root = (-b + math.sqrt(discriminant)) / (2 * a)
        print('Number of roots: 1\nRoot: %f\n' % (root))
      elif discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print('Number of roots: 2\nRoots: %f, %f\n' % (root1, root2))
      break
    except ValueError:
      print('Invalid input.\n')

blah = input('Press ENTER to quit.')
