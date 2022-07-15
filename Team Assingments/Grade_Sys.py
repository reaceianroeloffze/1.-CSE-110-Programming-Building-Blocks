# --- Team Assignment: Determining Pass Grade --- 

# -- Core assignment --

grade_percentage = float(input('What is your grade percentage (%)? '))

# if grade_percentage >= 90:
#     print ('Grade = A')
# if grade_percentage >= 80:
#     print ('Grade = B')
# if grade_percentage >= 70:
#     print ('Grade = C')
# if grade_percentage >= 60:
#     print ('Grade = D')
# else: 
#     grade_percentage < 60
#     print ('Grade = F')

if grade_percentage >= 90:
    letter = 'A'
elif grade_percentage >= 80:
    letter = 'B'
elif grade_percentage >= 70:
    letter = 'C'
elif grade_percentage >= 60:
    letter = 'D'
else:
    grade_percentage < 60 
    letter = 'F'

# -- Stretch Challenge --

last_digit = grade_percentage % 10

if last_digit >= 7 and letter in ('B', 'C', 'D'):
    sign = '+'
elif last_digit < 3 and letter in ('A', 'B', 'C', 'D'):
    sign = '-'
else:
    sign = ''
print (f'Grade = {letter}{sign}')


if grade_percentage >= 70:
    print ('Congratulations on passing! Well done!')
else:
    print ('You now know more than you did when you first started. Give it another go and passing is much more in reach this time.')