

def triangle(a, b, c): 
    lenghts = [a,b,c]
    lenghts.sort()
    if lenghts[2] < (lenghts[1] + lenghts[0]):
        return True
    else: 
        return False

lado_a = float(input("Ingrese lado a: "))
lado_b = float(input("Ingrese lado b: "))
lado_c = float(input("Ingrese lado c: "))

if triangle(lado_a, lado_b, lado_c): 
    print("Es posible construir un triángulo")
else: 
    print("No es posible construir un triángulo")