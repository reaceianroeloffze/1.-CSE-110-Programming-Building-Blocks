import math

multiple = int(input('Please choose number: '))

Largest = math.pow(multiple, 2)

range_size = multiple + 1

digits = int(math.log10(Largest)) + 1

for row in range (1, range_size):
    for column in range(1, range_size):
        print (f'{column * row:{digits}}', end=' ')
    print ()