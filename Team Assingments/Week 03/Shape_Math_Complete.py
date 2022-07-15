import math

# --- Square ---
# -- Area --
square_radius = float(input('Length of Side of Square/Cirle Radius (cm): '))
print ()
Square_area_cm2 = math.pow(square_radius, 2)
Square_area_m2 = math.pow(square_radius, 2) / 10_000
print (f'Area of Square in cm\u00b2 = {Square_area_cm2}')
print (f'Area of Square in m\u00b2 = {Square_area_m2}')
print ()
# -- Volume of Cube --
cube_volume_cm3 = math.pow(square_radius, 3)
cube_volume_m3 = math.pow(square_radius, 3) / 1_000_000
print(f'Volume of Cube in cm\u00b3 = {cube_volume_cm3:.1e}')
print(f'Volume of Cube in 9m\u00b3 = {cube_volume_m3:.1e}')
print ()

# --- Circle ---
# -- Area --
# circle_radius = float(input('Radius of Circle: '))
circle_area_cm2 = math.pi * math.pow(square_radius, 2)
circle_area_m2 = (math.pi * math.pow(square_radius, 2)) / 10_000
print (f'Area of Circle in cm\u00b2 = {circle_area_cm2:.5f}')
print (f'Area of Circle in m\u00b2 = {circle_area_m2:.5f}')
print ()
# -- Volume of Sphere --
sphere_volume_cm3 = 4/3 * (math.pi * math.pow(square_radius, 3))
sphere_volume_m3 = (4/3 * (math.pi * math.pow(square_radius, 3))) / 1_000_000
print (f'Volume of Sphere in cm\u00b3 = {sphere_volume_cm3:.5f}')
print (f'Volume of Sphere in m\u00b3 = {sphere_volume_m3:.5f}')
print ()

# --- Rectangle ---
# -- Area --
rect_length = float(input('Length of Rectangle: (cm) '))
rect_breadth = float(input('Breadth of Rectangle: (cm) '))
print ()
rectangle_area_cm2 = rect_length * rect_breadth
rectangle_area_m2 = (rect_length * rect_breadth) / 10_000
print (f'Area of Rectangle in cm\u00b2 = {rectangle_area_cm2}')
print (f'Area of Rectangle in m\u00b2 = {rectangle_area_m2}')
print ()
#  -- Volume of Prism --
prism_height = float(input('Height of Prism (cm): '))
prism_volume_cm3 = rectangle_area_cm2 * prism_height
prism_volume_m3 = (rectangle_area_m2 * prism_height) / 100
print (f'Volume of prism in cm\u00b3 = {prism_volume_cm3:.1e}')
print (f'Volume of prism in m\u00b3 = {prism_volume_m3:.1e}')
print ()