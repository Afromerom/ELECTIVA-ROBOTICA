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

```