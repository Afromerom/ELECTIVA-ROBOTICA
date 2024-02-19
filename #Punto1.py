import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones de las rectas
def line(x, slope, intercept):
    return slope * x + intercept

# Crear arrays de datos para cada recta
x_values = np.arange(1, 38, 0.01)

# Rectas horizontales
y_values3 = line(x_values, 0, 3)
y_values4 = line(x_values, 0, 5)
y_values5 = line(x_values, 0, 6)
y_values6 = line(x_values, 0, 3.5)
y_values7 = line(x_values, 0, 2.3)
y_values8 = line(x_values, 0, 1)
y_values9 = line(x_values, 0, 3.5)
y_values10 = line(x_values, 0, 1)

# Rectas verticales
x_values11 = line(np.arange(1, 1.51, 0.01), 0, 8)
x_values12 = line(np.arange(1, 3.51, 0.01), 0, 9)
x_values13 = line(np.arange(1, 3.51, 0.01), 0, 10)
x_values14 = line(np.arange(11, 12.01, 0.01), 0, 0)
x_values15 = line(np.arange(12, 13.01, 0.01), 0, 0)
x_values16 = line(np.arange(11.4, 12.61, 0.01), 0, 0)
x_values17 = line(np.arange(14, 15.01, 0.01), 0, 0)
x_values18 = line(np.arange(15, 16.01, 0.01), 0, 0)
x_values19 = line(np.arange(17, 18.51, 0.01), 0, 0)
x_values20 = line(np.arange(19.5, 21.01, 0.01), 0, 0)
x_values21 = line(np.arange(22, 24.01, 0.01), 0, 0)
x_values22 = line(np.arange(25, 27.01, 0.01), 0, 0)
x_values23 = line(np.arange(28, 30.01, 0.01), 0, 0)
x_values24 = line(np.arange(30.5, 31.51, 0.01), 0, 0)
x_values25 = line(np.arange(32, 33.51, 0.01), 0, 0)
x_values26 = line(np.arange(34, 35.01, 0.01), 0, 0)
x_values27 = line(np.arange(35, 36.01, 0.01), 0, 0)
x_values28 = line(np.arange(34.43, 35.56, 0.01), 0, 0)

# Rectas inclinadas
y_values2 = line(x_values, -1.5, 8)
y_values14 = line(x_values, 2.5, -26.5)
y_values15 = line(x_values, -2.5, 33.5)
y_values18 = line(x_values, -1.5, 24.5)
y_values20 = line(x_values, 1.5, -20.5)
y_values26 = line(x_values, -1.7, 36.7)
y_values33 = line(x_values, 1.26, -30.5)
y_values68 = line(x_values, -1.5, 32)
y_values69 = line(x_values, 1.5, -37)
y_values77 = line(x_values, -1.7, 53.4)
y_values78 = line(x_values, 2.5, -88.5)
y_values79 = line(x_values, -2.5, 86.5)
y_values80 = line(x_values, 0, -2.4)

# Dibujar las rectas
plt.plot(x_values, y_values3, 'b', linewidth=3)
plt.plot(x_values, y_values4, 'b', linewidth=3)
plt.plot(x_values, y_values5, 'b', linewidth=3)
plt.plot(x_values, y_values6, 'b', linewidth=3)
plt.plot(x_values, y_values7, 'b', linewidth=3)
plt.plot(x_values, y_values8, 'b', linewidth=3)
plt.plot(x_values, y_values9, 'b', linewidth=3)
plt.plot(x_values, y_values10, 'b', linewidth=3)

plt.plot(x_values11, np.arange(1, 1.51, 0.01), 'b', linewidth=3)
plt.plot(x_values12, np.arange(1, 3.51, 0.01), 'b', linewidth=3)
plt.plot(x_values13, np.arange(1, 3.51, 0.01), 'b', linewidth=3)
plt.plot(x_values14, line(np.arange(11, 12.01, 0.01), 2.5, -26.5), 'b', linewidth=3)
plt.plot(x_values15, line(np.arange(12, 13.01, 0.01), -2.5, 33.5), 'b', linewidth=3)
plt.plot(x_values16, line(np.arange(11.4, 12.61, 0.01), 0, 2), 'b', linewidth=3)
plt.plot(x_values17, np.arange(1, 3.51, 0.01), 'b', linewidth=3)
plt.plot(x_values18, np.arange(1, 3.51, 0.01), 'b', linewidth=3)
plt.plot(x_values19, line(np.arange(14, 15.01, 0.01), -1.5, 24.5), 'b', linewidth=3)
plt.plot(x_values20, line(np.arange(15, 16.01, 0.01), 1.5, -20.5), 'b', linewidth=3)
plt.plot(x_values21, np.arange(1, 3.51, 0.01), 'b', linewidth=3)
plt.plot(x_values22, np.arange(1, 3.51, 0.01), 'b', linewidth=3)
plt.plot(x_values23, line(np.arange(17, 18.51, 0.01), 0, 1), 'b', linewidth=3)
plt.plot(x_values24, np.arange(1, 3.54, 0.01), 'b', linewidth=3)