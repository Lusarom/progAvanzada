print('Precio   | Descuento | Precio Final')
print('--------------------------------------------')
Original = 4.95
while Original <= 24.95:
    Descuento = Original * 0.60
    PrecioFinal = Original - Descuento
    print(' $%.2f''     |'  %Original, '$%.2f''     |' %Descuento, '$%.2f' %PrecioFinal )
    Original = Original + 5
