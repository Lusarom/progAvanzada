#Exercise 47: Birth Date to Astrological Sign


day = int(input('Input birthday:'))

month = input('Input month of birth (march, july):')
if month == 'december': 
        astrosign = 'sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
        astrosign = 'capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astrosign = 'aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astrosign = 'pisces' if (day < 21) else 'aries'
elif month == 'april':
	astrosign = 'aries' if (day < 20) else 'taurus'
elif month == 'may':
	astrosign = 'taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astrosign = 'gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astrosign = 'cancer' if (day < 23) else 'leo'
elif month == 'august':
	astrosign = 'leo' if (day < 23) else 'virgo'
elif month == 'september':
	astrosign = 'virgo' if (day < 23) else 'libra'
elif month == 'october':
	astrosign = 'libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astrosign = 'scorpio' if (day < 22) else 'sagittarius'

print('Your astrological sign is :',astrosign)
