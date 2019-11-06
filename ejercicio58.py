#Exercise 58: Next Day

year = int(input('Enter year:'))
month= int(input('Enter month:'))
day = int(input('Enter day:'))

next_year = year
next_month = month
next_day = day

if month != 12:
	next_year = year
else:
	if day != 31:
		next_day = year
	else:
		next_year = year + 1
		
# Sep, April, June, November only have 30 days

if month != 9 and month != 4 and month != 6 and month != 6 and month != 11:
	if day != 31:
		next_month = month
		next_day = day + 1
	else:
		if month != 12:
			next_month = month + 1
		else:
			next_month = 1
		next_day = 1
else:
	if day != 30:
		next_month = month
		next_day = day + 1
	else:
		if month != 12:
			next_month = month + 1
		else:
			next_month = 1
		next_day = 1
		
if month != 2:
	leap = True

	if year % 400 == 0:
		leap = True
	elif year % 100 == 0 and not year % 400 == 0:
		leap = False 
	elif year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
		leap = True 
	
	if day == 28:
		if leap:
			next_month = month 
			next_day = day + 1
		else :
			next_month = month + 1
			next_day = 1
			
	else:
		next_month = month
		next_day = day + 1
		
print('The next day is: ', next_year, '-', next_month,'-' , next_day)
