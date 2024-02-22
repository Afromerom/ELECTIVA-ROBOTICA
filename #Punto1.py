# Programa para calcular la resistencia RTD de platino (PT100) en función de la temperatura
import cmath
from math import pi, cosh, sinh
# Definimos la temperatura
B = math.radians (45)


def matx(B):
    matriz_xv = [[1, 0, 0],[0, cmath.cos(B), -cmath.sin(B)],[0, cmath.sin(B), cmath.cos(B)]]
    return matriz_xv


# Impresión de los resultados
print("La matriz sobre el eje x es: ", matx(B))