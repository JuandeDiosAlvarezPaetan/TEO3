import random

def mcd(a, b): #Maximo comun divisor
    while b:
        a, b = b, a % b
    return a

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def genera_numero_num():
    while True:
        num = random.getrandbits(16) 
        if es_primo(num):
            return num

def modulo_inverso(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1