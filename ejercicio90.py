
def es_entero (s):
    s = s.strip()

    if (s[0] == '+' or s[0] == '-' and s[1:].isdigit()):
        return True
    
    if s.isdigit():
        return True
    return False

def main():
    s = input ('Introduce la cadena: ')
    if es_entero(s):
        print('La cadena representa un entero.')
    else:
        print('La cadena no es un entero.')
if __name__ == '__main__':
    main()
