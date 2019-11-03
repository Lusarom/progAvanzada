#Exercise 44: Date to Holiday Name

month = input('Month:')
day = int(input('Day:'))

holiday = ''

if month == 'January' and day == 1:
 print('New years day')
elif month == 'July' and day == 1:
 print('Canada day')
elif month == 'December' and day == 25: 
 print('Christmas Day')

else:
 print('Month and Day wrong')
