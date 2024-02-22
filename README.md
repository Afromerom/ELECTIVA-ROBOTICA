# ELECTIVA-ROBOTICA
<h1 align="center">Taller 1 Python<br>
Materia: Electiva de robótica<br>
Universidad: ECCI 🏫<br>
Andrés Felipe Romero Medina 🤖<br> 
Nicolás Mejía Muñoz 🤖<br> 
TALLER 1 <br>
22/0/2024 📅</h1><br>
<h2>Taller 1 – Python (código)🐍</h2>
<h2>Sin interacción de consola</h2>
<h4>Impresión de datos en consola</h4>
<h2>Punto 1</h2>
Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
vectores previamente inicializados.

```python
# Definición de dos vectores
a = [1, 2, 3]
b = [3, 4, 5]
# Función para la suma de dos vectores
def suma_de_vectores(a, b):
    return [x + y for x, y in zip(a, b)]
# Función para la resta de dos vectores
def resta_de_vectores(a, b):
    return [x - y for x, y in zip(a, b)]
# Función para el producto punto (producto escalar) de dos vectores
def ppunto_de_vectores(a, b):
    return sum(x * y for x, y in zip(a, b))
# Función para el producto cruz de dos vectores en 3D
def pcruz_de_vectores(a, b):
    return [
        a[1] * b[2] - b[1] * a[2],
        -(a[0] * b[2] - b[0] * a[2]),
        a[0] * b[1] - b[0] * a[1]
    ]
# Función para la división de elementos correspondientes de dos vectores
def division_de_vectores(a, b):
    return [x / y for x, y in zip(a, b)]
# Impresión de los resultados
print("suma: ", suma_de_vectores(a, b))
print("resta: ", resta_de_vectores(a, b))
print("producto punto: ", ppunto_de_vectores(a, b))
print("producto cruz: ", pcruz_de_vectores(a, b))
print("division: ", division_de_vectores(a, b))
```
<h2>Punto 2</h2>
Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
matrices previamente inicializadas.

```python
c = ([1, 2, 3],[4,5,6],[7,8,9])
d = ([3, 4, 5],[6,7,8],[9,10,11])
def sum_matrices(c, d):
    result = []
    for i in range(len(c)):
        row = []
        for j in range(len(c[0])):
            row.append(c[i][j] + d[i][j])
        result.append(row)
    return result
sum_result = sum_matrices(c, d)
print("Suma de matrices:")
for row in sum_result:
    print(row)
c = ([1, 2, 3],[4,5,6],[7,8,9])
d = ([3, 4, 5],[6,7,8],[9,10,11])
def sum_matrices(c, d):
    result = []
    for i in range(len(c)):
        row = []
        for j in range(len(c[0])):
            row.append(c[i][j] - d[i][j])
        result.append(row)
    return result
sum_result = sum_matrices(c, d)
print("Resta de matrices:")
for row in sum_result:
    print(row)
###########################################################################################
def producto_punto_matrices(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
matriz_A = [[1, 2, 3],[4,5,6],[7,8,9]]
matriz_B = [[3, 4, 5],[6,7,8],[9,10,11]]
resultado_producto_punto = producto_punto_matrices(matriz_A, matriz_B)
print("Producto punto de las matrices A y B:")
for fila in resultado_producto_punto:
    print(fila)
############################################################################################
def producto_cruz_matrices(matrix1, matrix2):
    if len(matrix1) != 3 or len(matrix2) != 3:
        raise ValueError("Las matrices deben ser de dimensiones 3x3 para el producto cruz.")

    result = [[0] * 3 for _ in range(3)]
    for i in range(3):
        result[i][0] = matrix1[(i + 1) % 3][1] * matrix2[(i + 2) % 3][2] - matrix1[(i + 2) % 3][1] * matrix2[(i + 1) % 3][2]
        result[i][1] = matrix1[(i + 2) % 3][0] * matrix2[(i + 1) % 3][2] - matrix1[(i + 1) % 3][0] * matrix2[(i + 2) % 3][2]
        result[i][2] = matrix1[(i + 1) % 3][0] * matrix2[(i + 2) % 3][1] - matrix1[(i + 2) % 3][0] * matrix2[(i + 1) % 3][1]

    return result
matriz_A = [[1, 2, 3],[4,5,6],[7,8,9]]
matriz_B = [[3, 4, 5],[6,7,8],[9,10,11]]
resultado_manual = producto_cruz_matrices(matriz_A, matriz_B)
print("Producto cruz de las matrices A y B:")
for fila in resultado_manual:
    print(fila)
```

<h2>Punto 3</h2>
Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual
deben consultar sobre el uso de funciones trigonométricas en Python.

```python
import cmath
# Programa coordenadas polares a cartesianas
r = 50
theta = 80 * (cmath.pi / 180)
# Coordenadas polares a cartesianas
x, y = cmath.polar(cmath.rect(r, theta))
coordinates_polar_to_cartesian = f'Programa coordenadas polares a cartesianas y viceversa\nDe polares a rectangulares en la función r=50 θ=80°\nEl vector corresponde a: A=[{x} + {y}j]'
# Programa coordenadas cartesianas a polares
A = 80 + 60j
r1, theta2 = cmath.polar(A)
coordinates_cartesian_to_polar = f'De rectangulares a polares en la función 80+60i\nEl vector corresponde a: [r = {r1} , θ = {cmath.phase(A)*180/cmath.pi}°]'
print(coordinates_polar_to_cartesian)
print(coordinates_cartesian_to_polar)
```

<h2>Punto 4</h2>
Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de
la temperatura.

```python
# Definimos la temperatura
Ta = 100  # °C
# Definimos la resistencia medida
R = 5000  # ohmios
# Definimos el valor nominal de la resistencia a 0 °C
R0 = 200  # ohmios
# Definimos la temperatura inicial
T = 0  # °C
# Constantes de la ecuación de Callendar-Van Dusen
A = 3.90830e-3
B = -5.77500e-7
C = -4.18301e-12
# Calculamos la resistencia RTD de platino (PT100)
rtd = R0 * (1 + A * T + B * T**2 + (T - 100) * C * T**3)
# Mostramos el resultado
print("El valor de la resistencia RTD de platino (PT100) a", Ta, "°C es:", rtd, "ohmios")
```
<h2>Punto 5</h2>
Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz).

```python
import numpy as np
rotarx = 90
rotary = 90
rotarz = 90
def rotation_matrix_x(angle):
    radian_angle = np.radians(angle)
    return np.array([
        [1, 0, 0],
        [0, np.cos(radian_angle), -np.sin(radian_angle)],
        [0, np.sin(radian_angle), np.cos(radian_angle)]
    ])
def rotation_matrix_y(angle):
    radian_angle = np.radians(angle)
    return np.array([
        [np.cos(radian_angle), 0, np.sin(radian_angle)],
        [0, 1, 0],
        [-np.sin(radian_angle), 0, np.cos(radian_angle)]
    ])
def rotation_matrix_z(angle):
    radian_angle = np.radians(angle)
    return np.array([
        [np.cos(radian_angle), -np.sin(radian_angle), 0],
        [np.sin(radian_angle), np.cos(radian_angle), 0],
        [0, 0, 1]
    ])
# Imprimir matrices de rotación de 90 grados
print("Matriz de rotación alrededor del eje X (90°):")
print(rotation_matrix_x(rotarx))
print("\nMatriz de rotación alrededor del eje Y (90°):")
print(rotation_matrix_y(rotary))
print("\nMatriz de rotación alrededor del eje Z (90°):")
print(rotation_matrix_z(rotarz))
```
<h2>Punto 6</h2>
Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
cilindro para realizar el cálculo.

```python
#Definimos los valores del radio externo e interno
radio_externo = 50
radio_interno = 15
#Definimos el valor de la presión
presion = 20
#Calculamos el área del cilindro mayor
area_salida = 3.14159 * radio_externo**2
#Calculamos la fuerza de salida
fuerza_salida = presion * area_salida
#Calculamos el área de entrada
area_entrada = area_salida - (3.14159 * radio_interno**2)
#Calculamos la fuerza de entrada
fuerza_entrada = presion * area_entrada
#Mostramos los resultados en pantalla
print(f"El valor de la fuerza de salida es: {fuerza_salida} N")
print(f"El valor de la fuerza de entrada es: {fuerza_entrada} N")
```

<h4>Con interacción de consola (fprintf o disp) y teclado (input)</h4>

<h2>Punto 1</h2>
Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el
valor de corriente y voltaje.

```python
print('Programa calculo de la potencia de un circuito')  # Plasmamos en pantalla

# Tomamos las variables del usuario
v = float(input('Escriba el voltaje del circuito: '))
k = float(input('Escriba la corriente del circuito: '))

# Calculamos el valor de la potencia
pot = v * k

# Plasmamos en pantalla el resultado
result_message = f'La potencia del voltaje: {v} V y la corriente: {k} mA corresponde a: {pot} watts.'
print(result_message)
```

<h2>Punto 2</h2>
Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.

```python
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
```

<h2>Punto 3</h2>
Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro)
donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen.

```python
import math
# Programa de calculo de áreas
print('Programa calculo de volumenes')
print('1. Cálculo de volumen de Prisma')
print('2. Cálculo de volumen de Piramide')
print('3. Cálculo de volumen de Cono Truncado')
print('4. Cálculo de volumen de Cilindro')

opt = int(input('Ingrese la figura que desea validar: '))

if opt == 1:
    print('1. Cálculo de volumen de Prisma')
    l = float(input('Escriba el valor del lado: '))
    b = float(input('Escriba el valor de la base: '))
    h = float(input('Escriba el valor de la altura: '))
    vpris = l * b * h
    print(f'El volumen del Prisma corresponde a: {vpris} m³')
elif opt == 2:
    print('2. Cálculo de volumen de la piramide')
    b1 = float(input('Escriba el valor de la base: '))
    h1 = float(input('Escriba el valor de la altura: '))
    vpi = (1/3) * (b1 * h1)
    print(f'El volumen de la Piramide corresponde a: {vpi} m³')
elif opt == 3:
    print('3. Cálculo de volumen del Cono Truncado')
    R = float(input('Escriba el valor del radio de la base inferior: '))
    r = float(input('Escriba el valor del radio de la base superior: '))
    h2 = float(input('Escriba el valor de la altura: '))
    vct = ((h2 * math.pi) / 3) * (R**2 + r**2 + R * r)
    print(f'El volumen del Cono truncado corresponde a: {vct} m³')
elif opt == 4:
    print('4. Cálculo de volumen de Cilindro')
    al = float(input('Escriba el valor de la altura: '))
    ra = float(input('Escriba el valor del radio: '))
    vci = math.pi * ra**2 * al
    print(f'El volumen del Cilindro corresponde a: {vci} m³')
else:
    print('Opción no válida')

```
<h2>Punto 4</h2>
Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico,
donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.

```python
# Programa Robots
print('Programa Robots')  # Plasmamos en pantalla
print('1.Robot Cilindrico')  # Plasmamos en pantalla
print('2.Robot Cartesiano')  # Plasmamos en pantalla
print('3.Robot Esferico')  # Plasmamos en pantalla
opt = int(input('Ingrese la figura que desea validar: '))  # Definimos la opción en pantalla

if opt == 1:  # Caso 1
    print('1.Robot Cilindrico')  # Plasmamos en pantalla
    print('Posee articulaciones rotacional, prismatico, prismatico ')  # Plasmamos en pantalla
elif opt == 2:  # Caso 2
    print('2.Robot Cartesiano')  # Plasmamos en pantalla
    print('Posee articulaciones prismatico, prismatico, prismatico')  # Plasmamos en pantalla
elif opt == 3:  # Caso 3
    print('3.Robot Esferico')  # Plasmamos en pantalla
    print('Posee articulaciones rotacional, rotacional, prismatico')  # Plasmamos en pantalla
else:
    print('Opción no válida')  # Manejo de opción no válida
```

<h2>Punto 5</h2>
Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla
hasta que el usuario teclee No.

```python
print('Programa promedio de Pregunta S/N')

respuesta = 'Si'  # Definimos la respuesta como 's'

while respuesta == 'Si':  # Mientras que la respuesta sea 'Si'
    print('¿Desea continuar? (s=si)(n=no)')  # Preguntar Desea continuar Si/No
    respuesta = input()
```
<h4>Uso de las funciones para graficar</h4>