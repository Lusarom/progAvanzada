lessdep = 0.10
moredep = 0.25
less = int (input('¿Cuantas botellas pequeñas han ingresado?'))
more=int(input('¿Cuantas botellas grandes han ingresado?'))
operation = less * lessdep + more * moredep
print("El total es $%.2f." % operation)
