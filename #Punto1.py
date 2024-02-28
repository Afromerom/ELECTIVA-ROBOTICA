import numpy as np
import matplotlib.pyplot as plt

# Ecuaciones para la resistencia de la PT100
def pt100_superior(T):
    R0 = 100.0  # Resistencia nominal a 0°C
    A = 3.9083e-3
    B = -5.775e-7
    return R0 * (1 + A * T + B * T**2)

def pt100_inferior(T):
    R0 = 100.0  # Resistencia nominal a 0°C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12
    return R0 * (1 + A * T + B * T**2 + C * (T- 100) * T**3)

# Rango de temperaturas
temperaturas = np.arange(-200, 201, 1)

# Calcular resistencias para las temperaturas dadas
resistencias_superior = pt100_superior(temperaturas)
resistencias_inferior = pt100_inferior(temperaturas)

# Crear una figura para la ecuación superior
plt.figure(1, figsize=(10, 6))
plt.plot(temperaturas, resistencias_superior, label='Ecuación Superior')
plt.title('Comportamiento de la PT100 - Ecuación Superior')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohmios)')
plt.legend()
plt.grid(True)

# Crear otra figura para la ecuación inferior
plt.figure(2, figsize=(10, 6))
plt.plot(temperaturas, resistencias_inferior, label='Ecuación Inferior')
plt.title('Comportamiento de la PT100 - Ecuación Inferior')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohmios)')
plt.legend()
plt.grid(True)

# Mostrar las dos ventanas de gráficos
plt.show()