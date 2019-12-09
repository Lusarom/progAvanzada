
WIDTH = 80

def centro(s, width):
    if width < len(s):
        return s
    
    espacios = (width - len(s)) // 2
    resultado = ' ' * espacios + s

    return resultado

def main():
    print(centro(' una fabulosa historia', WIDTH))
    print(centro('por: ', WIDTH))
    print(centro('algunos famosos', WIDTH))
    print()
    print('Una vez en el timpo...')
main()