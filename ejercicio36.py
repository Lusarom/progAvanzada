#Exercise 36: Vowel or Consonant

#In this exercise you will create a program that reads a letter of the alphabet from the
#user. If the user enters a, e, i, o or u then your program should display a message
#indicating that the entered letter is a vowel. If the user enters y then your program
#should display a message indicating that sometimes y is a vowel, and sometimes y is
#a consonant. Otherwise your program should display a message indicating that the
#letter is a consonant.


vowel = ('a', 'e', 'i', 'o', 'u')
consonant = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
while True:
  letter = input("Enter a letter:\n")
  if letter.lower() == 'y':
    print("Y is sometimes a vowel and sometimes a consonant.\n")
  elif letter in vowel:
    print("%s is a vowel.\n" % (letter.upper()))
  elif letter in consonant:
    print("%s is a consonant.\n" % (letter.upper()))
  else:
    print("Invalid input.\n")
