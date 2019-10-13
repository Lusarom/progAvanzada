#Exercise 35: Dog Years

#It is commonly said that one human year is equivalent to 7 dog years. However this
#simple conversion fails to recognize that dogs reach adulthood in approximately two
#years. As a result, some people believe that it is better to count each of the first two
#human years as 10.5 dog years, and then count each additional human year as 4 dog years.


humage = int(input('Input a dog age in human years'))

if humage < 0:
	print('Age must be positive number')
	
elif humage <= 2:
	doage = humage * 10.5
else:
	doage = 21 + (humage - 2)*4

print('The dog age is', doage)
