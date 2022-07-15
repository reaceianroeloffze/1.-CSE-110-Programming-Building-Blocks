# Create List:
numbers = []

# Create variable to be used in while loop:
entered_number = ''

# Loop through inputs until user types '0':
while entered_number != 0:
    entered_number = int(input('Please enter a number: '))
    if entered_number != 0:
        numbers.append(entered_number)
print ()
        
# Core Requirement 01: Printing the sum of all input numbers (adding them all up):
print (f'Total Sum of All Numbers in List = {sum(numbers)}')

# Core Requirement 02: Printing the Average (the sum of all numbers in the list / the amount of numbers in the list):
# Method 01: Calculate manually:
# list_average = sum(numbers) / len(numbers)
# print (f'List Average = {list_average}')

# OR

# Method 02: Calculate automatically using function from the Python Statistics Library:
import statistics

print (f'List Average = {statistics.mean(numbers)}')

# Core Requirement 03: Printing the Largest number in the list:
print (f'Largest number in List = {max(numbers)}')

# Stretch Challenge 01: Inputing Negative numbers and obtaining the Smallest positive number:
print (f'Smallest Positive Number in List = {min(n for n in numbers if n > 0)}')
print ()

# Stretch Challenge 02: Sorting the list and displaying the sorted list:
numbers.sort()
print ('Sorted list:')

for i in numbers:
    print (i)
    