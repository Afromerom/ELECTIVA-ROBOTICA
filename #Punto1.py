import cv2
import numpy as np
import matplotlib.pyplot as plt

# Función para obtener contornos a partir de una imagen
def obtener_contornos(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral para obtener una imagen binaria
    _, umbral = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

    # Encontrar contornos en la imagen binaria
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contornos

# Función para obtener coordenadas X y Y de los contornos
def obtener_coordenadas(contornos):
    coordenadas = []
    for contorno in contornos:
        for punto in contorno:
            x, y = punto[0]
            coordenadas.append((x, y))
    return coordenadas

# Cargar las imágenes
ruta_imagen1 = 'C:\\Users\\Pipe\\Desktop\\UNIVERSITY\\ROBOTICA\\logo1.jpg'
ruta_imagen2 = 'C:\\Users\\Pipe\\Desktop\\UNIVERSITY\\ROBOTICA\\logo2.jpg'
imagen1 = cv2.imread(ruta_imagen1)
imagen2 = cv2.imread(ruta_imagen2)

# Obtener contornos para ambas imágenes
contornos_imagen1 = obtener_contornos(imagen1.copy())
contornos_imagen2 = obtener_contornos(imagen2.copy())

# Obtener coordenadas de los contornos
coordenadas_imagen1 = obtener_coordenadas(contornos_imagen1)
coordenadas_imagen2 = obtener_coordenadas(contornos_imagen2)

# Imprimir coordenadas de la primera imagen
print("Coordenadas de los contornos en la primera imagen:")
for coord in coordenadas_imagen1:
    print(f"X: {coord[0]}, Y: {coord[1]}")

# Imprimir coordenadas de la segunda imagen
print("\nCoordenadas de los contornos en la segunda imagen:")
for coord in coordenadas_imagen2:
    print(f"X: {coord[0]}, Y: {coord[1]}")

# Crear gráficos 2D para ambas imágenes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Imagen 1
ax1.scatter(*zip(*coordenadas_imagen1), color='red', marker='o', label='Contornos')
ax1.imshow(cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB))
ax1.set_title('Chevrolet')
ax1.legend()

# Imagen 2
ax2.scatter(*zip(*coordenadas_imagen2), color='blue', marker='o', label='Contornos')
ax2.imshow(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))
ax2.set_title('Renault')
ax2.legend()

plt.show()