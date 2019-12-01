print('Celsius', 'Fahrenheit')

for num in range(1, 11):
    celsius = num * 10
    print(celsius, end='      ')
    fahrenheit = 1.8 * celsius + 32
    print(fahrenheit, end=' ')
    print('\n')
