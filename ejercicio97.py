from ejercicio94 import randomPassword
from ejercicio96 import checkPassword

def main(): 
    n = 0
    passw = ''
    while not checkPassword(passw): 
        passw = randomPassword()
        n = n+1
    print("Intentos: ", n)
    print("Password: ", passw)
    
main()