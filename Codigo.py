import random

def mcd(a, b):
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

def generar_claves():
    p = genera_numero_num()
    q = genera_numero_num()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Elegir un número aleatorio e relativamente primo a phi
    while True:
        e = random.randrange(2, phi)
        if mcd(e, phi) == 1:
            break

    d = modulo_inverso(e, phi)
    return (e, n), (d, n)

def encriptar(msj, llave_publica):
    e, n = llave_publica
    cipher = [pow(ord(char), e, n) for char in msj]
    return cipher

def desencriptar(cipher, llave_privada):
    d, n = llave_privada
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)

# Ejemplo de uso
llave_publica, llave_privada = generar_claves()
msj = "YONYON"
print("Mensaje original:", msj)

msj_encriptado = encriptar(msj, llave_publica)
print("Mensaje encriptado:", ''.join(map(str, msj_encriptado)))

msj_desencriptado = desencriptar(msj_encriptado, llave_privada)
print("Mensaje desencriptado:", msj_desencriptado)