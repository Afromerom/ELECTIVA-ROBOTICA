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
