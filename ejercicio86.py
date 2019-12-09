#Ejercicio 86


from int_ordinal import intToOrdinal

def displayVerse (n):
    print('un', intToOrdinal(n), 'dia de navidad')
    print('Mi verdadero amor me envio: ')

    if n >= 12:
        print('doce bateristas tamborileando,')
    if n >= 11:
        print('once gaiteros giteando,')
    if n >= 10:
        print('diez señores saltando,')
    if n >= 9:
        print('nueve señoras bailando')
    if n >= 8:
        print('ocho criadas un ordeño')
    if n >= 7:
        print('siete nadadores nadando')
    if n >= 6:
        print('seis gansos colocados')
    if n >= 5:
        print('5 anillos de oro')
    if n >= 4:
        print('cuatro aves voladoras')
    if n >= 3:
        print('tres gallinas francesas')
    if n >= 2:
        print('dos tortolas')
    if n >= 1:
        print('A', end=' ')
    else:
        print('y una ', end=' ')
    print('perdiz en un peral')
    print()
def main():
    for verse in range (1, 13):
        displayVerse(verse)
main()