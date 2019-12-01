#escribir un programa que determine si una palabra insertada por el usuario es palodromo o no lo es
#un palondromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda, por ejemplo
#radar, rotor, rallar, sometemos.

class cadenas:
    def __init__ (self, cade1):
        self.cade1=cade1
 
    def Palidromo(self):
        cade1 = self.cade1
        c,i,nom,cade,x = 0,0,'','',''
        i = len(cade1)
        nom = cade1.lower()
        
        while i != c:
            for x in nom:
                cade = x + cade
                c=c+1
            if nom==cade:
                #print (cade1, 'Palindromo')
                return str(cade1 + 'Palindromo')
            else:
                #print (cade1, 'Error de Palindromo')
                return str(cade1 + 'Error de Palindromo')
 
cade1 = input('Escribe una palabra')
op1=cadenas(cade1)
 
print(op1.Palidromo())
