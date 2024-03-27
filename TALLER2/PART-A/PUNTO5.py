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
