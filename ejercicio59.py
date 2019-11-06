#Exercise 59: Is a License Plate Valid?

string = input('Enter the string:')

upper = False
alpha = False
old = False
new = False

if string[0].isupper() == True and string[1].isupper() == True and string[2].isupper() == True:
  upper = True
  

if string[0].isalpha() == True and string[1].isalpha() == True and string[2].isalpha() == True and string[3].isdigit() == True and string[4].isdigit() == True and string[5].isdigit() == True and upper == True:
  old = True
  
  print('That is an old license plate')


if string[0].isdigit() == True and string[1].isdigit() == True and string[2].isdigit() == True and string[3].isdigit() == True:
  digit = True

if string[4].isalpha() == True and string[5].isalpha() == True and string[6].isalpha() == True:
  alpha = True

if string[4].isupper() == True and string[5].isupper() == True and string[6].isupper() == True:
  upper2 = True

if alpha == True and upper2 == True and digit == True:
  new = True
  
  print('That is a new license plate')

if old == False and new == False:
    
  print('Thats no license plate')
