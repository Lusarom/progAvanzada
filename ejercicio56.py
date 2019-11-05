#Exercise 56: Cell Phone Bill

CHAR = '-'

CALL = 50
TEXT = 50
COST = 15.00
TOTAL = 15.00
COST_911 = 0.44
TAX_RATE = 0.05

minutes = int(input('Enter the amount of air time in minutes:\t'))

if minutes > 50:
  extraMinutes = minutes - 50
  extraMinutesCost = extraMinutes * 0.25
  TOTAL += extraMinutesCost
  
texts = int(input('Enter the number of texts:\t'))

if texts > 50:
  extraTexts = texts - 50
  extraTextsCost = extraTexts * 0.15
  TOTAL += extraTextsCost

TOTAL += COST_911

TAX = TAX_RATE * TOTAL
TOTAL += TAX

print(CHAR * 50)

print('Base Charge: $%.2f' % (COST))

try:
  print('Additional Minutes Charge: $%.2f' % (extraMinutesCost))

except NameError:
  pass

try:  
  print('Additional Text Messages Charge: $%.2f' % (extraTextsCost))

except NameError:
  pass

print('911 Fee: $%.2f' % (COST_911))
print('Tax: $%.2f' % (TAX))
print('Total: $%.2f' % (TOTAL))
