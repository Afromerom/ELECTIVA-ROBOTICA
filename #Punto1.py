import numpy as np

def pt100_resistencia_superior(temperatura):
    
    R0 = 100.0  # Resistencia nominal a 0°C para la PT100
    A = 3.9083e-3
    B = -5.775e-7
    # Ecuación superior de la PT100: R(T) = R0 * (1 + A * T + B * T^2)
    resistencia_superior = R0 * (1 + A * temperatura + B * temperatura**2)
    return resistencia_superior

def pt100_resistencia_inferior(temperatura):
    R0 = 100.0  # Resistencia nominal a 0°C para la PT100
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12
    # Ecuación inferior de la PT100: R(T) = R0 * (1 + A * T + B * T^2)
    resistencia_inferior = R0 * (1 + A * temperatura + B * temperatura**2 + C * (temperatura- 100) * temperatura**3)
    return resistencia_inferior
temperatura =50

print("El valor de la resistencia RTD de platino (PT100) a", pt100_resistencia_superior(temperatura),"ohmios")
