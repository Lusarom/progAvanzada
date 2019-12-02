PENNIES_PER_NICKEL=5
NICKEL = 0.05

total = 0.00

line = input('enter the price of the item (black to quit): ')
while line !=' ':

  total = total + float(line)
  line = input ('enter the price of the item(black to quit): ')

print ('the exact amount payable is %.02f'% total)

rounding_indicator = total * 100 % PENNIES_PER_NICKEL

if rounding_indicator< PENNIES_PER_NICKEL /2:

  cash_total = total - rounding_indicator/100

else:

  cash_total = total + NICKEL - rounding_indicator/100

print ('the cash amount payable is %.02f'%cash_total)