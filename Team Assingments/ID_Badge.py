# output = '{:{}}''{:^{}}' '{:>{}}' .format('Python', 1, 'Software', 30, 'Engineering', 1)
# print (output)
# print ('{:} {:^30} {:>} '.format('Python', 'Software', 'Engineering'))
# print ('{:} {:^30} {:>} '.format('L', 'x', 'R'))

# print ('{:=^30}'.format('ID Card'))


# ---Basic Assigment---
print ('Please input the following:')
print ()
Last_name = input ('Last Name: ')
First_name = input ('First Name: ')
Email = input ('Email Address: ')
Phone = input ('Phone Number: ')
Job = input ('Job Title: ')
ID = input ('ID Number: ')
# Stretch Challenge
Hair_Colour =input ('Hair Colour: ')
Eye_Colour =input ('Eye Colour: ')
Month = input ('Starting Month: ')
Training = input('Training: ')
print ()
print('\033[96m{:=^50} \033[0m'.format(' ID Card '))
ID_Card = f'{Last_name.upper()}, {First_name.capitalize()}\n{Job.title()}\nID: {ID}\n\n{Email.lower()}\n{Phone}'
print ('\033[93m' + ID_Card + '\033[0m')
print ()
print ('\033[93mHair: {:25} Eyes: {}\nMonth: {:24} Training {} \033[0m'.format(Hair_Colour.capitalize(), Eye_Colour.capitalize(), Month.capitalize(), Training.capitalize()))
print ('\033[96m{:=^50}\033[0m'.format(''))

# print (f'Hair: {Hair_Colour.capitalize():25} Eyes: {Eye_Colour.capitalize()}\nMonth: {Month.capitalize():24} Training: {Training.capitalize()}')
# if Question == 'Y' or 'y':
#     print ('Training: Yes')
# elif Question == 'N' or 'n':
#     print ('Training: No')
# else:
#     print ('please enter yes(Y) or no(N)')