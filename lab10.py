import random
from math import pow
import base64
 
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
        
def encrypt(msg, q, h, g, clave):
 
    en_msg = []
 
    k = clave
    s = modulo(h, k, q)
    p = modulo(g, k, q)
     
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
 
    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
        
    concatenado = ""
    for i in en_msg:
        concatenado += str(i)
    encodedBytes = base64.b64encode(concatenado.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(encodedStr)
    return en_msg, p

def decrypt(en_msg, p, key, q):
 
    dr_msg = []
    h = modulo(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
         
    return dr_msg
while True:
    print("1. Generar claves")
    print("2. Encriptar mensaje")
    print("3. Decriptar mensaje")
    print("4. Salir.")
    opcion = input("Ingresa el numero de opcion a elegir\n")
    
    if(opcion == "1"):
        print("Generar Claves")
        q = generarPrimo()
        g = random.randint(2, q)
        claveprivada = generarClave(q)
        h = modulo(g, claveprivada, q)
        clavepublica = (g, h)
        
        print("")        
        print("p:", q)
        print("g:", g)
        print("h:", h)
        print("clave privada:", claveprivada)
        print("clave publica:", clavepublica)
        print("")

        
    elif(opcion == "2"):
        print("Encriptar mensaje")
        msg = input("Ingrese mensaje a encriptar:\n")
        en_msg, p = encrypt(msg, q, h, g, claveprivada)
    elif(opcion == "3"):
        print("Decriptar mensaje")
        decriptado = decrypt(en_msg, p, claveprivada, q)
        dmsg = ''.join(decriptado)
        print(dmsg)
    elif(opcion == "4"):
        break
