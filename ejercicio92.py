

def Primo (n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def main():
        value = int(input('Introduce un numero entero: '))
        if Primo(value):
            print(value, 'es primo.')
        else:
            print(value,'No es primo')
if __name__ == '__main__':
        main()
