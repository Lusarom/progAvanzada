inter=0.04
deposit=float(input('Ingrese la cantidad a depositar en el año:$'))
anio1=deposit*inter
anio1T=anio1+deposit
print('El total en su cuenta en este año es:$%.2f' %anio1T)
anio2=anio1T*inter
anio2T=anio1T+anio2
print('El total en su cuenta en este año es:$%.2f' %anio2T)
anio3=anio2T*inter
anio3T=anio2T+anio3
print('El total en su cuenta en este año es:$%.2f' %anio3T)
