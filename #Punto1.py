import random

# Solicitar al usuario el rango
inicio = int(input('Ingrese el valor inicial del rango: '))
fin = int(input('Ingrese el valor final del rango: '))

# Solicitar al usuario la cantidad de números aleatorios
cantidad_numeros = int(input('Ingrese la cantidad de números aleatorios que desea generar: '))

# Generar y mostrar los números aleatorios
print(f'\nNúmeros aleatorios en el rango [{inicio}, {fin}]:')
for _ in range(cantidad_numeros):
    numero_aleatorio = random.randint(inicio, fin)
    print(numero_aleatorio)