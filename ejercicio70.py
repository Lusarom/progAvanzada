mensaje = input('Inserta mensaje:')
valor = int(input('Ingrese el valor de cambio'))

newmensaje = ' '

for ch in mensaje:
    if ch >= 'a' and ch <= 'z':
        pos = ord(ch) - ord("a")
        pos = (pos + valor) % 26
        nuevo  = chr(pos + ord ('a'))
        newmensaje = newmensaje + nuevo
    elif ch >= 'A' and ch <= 'Z':
        pos = ord(ch) - ord('A')
        pos = (pos + valor) % 26
        nuevo  = chr(pos + ord ('A'))
        newmensaje = newmensaje + nuevo
else:
    newmensaje = newmensaje + ch
print('El mensaje cambiado es:', newmensaje)
