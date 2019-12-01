def Averages():
  my_list = []
  Average  = 0
  count = 0
  Total = 0
  import sys
  print("Give me a number.")
  NumberGiven = int(sys.stdin.readline())
  while NumberGiven != 0:
      count +=1
      my_list.append(NumberGiven)
      print ("Give me another number please:")
      NumberGiven = int(sys.stdin.readline())
      #When done, the components in the list should be added in a new value
      Total = sum(my_list)
      Average = (Total/count)
  else:
      print("The average number of the numbers entered is", Average)
      #NumberGiven = input("Please give me a number")

Averages()
    
