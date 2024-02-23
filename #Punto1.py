import numpy as np
import matplotlib.pyplot as plt

def carga_descarga_RC(V, C, R, tiempo):
    tau = R * C  # Constante de tiempo del circuito RC
    voltajes = [V * (1 - np.exp(-t / tau)) for t in tiempo]
    return voltajes

def graficar_carga_descarga(tiempo, voltajes):
    plt.plot(tiempo, voltajes, label='Carga/Descarga')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Solicitar entrada al usuario
V = float(input("Ingrese el voltaje inicial (V): "))
C = float(input("Ingrese la capacitancia (F): "))
R = float(input("Ingrese la resistencia (ohmios): "))
tiempo = np.linspace(0, 5 * R * C, 1000)  # 1000 puntos en el intervalo de carga y descarga

# Calcular voltajes
voltajes = carga_descarga_RC(V, C, R, tiempo)

# Graficar
graficar_carga_descarga(tiempo, voltajes)