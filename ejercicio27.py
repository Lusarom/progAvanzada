## Calculadora de IMC
masa = float(input('Inserte su masa en kilogramos:'))
estatura = float(input('Inserte su estatura en metros:'))

imc = masa / estatura**2

if imc < 16:
    print('Tiene delgadez severa')
elif imc >=16 and imc < 17 :
    print('Tiene delgadez moderada')
elif imc >=17 and imc < 18.5 :
    print('Tiene delgadez leve')
elif imc >=18.5 and imc < 25 :
    print('Tiene IMC normal')
elif imc >=25 and imc < 30 :
    print('Tiene preobesidad')
elif imc >=30 and imc < 35 :
    print('Tiene obesidad leve')
elif imc >=35 and imc < 40 :
    print('Tiene obesidad media')
elif imc >= 40 :
    print('Tiene obesoidad morbida')
else:
    print('Opcion invalida')

    print('Su imc fue de ', imc)