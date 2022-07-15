import math

# --- Square ---
length_radius = float(input('Length of Square & Circle Radius (cm): '))
# -- Area of Square --
square_area_cm2 = math.pow(length_radius, 2)
square_area_m2 = math.pow(length_radius, 2) / 10_000
print (f'Area of Square in cm\u00b2 = {square_area_cm2}')
print (f'Area of Square in m\u00b2 = {square_area_m2:.2e}')
# -- Volume of a Cube --
cube_volume_cm3 = math.pow(length_radius, 3)
cube_volume_m3 = math.pow(length_radius, 3) / 1_000_000
print (f'Volume of Cube in cm\u00b3 = {cube_volume_cm3}')
print (f'Volume of Cube in m\u00b3 = {cube_volume_m3:.4e}')
print()
# --- Circle ---
# radius = float(input('Radius of Circle (cm): '))
# -- Area of Circle --
circle_area_cm2 = math.pi * math.pow(length_radius, 2)
circle_area_m2 = math.pi * math.pow(length_radius, 2) / 10_000
print (f'Area of Circle in cm\u00b2 = {circle_area_cm2:4f}')
print (f'Area of Circle in m\u00b2 = {circle_area_m2:.4e}')
#  -- Volume of Sphere --
sphere_volume_cm3 = 4/3 * (math.pi * math.pow(length_radius, 3))
sphere_volume_m3 = (4/3 * (math.pi * math.pow(length_radius, 3))) / 1_000_000
print (f'Volume Of Sphere in cm\u00b3 = {sphere_volume_cm3:.4f}')
print (f'Volume Of Sphere in m\u00b3 = {sphere_volume_m3:.4e}')
print()

# --- Rectangle ---
rectangle_length = float(input('Length of Rectangle (cm): '))
rectangle_breadth = float(input('Breadth of Rectangle (cm): '))
# -- Area of Rectangle --
rectangle_area_cm2 = rectangle_length * rectangle_breadth
rectangle_area_m2 = (rectangle_length * rectangle_breadth) / 10_000
print (f'Area of Rectangle in cm\u00b2 = {rectangle_area_cm2}')
print (f'Area of Rectangle in m\u00b2 = {rectangle_area_m2:.1e}')
# -- Volume of Prism --
prism_height = float(input('Height of Prism (cm): '))
prism_volume_cm3 = rectangle_area_cm2 * prism_height
prism_volume_m3 = (rectangle_area_m2 * prism_height) / 100
print (f'Volume of Prism in cm\u00b3 = {prism_volume_cm3}')
print (f'Volume of Prism in m\u00b3 = {prism_volume_m3:.2e}')
print ()