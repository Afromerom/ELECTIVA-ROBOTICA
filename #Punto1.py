import matplotlib.pyplot as plt
import numpy as np

# Función para convertir resistencia a temperatura para PT100
def resistance_to_temperature(resistance):
    # Coeficientes de la ecuación de Callendar-Van Dusen para PT100
    A, B, C = 3.9083e-3, -5.775e-7, -4.183e-12
    
    # R0 es la resistencia a 0°C para PT100 (100 ohmios)
    R0 = 100.0
    
    # Calcular temperatura en grados Celsius
    temperature = (-R0 * A + np.sqrt(R0**2 * A**2 - 4 * R0 * B * (R0 - resistance))) / (2 * R0 * B)
    
    return temperature

# Rango de temperaturas de -200°C a 200°C
temperatures = np.linspace(-200, 200, 400)
# Calcular resistencia correspondiente a cada temperatura
resistances = 100.0 * (1 + temperatures * 3.9083e-3 + temperatures**2 * (-5.775e-7) + temperatures**3 * (-4.183e-12))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(temperatures, resistances, label='Comportamiento de PT100')
plt.title('Comportamiento de PT100 en el rango de -200°C a 200°C')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohmios)')
plt.legend()
plt.grid(True)
plt.show()