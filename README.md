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
import numpy as np
# Definir dos matrices para el producto punto
matriz_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_B = [[3, 4, 5], [6, 7, 8], [9, 10, 11]]
############### SUMA ###############################
def sum_matrices(matriz_A, matriz_B):
    result = []
    for i in range(len(matriz_A)):
        row = []
        for j in range(len(matriz_A[0])):
            row.append(matriz_A[i][j] + matriz_B[i][j])
        result.append(row)
    return result
# Calcular la suma de las matrices c y d
sum_result = sum_matrices(matriz_A , matriz_B)
print("Suma de matrices:")
for row in sum_result:
    print(row)
############### RESTA ##############################
def rest_matrices(matriz_A , matriz_B):
    result = []
    for i in range(len(matriz_A )):
        row = []
        for j in range(len(matriz_A[0])):
            row.append(matriz_A [i][j] - matriz_B[i][j])
        result.append(row)
    return result
# Calcular la resta de las matrices c y d
rest_result = rest_matrices(matriz_A , matriz_B)
print("Resta de matrices:")
for row in rest_result:
    print(row)
################## PRODUCTO PUNTO ##################
def producto_punto_matrices(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
# Calcular el producto punto de las matrices A y B
resultado_producto_punto = producto_punto_matrices(matriz_A, matriz_B)
print("Producto punto de las matrices A y B:")
for fila in resultado_producto_punto:
    print(fila)
################## PRODUCTO CRUZ ###################
def producto_cruz_matrices(matrix1, matrix2):
    if len(matrix1) != 3 or len(matrix2) != 3:
        raise ValueError("Las matrices deben ser de dimensiones 3x3 para el producto cruz.")

    result = [[0] * 3 for _ in range(3)]
    for i in range(3):
        result[i][0] = matrix1[(i + 1) % 3][1] * matrix2[(i + 2) % 3][2] - matrix1[(i + 2) % 3][1] * matrix2[(i + 1) % 3][2]
        result[i][1] = matrix1[(i + 2) % 3][0] * matrix2[(i + 1) % 3][2] - matrix1[(i + 1) % 3][0] * matrix2[(i + 2) % 3][2]
        result[i][2] = matrix1[(i + 1) % 3][0] * matrix2[(i + 2) % 3][1] - matrix1[(i + 2) % 3][0] * matrix2[(i + 1) % 3][1]

    return result
# Calcular el producto cruz de las matrices A y B
resultado_manual = producto_cruz_matrices(matriz_A, matriz_B)
print("Producto cruz de las matrices A y B:")
for fila in resultado_manual:
    print(fila)
################## DIVISIÓN ########################
def dividir_matrices(matriz1, matriz2):
    # Realizar la división elemento por elemento utilizando numpy
    resultado = np.divide(matriz1, matriz2)
    return resultado
# Calcular la división elemento por elemento de las matrices A y B
print("La división entre las matrices A y B:", dividir_matrices(matriz_A, matriz_B))
```

<h2>Punto 3</h2>
Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual
deben consultar sobre el uso de funciones trigonométricas en Python.

```python
import math

def cartesian_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)  # Radio en el plano xy
    theta = math.atan2(y, x)    # Ángulo azimutal en el plano xy
    z_cylindrical = z            # La coordenada z se mantiene igual en coordenadas cilíndricas
    return r, theta, z_cylindrical

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)  # Radio esférico
    theta = math.atan2(y, x)            # Ángulo azimutal en el plano xy
    phi = math.acos(z / r)              # Ángulo de elevación con respecto al eje z
    return r, theta, phi

# Usa las coordenadas rectangulares
x = 4
y = 5
z = 6

# Convertir a coordenadas cilíndricas
r_cylindrical, theta_cylindrical, z_cylindrical = cartesian_to_cylindrical(x, y, z)
print(f"\nCoordenadas Cilíndricas: r = {r_cylindrical}, θ = {theta_cylindrical}, z = {z_cylindrical}")

# Convertir a coordenadas esféricas
r_spherical, theta_spherical, phi_spherical = cartesian_to_spherical(x, y, z)
print(f"Coordenadas Esféricas: r = {r_spherical}, θ = {theta_spherical} rad, φ = {phi_spherical} rad")
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
v = float(input('Escriba el voltaje (V) del circuito: '))
k = float(input('Escriba la corriente (A) del circuito: '))
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
while True:
    respuesta = input("¿Desea continuar Si/No? ")

    if respuesta == "no":
        break
    elif respuesta != "si":
        print("Por favor, ingrese Si o No.")
```
<h4>Uso de las funciones para graficar</h4>


<h2>Punto 1</h2>
Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C.

```python
import numpy as np
import matplotlib.pyplot as plt
# Definir el rango de temperatura de -200°C a 200°C
temperaturas = np.linspace(-200, 200, 400)
# Simular el comportamiento del sensor PT100 (esto es solo un ejemplo, no representa la realidad)
# Puedes ajustar los valores de la resistencia en función de la temperatura según la tabla de calibración de un PT100 real
resistencia_referencia = 100.0  # Resistencia a 0°C (valor de referencia)
coeficiente_temperatura = 0.00385  # Coeficiente de temperatura del PT100
# Calcular la resistencia en función de la temperatura
resistencias = resistencia_referencia * (1 + coeficiente_temperatura * temperaturas)
# Graficar el comportamiento del sensor PT100
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, label='Sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohmios)')
plt.title('Comportamiento del Sensor PT100')
plt.legend()
plt.grid(True)
plt.show()
```

<h2>Punto 2</h2>
Realice un programa que le permita al usuario ingresar los coeficientes de una función de
transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo
de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Función para determinar el tipo de sistema
def determinar_tipo_sistema(zeta):
    if zeta < 1:
        return "Subamortiguado"
    elif zeta == 1:
        return "Críticamente Amortiguado"
    else:
        return "Sobreamortiguado"

# Solicitar al usuario ingresar los coeficientes
omega_n = float(input("Ingrese la frecuencia natural (omega_n): "))
zeta = float(input("Ingrese el coeficiente de amortiguamiento (zeta): "))
ganancia = float(input("Ingrese la ganancia: "))

# Crear la función de transferencia de segundo orden
num = [ganancia * omega_n**2]
den = [1, 2 * zeta * omega_n, omega_n**2]
system = signal.TransferFunction(num, den)

# Determinar el tipo de sistema
tipo_sistema = determinar_tipo_sistema(zeta)
print(f"El sistema es {tipo_sistema}")

# Crear un rango de tiempo
t = np.linspace(0, 10, 1000)

# Calcular la respuesta del sistema al impulso
t, y = signal.step(system, T=t)

# Graficar la respuesta del sistema
plt.plot(t, y)
plt.title('Respuesta del Sistema de Segundo Orden')
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.grid(True)
plt.show()
```
<h2>Punto 3</h2>
Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el
valor de voltaje (V), capacitancia (....) y resistencia (O). Posteriormente realice en Python la
gráfica.

```python
import numpy as np
import matplotlib.pyplot as plt

def carga_descarga_RC(tiempo, voltaje, resistencia, capacitancia, carga=True):
    tau = resistencia * capacitancia  # Constante de tiempo (tau)
    if carga:
        return voltaje * (1 - np.exp(-tiempo / tau))
    else:
        return voltaje * np.exp(-tiempo / tau)

def convertir_a_microfaradios(valor_faradios):
    return valor_faradios * 1e6

# Entrada de usuario
voltaje = float(input("Ingrese el valor de voltaje (V): "))
resistencia = float(input("Ingrese el valor de resistencia (ohmios): "))
capacitancia_faradios = float(input("Ingrese el valor de capacitancia (micro faradios): "))

# Conversión a microfaradios
capacitancia_microfaradios = convertir_a_microfaradios(capacitancia_faradios)

# Generar datos para la gráfica
tiempo = np.linspace(0, 5 * resistencia * capacitancia_faradios, 1000)
voltajes_carga = carga_descarga_RC(tiempo, voltaje, resistencia, capacitancia_faradios, carga=True)
voltajes_descarga = carga_descarga_RC(tiempo, voltaje, resistencia, capacitancia_faradios, carga=False)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(tiempo, voltajes_carga, label='Carga')
plt.plot(tiempo, voltajes_descarga, label='Descarga')
plt.title('Carga y Descarga en un Circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.show()
```

<h2>Punto 4</h2>
Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas
ingresadas por el usuario.

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_vector(ax, vector, color='b', label='Vector'):
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color=color, label=label)
    ax.set_xlim([0, max(vector[0], 1)])
    ax.set_ylim([0, max(vector[1], 1)])
    ax.set_zlim([0, max(vector[2], 1)])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.legend()

def main():
    # Solicitar al usuario ingresar las coordenadas del vector
    x = float(input("Ingrese la coordenada X del vector: "))
    y = float(input("Ingrese la coordenada Y del vector: "))
    z = float(input("Ingrese la coordenada Z del vector: "))
    vector = np.array([x, y, z])
    # Crear el sistema de coordenadas 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Dibujar el vector en el sistema de coordenadas 3D
    plot_vector(ax, vector)
    # Mostrar el gráfico
    plt.show()
main()
```

<h2>Punto 5</h2>
Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta
líneas rectas y/o curvas.

```python
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(1, 3.51, 0.01)
x = 0 * y + 3
plt.plot(x, y, 'b', linewidth=2)

x1 = np.arange(3, 4.01, 0.01)
y1 = -1.5 * x1 + 8
plt.plot(x1, y1, 'b', linewidth=2)

x2 = np.arange(4, 5, 0.01)
y2 = 1.5 * x2 - 4
plt.plot(x2, y2, 'b', linewidth=2)

y3 = np.arange(1, 3.5, 0.01)
x3 = 0 * y3 + 5
plt.plot(x3, y3, 'b', linewidth=2)

y4 = np.arange(1, 3.51, 0.01)
x4 = 0 * y4 + 6
plt.plot(x4, y4, 'b', linewidth=2)

x5 = np.arange(6, 7.01, 0.01)
y5 = 0 * x5 + 3.5
plt.plot(x5, y5, 'b', linewidth=2)

x6 = np.arange(6, 6.51, 0.01)
y6 = 0 * x6 + 2.3
plt.plot(x6, y6, 'b', linewidth=2)

x7 = np.arange(6, 7.01, 0.01)
y7 = 0 * x7 + 1
plt.plot(x7, y7, 'b', linewidth=2)

x8 = np.arange(8, 9.01, 0.01)
y8 = 0 * x8 + 3.5
plt.plot(x8, y8, 'b', linewidth=2)

x9 = np.arange(8, 9.01, 0.01)
y9 = 0 * x9 + 1
plt.plot(x9, y9, 'b', linewidth=2)

y10 = np.arange(1, 1.51, 0.01)
x10 = 0 * y10 + 8
plt.plot(x10, y10, 'b', linewidth=2)

y11 = np.arange(1, 3.51, 0.01)
x11 = 0 * y11 + 9
plt.plot(x11, y11, 'b', linewidth=2)

y12 = np.arange(1, 3.51, 0.01)
x12 = 0 * y12 + 10
plt.plot(x12, y12, 'b', linewidth=2)

x13 = np.arange(11, 12.01, 0.01)
y13 = 2.5 * x13 - 26.5
plt.plot(x13, y13, 'b', linewidth=2)

x14 = np.arange(12, 13.01, 0.01)
y14 = -2.5 * x14 + 33.5
plt.plot(x14, y14, 'b', linewidth=2)

x15 = np.arange(11.4, 12.61, 0.01)
y15 = 0 * x15 + 2
plt.plot(x15, y15, 'b', linewidth=2)

y16 = np.arange(1, 3.51, 0.01)
x16 = 0 * y16 + 14
plt.plot(x16, y16, 'b', linewidth=2)

y17 = np.arange(1, 3.51, 0.01)
x17 = 0 * y17 + 16
plt.plot(x17, y17, 'b', linewidth=2)

x18 = np.arange(14, 15.01, 0.01)
y18 = -1.5 * x18 + 24.5
plt.plot(x18, y18, 'b', linewidth=2)

x19 = np.arange(15, 16.01, 0.01)
y19 = 1.5 * x19 - 20.5
plt.plot(x19, y19, 'b', linewidth=2)

y20 = np.arange(1, 3.51, 0.01)
x20 = 0 * y20 + 17
plt.plot(x20, y20, 'b', linewidth=2)

y21 = np.arange(1, 3.51, 0.01)
x21 = 0 * y21 + 18.5
plt.plot(x21, y21, 'b', linewidth=2)

x22 = np.arange(17, 18.51, 0.01)
y22 = 0 * x22 + 1
plt.plot(x22, y22, 'b', linewidth=2)

y23 = np.arange(1, 3.55, 0.01)
x23 = 0 * y23 + 19.5
plt.plot(x23, y23, 'b', linewidth=2)

y24 = np.arange(1, 3.51, 0.01)
x24 = 0 * y24 + 21
plt.plot(x24, y24, 'b', linewidth=2)

x25 = np.arange(19.5, 21.01, 0.01)
y25 = -1.7 * x25 + 36.7
plt.plot(x25, y25, 'b', linewidth=2)

x26 = np.arange(19.5, 21.01, 0.01)
y26 = 0 * x26 + 3.9
plt.plot(x26, y26, 'b', linewidth=2)

x27 = np.arange(22, 24.01, 0.01)
y27 = 0 * x27 + 3.5
plt.plot(x27, y27, 'b', linewidth=2)

x28 = np.arange(22, 24.01, 0.01)
y28 = 0 * x28 + 1
plt.plot(x28, y28, 'b', linewidth=2)

x29 = np.arange(25, 27.01, 0.01)
y29 = 0 * x29 + 3.5
plt.plot(x29, y29, 'b', linewidth=2)

x30 = np.arange(25, 27.01, 0.01)
y30 = 0 * x30 + 1
plt.plot(x30, y30, 'b', linewidth=2)

y31 = np.arange(1, 3.51, 0.01)
x31 = 0 * y31 + 22
plt.plot(x31, y31, 'b', linewidth=2)

y32 = np.arange(1, 3.51, 0.01)
x32 = 0 * y32 + 24
plt.plot(x32, y32, 'b', linewidth=2)

x33 = np.arange(25, 27.01, 0.01)
y33 = 1.26 * x33 - 30.5
plt.plot(x33, y33, 'b', linewidth=2)

y34 = np.arange(-3.5, -0.99, 0.01)
x34 = 0 * y34 + 3
plt.plot(x34, y34, 'b', linewidth=2)

y35 = np.arange(-2, -0.99, 0.01)
x35 = 0 * y35 + 5
plt.plot(x35, y35, 'b', linewidth=2)

y36 = np.arange(-3.5, -0.99, 0.01)
x36 = 0 * y36 + 6
plt.plot(x36, y36, 'b', linewidth=2)

y37 = np.arange(-3.5, -0.99, 0.01)
x37 = 0 * y37 + 8
plt.plot(x37, y37, 'b', linewidth=2)

y38 = np.arange(-3.5, -0.99, 0.01)
x38 = 0 * y38 + 9
plt.plot(x38, y38, 'b', linewidth=2)

y39 = np.arange(-3.5, -0.99, 0.01)
x39 = 0 * y39 + 11
plt.plot(x39, y39, 'b', linewidth=2)

y40 = np.arange(-3.5, -0.99, 0.01)
x40 = 0 * y40 + 12
plt.plot(x40, y40, 'b', linewidth=2)

y41 = np.arange(-3.5, -0.99, 0.01)
x41 = 0 * y41 + 15
plt.plot(x41, y41, 'b', linewidth=2)

y42 = np.arange(-3.5, -0.99, 0.01)
x42 = 0 * y42 + 18
plt.plot(x42, y42, 'b', linewidth=2)

y43 = np.arange(-3.5, -0.99, 0.01)
x43 = 0 * y43 + 20
plt.plot(x43, y43, 'b', linewidth=2)

y44 = np.arange(-3.5, -0.99, 0.01)
x44 = 0 * y44 + 22
plt.plot(x44, y44, 'b', linewidth=2)

y45 = np.arange(-3.5, -0.99, 0.01)
x45 = 0 * y45 + 24
plt.plot(x45, y45, 'b', linewidth=2)

y46 = np.arange(-3.5, -0.99, 0.01)
x46 = 0 * y46 + 25
plt.plot(x46, y46, 'b', linewidth=2)

y47 = np.arange(-3.5, -0.99, 0.01)
x47 = 0 * y47 + 28
plt.plot(x47, y47, 'b', linewidth=2)

y48 = np.arange(-3.7, -1.19, 0.01)
x48 = 0 * y48 + 30
plt.plot(x48, y48, 'b', linewidth=2)

y49 = np.arange(-3.5, -0.99, 0.01)
x49 = 0 * y49 + 31
plt.plot(x49, y49, 'b', linewidth=2)

y50 = np.arange(-3.5, -0.99, 0.01)
x50 = 0 * y50 + 32
plt.plot(x50, y50, 'b', linewidth=2)

y51 = np.arange(-3.5, -0.99, 0.01)
x51 = 0 * y51 + 33.5
plt.plot(x51, y51, 'b', linewidth=2)

x52 = np.arange(3, 5.01, 0.01)
y52 = 0 * x52 - 1
plt.plot(x52, y52, 'b', linewidth=2)

x53 = np.arange(3, 5.01, 0.01)
y53 = 0 * x53 - 2
plt.plot(x53, y53, 'b', linewidth=2)

x54 = np.arange(3, 5.01, 0.01)
y54 = -0.8 * x54 + 0.4
plt.plot(x54, y54, 'b', linewidth=2)

x55 = np.arange(6, 8.01, 0.01)
y55 = 0 * x55 - 1
plt.plot(x55, y55, 'b', linewidth=2)

x56 = np.arange(6, 8.01, 0.01)
y56 = 0 * x56 - 3.5
plt.plot(x56, y56, 'b', linewidth=2)

x57 = np.arange(9, 10.01, 0.01)
y57 = -1.5 * x57 + 12.5
plt.plot(x57, y57, 'b', linewidth=2)

x58 = np.arange(10, 11.01, 0.01)
y58 = 1.5 * x58 - 17.5
plt.plot(x58, y58, 'b', linewidth=2)

x59 = np.arange(12, 14.01, 0.01)
y59 = 0 * x59 - 1
plt.plot(x59, y59, 'b', linewidth=2)

x60 = np.arange(12, 14.01, 0.01)
y60 = 0 * x60 - 3.5
plt.plot(x60, y60, 'b', linewidth=2)

x61 = np.arange(12, 13.01, 0.01)
y61 = 0 * x61 - 2.5
plt.plot(x61, y61, 'b', linewidth=2)

x62 = np.arange(15, 17.01, 0.01)
y62 = 0 * x62 - 1
plt.plot(x62, y62, 'b', linewidth=2)

x63 = np.arange(15, 17.01, 0.01)
y63 = 0 * x63 - 2
plt.plot(x63, y63, 'b', linewidth=2)

x64 = np.arange(15, 17.01, 0.01)
y64 = -0.8 * x64 + 10
plt.plot(x64, y64, 'b', linewidth=2)

y65 = np.arange(-2, -0.99, 0.01)
x65 = 0 * y65 + 17
plt.plot(x65, y65, 'b', linewidth=2)

x66 = np.arange(18, 20.01, 0.01)
y66 = 0 * x66 - 1
plt.plot(x66, y66, 'b', linewidth=2)

x67 = np.arange(18, 20.01, 0.01)
y67 = 0 * x67 - 3.5
plt.plot(x67, y67, 'b', linewidth=2)

x68 = np.arange(22, 23.01, 0.01)
y68 = -1.5 * x68 + 32
plt.plot(x68, y68, 'b', linewidth=2)

x69 = np.arange(23, 24.01, 0.01)
y69 = 1.5 * x69 - 37
plt.plot(x69, y69, 'b', linewidth=2)

x70 = np.arange(25, 27.01, 0.01)
y70 = 0 * x70 - 1
plt.plot(x70, y70, 'b', linewidth=2)

x71 = np.arange(25, 27.01, 0.01)
y71 = 0 * x71 - 3.5
plt.plot(x71, y71, 'b', linewidth=2)

x72 = np.arange(25, 26.01, 0.01)
y72 = 0 * x72 - 2.5
plt.plot(x72, y72, 'b', linewidth=2)

x73 = np.arange(28, 30.01, 0.01)
y73 = -0.1 * x73 + 1.8
plt.plot(x73, y73, 'b', linewidth=2)

x74 = np.arange(28, 30.01, 0.01)
y74 = -0.1 * x74 - 0.7
plt.plot(x74, y74, 'b', linewidth=2)

x75 = np.arange(30.5, 31.51, 0.01)
y75 = 0 * x75 - 1
plt.plot(x75, y75, 'b', linewidth=2)

x76 = np.arange(30.5, 31.51, 0.01)
y76 = 0 * x76 - 3.5
plt.plot(x76, y76, 'b', linewidth=2)

x77 = np.arange(32, 33.51, 0.01)
y77 = -1.7 * x77 + 53.4
plt.plot(x77, y77, 'b', linewidth=2)

x78 = np.arange(34, 35.01, 0.01)
y78 = 2.5 * x78 - 88.5
plt.plot(x78, y78, 'b', linewidth=2)

x79 = np.arange(35, 36.01, 0.01)
y79 = -2.5 * x79 + 86.5
plt.plot(x79, y79, 'b', linewidth=2)

x80 = np.arange(34.43, 35.57, 0.01)
y80 = 0 * x80 - 2.4
plt.plot(x80, y80, 'b', linewidth=2)

y81 = np.arange(1, 3.51, 0.01)
x81 = 0 * y81 + 28
plt.plot(x81, y81, 'b', linewidth=2)

x82 = np.arange(28, 30.01, 0.01)
y82 = -1.2 * x82 + 37.1
plt.plot(x82, y82, 'b', linewidth=2)

y83 = np.arange(1, 3.51, 0.01)
x83 = 0 * y83 + 30
plt.plot(x83, y83, 'b', linewidth=2)

y84 = np.arange(1, 3.51, 0.01)
x84 = 0 * y84 + 31.5
plt.plot(x84, y84, 'b', linewidth=2)

x85 = np.arange(31, 32.01, 0.01)
y85 = 0 * x85 + 3.5
plt.plot(x85, y85, 'b', linewidth=2)

x86 = np.arange(31, 32.01, 0.01)
y86 = 0 * x86 + 1
plt.plot(x86, y86, 'b', linewidth=2)

x87 = np.arange(33, 35.01, 0.01)
y87 = 0 * x87 + 1
plt.plot(x87, y87, 'b', linewidth=2)

x88 = np.arange(33, 35.01, 0.01)
y88 = 0 * x88 + 3.5
plt.plot(x88, y88, 'b', linewidth=2)

y89 = np.arange(1, 3.51, 0.01)
x89 = 0 * y89 + 33
plt.plot(x89, y89, 'b', linewidth=2)

x90 = np.arange(36, 38.01, 0.01)
y90 = 0 * x90 + 3.5
plt.plot(x90, y90, 'b', linewidth=2)

x91 = np.arange(36, 38.01, 0.01)
y91 = 0 * x91 + 1
plt.plot(x91, y91, 'b', linewidth=2)

y92 = np.arange(1, 3.51, 0.01)
x92 = 0 * y92 + 36
plt.plot(x92, y92, 'b', linewidth=2)

y93 = np.arange(1, 3.51, 0.01)
x93 = 0 * y92 + 39
plt.plot(x93, y93, 'b', linewidth=2)

x94 = np.arange(39, 40.01, 0.01)
y94 = 0 * x94 + 1
plt.plot(x94, y94, 'b', linewidth=2)

x95 = np.arange(41, 42.01, 0.01)
y95 = 2.5 * x95 - 101.5
plt.plot(x95, y95, 'b', linewidth=2)

x96 = np.arange(42, 43.01, 0.01)
y96 = -2.5 * x96 + 108.5
plt.plot(x96, y96, 'b', linewidth=2)

y97 = np.arange(1, 3.51, 0.01)
x97 = 0 * y97 + 38
plt.plot(x97, y97, 'b', linewidth=2)

x98 = np.arange(41.4, 42.61, 0.01)
y98 = 0 * x98 + 2.2
plt.plot(x98, y98, 'b', linewidth=2)

x99 = np.arange(44, 46.01, 0.01)
y99 = 0 * x99 + 3.5
plt.plot(x99, y99, 'b', linewidth=2)

x100 = np.arange(44, 46.01, 0.01)
y100 = 0 * x100 + 1
plt.plot(x100, y100, 'b', linewidth=2)

x101 = np.arange(44, 46.01, 0.01)
y101 = 0 * x101 + 2.3
plt.plot(x101, y101, 'b', linewidth=2)

y102 = np.arange(2.3, 3.51, 0.01)
x102 = 0 * y102 + 44
plt.plot(x102, y102, 'b', linewidth=2)

y103 = np.arange(1, 2.31, 0.01)
x103 = 0 * y103 + 46
plt.plot(x103, y103, 'b', linewidth=2)

x104 = np.arange(38, 39.01, 0.01)
y104 = 2.5 * x104 - 98.5
plt.plot(x104, y104, 'b', linewidth=2)

x105 = np.arange(39, 40.01, 0.01)
y105 = -2.5 * x105 + 96.5
plt.plot(x105, y105, 'b', linewidth=2)

x106 = np.arange(38.4, 39.61, 0.01)
y106 = 0 * x106 - 2.4
plt.plot(x106, y106, 'b', linewidth=2)

y107 = np.arange(-3.5, -0.99, 0.01)
x107 = 0 * y107 + 40.5
plt.plot(x107, y107, 'b', linewidth=2)

y108 = np.arange(-3.5, -0.99, 0.01)
x108 = 0 * y108 + 42
plt.plot(x108, y108, 'b', linewidth=2)

x109 = np.arange(40.5, 42.01, 0.01)
y109 = -1.7 * x109 + 67.9
plt.plot(x109, y109, 'b', linewidth=2)

y110 = np.arange(-3.5, -0.99, 0.01)
x110 = 0 * y110 + 42.5
plt.plot(x110, y110, 'b', linewidth=2)

y111 = np.arange(-3.5, -0.99, 0.01)
x111 = 0 * y111 + 44
plt.plot(x111, y111, 'b', linewidth=2)

y112 = np.arange(-3.7, -1.19, 0.01)
x112 = 0 * y112 + 44
plt.plot(x112, y112, 'b', linewidth=2)

x113 = np.arange(42.5, 44.01, 0.01)
y113 = -0.1 * x113 + 3.2
plt.plot(x113, y113, 'b', linewidth=2)

x114 = np.arange(42.5, 44.01, 0.01)
y114 = -0.1 * x114 + 0.8
plt.plot(x114, y114, 'b', linewidth=2)

y115 = np.arange(-3.5, -0.99, 0.01)
x115 = 0 * y115 + 44.5
plt.plot(x115, y115, 'b', linewidth=2)

x116 = np.arange(44.5, 46.51, 0.01)
y116 = 0 * x116 - 1
plt.plot(x116, y116, 'b', linewidth=2)

x117 = np.arange(44.5, 46.51, 0.01)
y117 = 0 * x117 - 2
plt.plot(x117, y117, 'b', linewidth=2)

x118 = np.arange(44.5, 46.51, 0.01)
y118 = -0.8 * x118 + 33.6
plt.plot(x118, y118, 'b', linewidth=2)

y120 = np.arange(-3.5, -0.99, 0.01)
x120 = 0 * y120 + 47
plt.plot(x120, y120, 'b', linewidth=2)

y121 = np.arange(-2.3, -0.99, 0.01)
x121 = 0 * y121 + 49
plt.plot(x121, y121, 'b', linewidth=2)

y122 = np.arange(-3.5, -2.29, 0.01)
x122 = 0 * y122 + 51
plt.plot(x122, y122, 'b', linewidth=2)

x123 = np.arange(47, 48.51, 0.01)
y123 = 0 * x123 - 1
plt.plot(x123, y123, 'b', linewidth=2)

x124 = np.arange(47, 48.01, 0.01)
y124 = 0 * x124 - 2.3
plt.plot(x124, y124, 'b', linewidth=2)

x125 = np.arange(47, 48.51, 0.01)
y125 = 0 * x125 - 3.5
plt.plot(x125, y125, 'b', linewidth=2)

x126 = np.arange(49, 51.01, 0.01)
y126 = 0 * x126 - 1
plt.plot(x126, y126, 'b', linewidth=2)

x127 = np.arange(49, 51.01, 0.01)
y127 = 0 * x127 - 2.3
plt.plot(x127, y127, 'b', linewidth=2)

x128 = np.arange(49, 51.01, 0.01)
y128 = 0 * x128 - 3.5
plt.plot(x128, y128, 'b', linewidth=2)

plt.show()
```

<h2>Punto 6</h2>
Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai,
Mazda, etc.), a través de Python.

```python

```