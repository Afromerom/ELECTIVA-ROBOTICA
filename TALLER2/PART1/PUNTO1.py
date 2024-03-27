import math

def cartesian_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)  # Radio en el plano xy
    theta = math.atan2(y, x)    # Ángulo azimutal en el plano xy
    z_cylindrical = z            # La coordenada z se mantiene igual en coordenadas cilíndricas
    return r, theta, z_cylindrical

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)  # Radio esférico
    theta = math.atan2(y, x)            # Ángulo azimutal en el plano xy
    phi = math.acos(z / r)              # Ángulo de elevación con respecto al eje z
    return r, theta, phi

# Usa las coordenadas rectangulares
x = 4
y = 5
z = 6

# Convertir a coordenadas cilíndricas
r_cylindrical, theta_cylindrical, z_cylindrical = cartesian_to_cylindrical(x, y, z)
print(f"\nCoordenadas Cilíndricas: r = {r_cylindrical}, θ = {theta_cylindrical}, z = {z_cylindrical}")

# Convertir a coordenadas esféricas
r_spherical, theta_spherical, phi_spherical = cartesian_to_spherical(x, y, z)
print(f"Coordenadas Esféricas: r = {r_spherical}, θ = {theta_spherical} rad, φ = {phi_spherical} rad")