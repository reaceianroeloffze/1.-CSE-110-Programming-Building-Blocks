import math

# Function to determine the area of a square
def obtain_area_square(side):
    return obtain_area_rectangle(side, side)

# Function to determine the area of a rectangle
def obtain_area_rectangle(length, breadth):
    return length * breadth

# Function to determine the area of a circle
def obtain_area_circle(radius):
    return math.pi * pow(radius, 2)

# Function to determine area based on input
def obtain_area(shape, value1, value2=0):
    area = -1
    
    if shape == 'Square':
        area = obtain_area_square(value1)
    if shape == 'Rectangle':
        area = obtain_area_rectangle(value1, value2)
    if shape == 'Circle':
        area = obtain_area_circle(value1)
        
    return area

while True:
    shape = input('What shape do you have? ').capitalize()
    
    if shape == 'Square':
        square_side = float(input('Enter side of square: '))
        area = obtain_area(shape, square_side)
        print (f'Area of {shape} = {area} ')
    elif shape == 'Rectangle':
        length = float(input('Enter length of rectangle: '))
        breadth = float(input('Enter breadth of rectangle: '))
        area = obtain_area(shape, length, breadth)
        print (f'Area of {shape} = {area} ')
    elif shape == 'Circle':
        radius = float(input('Enter radius of circle: '))
        area = obtain_area(shape, radius)
        print (f'Area of {shape} = {area} ')
    elif shape == 'Quit':
        break
    else:
        print ('\nInvalid Input\n')


    
    
