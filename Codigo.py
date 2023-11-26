import random
import string

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

    # Elegir un número aleatorio e  primo a phi
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

# Ejemplo
llave_publica, llave_privada = generar_claves()
msj = "Mensaje"
print("Mensaje original:", msj)

msj_encriptado = encriptar(msj, llave_publica)
print("Mensaje encriptado:", ''.join(map(str, msj_encriptado)))

msj_desencriptado = desencriptar(msj_encriptado, llave_privada)
print("Mensaje desencriptado:", msj_desencriptado)

def seleccionar_imagenes_y_pines():
    opciones_imagenes = ['Gato', 'Perro', 'Motocicleta', 'Achimenea', 'Bicicleta', 'Laptop', 'Bufanda', 'Mouse', 'Tienda', 'Camion', 'Autobus']
    opciones_pines = ['1234', '5678', '2468', '1357', '7413', '4620', '2003', '9210', '0001']

    imagenes_seleccionadas = []
    pines_seleccionados = []
    letra_imagen = {}  # Almacena las opciones de imágenes asociadas a las letras
    letra_pin = {}  # Almacena las opciones de pines asociadas a las letras
    
    random.shuffle(opciones_imagenes)  # Mezclar las opciones de imágenes
    random.shuffle(opciones_pines)  # Mezclar las opciones de pines
    
    print("Seleccione las imagenes:")
    for i in range(3):  # Solicitar tres imágenes
        opciones_mostradas = opciones_imagenes[i * 3 : (i + 1) * 3]  # Mostrar tres opciones en cada elección
        letra_opciones = string.ascii_lowercase[:len(opciones_mostradas)]  # Letras disponibles para seleccionar
        
        print(f"\nOpciones {i + 1}:\n")
        for j, opcion in enumerate(opciones_mostradas):
            letra = letra_opciones[j]
            letra_imagen[letra] = opcion  # Asociar la letra con la opción de imagen mostrada
            print(f"{letra}) {opcion}")
        
        # Validacion
        seleccion = input(f"\nSeleccione una opcion para la imagen {i + 1}: ").lower()
        while seleccion not in letra_imagen:
            seleccion = input("Ingrese una opcion valida (a, b, c): ").lower()
        
        imagenes_seleccionadas.append(letra_imagen[seleccion])
    
    print("\nSeleccione los pines:")
    for i in range(3):  # Solicitar tres pines
        opciones_mostradas = opciones_pines[i * 3 : (i + 1) * 3]  # Mostrar tres opciones en cada elección
        letra_opciones = string.ascii_lowercase[:len(opciones_mostradas)]  # Letras disponibles para seleccionar
        
        print(f"\nOpciones {i + 1}:\n")
        for j, opcion in enumerate(opciones_mostradas):
            letra = letra_opciones[j]
            letra_pin[letra] = opcion  # Asociar la letra con la opción de pin mostrada
            print(f"{letra}) {opcion}")
        
        # Validacion
        seleccion = input(f"\nSeleccione una opcion para el pin {i + 1}: ").lower()
        while seleccion not in letra_pin:
            seleccion = input("Ingrese una opcion valida (a, b, c): ").lower()
        
        pines_seleccionados.append(letra_pin[seleccion])
    
    return imagenes_seleccionadas, pines_seleccionados

# Muestra las opciones seleccionadas
imagenes, pines = seleccionar_imagenes_y_pines()
print("Imagenes seleccionadas:", imagenes)
print("Pines seleccionados:", pines)