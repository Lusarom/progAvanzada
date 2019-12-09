
def precedence(operation):
    operation = operation.strip()
    if (operation == '+') or (operation == '-'): 
        return 1
    elif (operation == '*') or (operation == '/'): 
        return 2
    elif (operation == '^'):
        return 3
    else: 
        return -1
    
    
def main():    
    op = input("Ingrese el símbolo de la operación que desea evaluar: ")

    result = precedence(op)
    if result == -1: 
        print("El símbolo ingresado no es una operación válida")
    else: 
        print(result)
main()