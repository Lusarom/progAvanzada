

from math import sqrt

distance = float(input('Inserte altura en metros:'))

gravity = 9.81

final_speed = sqrt(2 * gravity * distance )

print('\n the final speed is: %.2f.' %final_speed, 'm/s')
