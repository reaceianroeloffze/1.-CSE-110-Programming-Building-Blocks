import math

# --- Given Quantities ---
m = float(input('Mass (kg): '))
g = float(input('Gravitational Acceleration (m/s\u00b2) 9.8 for Earth. 24 for Jupiter: '))
t = float(input('time (s): '))
p = float(input('Fluid Density (kg/m\u00b3) 1.3 in air, 1000 in water: '))
# A = float(input('Cross-sectional Area (m\u00b2): '))
A = math.pi * math.pow(0.15,2)
C = float(input('Drag Constant: '))
c = (1/2) * p * C * A
print (f'c = {c:.3f}')
#  v = ?

# --- Formula ---
v = math.sqrt(m*g/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))
print (f' Velocity after {t} seconds = {v:.3f} m/s')