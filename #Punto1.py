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