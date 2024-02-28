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