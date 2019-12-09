
  

from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

def randomPassword():
    randomLength = randint(SHORTEST, LONGEST)
    result = ''
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result += randomChar
    return result 

def main(): 
    print("Your random password is: ", randomPassword())

if __name__ == "__name__":
    main()