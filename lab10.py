import random
from math import pow
 
a = random.randint(2, 10)

def esprimo(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True
    
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
 
def generarClave(q):
    llave = random.randint(1, (q - 1) // 2)
    return llave
 
def modulo(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c
 
def esprimo(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True

def generarPrimo(): 
    while True: 
        x=random.randrange(10000,100000) 
        if(esprimo(x)==True):
            return x

while True:
    print("1. Generar claves")
    print("2. Encriptar mensaje")
    print("3. Decriptar mensaje")
    print("4. Salir.")
    opcion = input("Ingresa el numero de opcion a elegir\n")
    
    if(opcion == "1"):
        print("Generar Claves")
        p = generarPrimo()
        g = random.randint(2, p)
        claveprivada = generarClave(p)
        h = modulo(g, claveprivada, p)
        clavepublica = (g, h)
        
        print("")        
        print("p:", p)
        print("g:", g)
        print("h:", h)
        print("clave privada:", claveprivada)
        print("clave publica:", clavepublica)
        print("")

        
    elif(opcion == "2"):
        print("Encriptar mensaje")
    elif(opcion == "3"):
        print("Decriptar mensaje")
    elif(opcion == "4"):
        break