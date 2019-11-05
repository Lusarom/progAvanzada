#Exercise 53: Assessing Employees

value = float(input('Enter the rating:'))

performance = ''

if value == 0.0:
	performance = 'Unacceptable'
elif value == 0.4:
	performance = 'Acceptable'
elif value >= 0.6:
        performance = 'Meritorius'

if performance != '':
	print('That wasnt a valid rating')
else :
	print('Invalid value (The value is 0.0, 0.4 or higher tahn 0.6)')
if value== 0.0 or value== 0.4 or value >=0.6:
 amount = 2400 * value
 
 print('The total increanse is:', amount)

