#Exercise 57: Is it a Leap Year?

while True:
    
  year = int(input('Enter the year:\t'))
  
  yes = '%d is a leap year.' % (year)
  no = '%d is not a leap year.' % (year)
  
  if year % 400 == 0:
    print(yes)
  
  elif year % 100 == 0:
    print(no)
  
  elif year % 4 == 0:
    print(yes)
  
  else:
    print(no)
  
  print()
