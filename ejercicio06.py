IVA=0.16
Propina=0.15

Platillo1= input('Insertar Platillo')
print('Platillo 1', Platillo1)
Precio1= float (input('Insertar Precio'))
print('Precio 1', Precio1)

Platillo2= input('Insertar Platillo')
print('Platillo 2', Platillo2)
Precio2= float (input('Insertar Precio'))
print('Precio 2', Precio2)

Platillo3= input('Insertar Platillo')
print('Platillo 3', Platillo3)
Precio3= float (input('Insertar Precio'))
print('Precio 3', Precio3)

Platillo4= input('Insertar Platillo')
print('Platillo 4', Platillo4)
Precio4= float (input('Insertar Precio'))
print('Precio 4', Precio4)

Platillo5= input('Insertar Platillo')
print('Platillo 5', Platillo5)
Precio5= float (input('Insertar Precio'))
print('Precio 5', Precio5)

Subtotal= Precio1+Precio2+Precio3+Precio4+Precio5
print('Subtotal',)

IVA=Subtotal*0.16
Subtotal1=Subtotal+IVA
print('IVA',Subtotal1)

Propina=Subtotal*.015
Subtotal2=Subtotal+Propina
print('Propina',Subtotal2)

TOTAL=Subtotal+Subtotal1+Subtotal2
print('TOTAL',TOTAL)
