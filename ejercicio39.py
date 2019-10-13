#Exercise 39: Sound Levels

#The following table lists the sound level in decibels for several common noises.

#Noise Decibel level (dB)
#Jackhammer 130
#Gas lawnmower 106
#Alarm clock 70
#Quiet room 40

#Write a program that reads a sound level in decibels from the user. If the user
#enters a decibel level that matches one of the noises in the table then your program
#should display a message containing only that noise. If the user enters a number
#of decibels between the noises listed then your program should display a message
#indicating which noises the level is between. Ensure that your program also generates
#reasonable output for a value smaller than the quietest noise in the table, and for a
#value larger than the loudest noise in the table.



decibels = float(input("Enter the number of decibels: "))
	
if decibels > 0 and decibels < 40:
    print('quieter than a quiet room.')
		
elif decibels == 40:
    print('about the same as a quiet room.')
	
elif decibels > 40 and decibels < 70:
    print('quieter than an alarm clock.')
elif decibels == 70:
    print('about the same as an alarm clock.')
		
elif decibels > 70 and decibels < 106:
    print('quieter than a lawn mower.')
	
elif decibels == 106:
    ('about the same as a lawn mower.')
	
elif decibels > 106 and decibels < 130:
    print(" quieter than a jackhammer.")
		
elif decibels == 130:
    print('about the same as a jackhammer.')
		
elif decibels > 130:
    print('way too loud.')
		
else:
    print('Please enter a correct data value.')
		
    print('Your sound level is')


