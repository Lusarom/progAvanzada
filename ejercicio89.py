

def capitilize(s):

    result = s.replace(" i "," I ")
    

    if len(s) > 0:
        print("resultado[0]",result[0])
        result = result[0].upper() + \
        result[1 : len(result)]
        print("escribe con mayúscula el primer carácter de la cadena", result)

    
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            
            pos = pos + 1

            
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1

            
            if pos < len(s):
                result = result[0:pos] + \
                result[pos].upper()+ \
                result[pos+1:len(result)] 
            
        pos = pos + 1

    return result

def main():
    s = input("Introduce el texto: ")
    capitalized = capitilize(s)
    print("Se capitaliza como:", capitalized)


main()
