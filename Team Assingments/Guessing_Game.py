# --- Core Requirements ---

# -- Step 1 --
# magic_number = int(input('What is the magic number? '))
# guess = int(input('What is your guess? '))
# if guess < magic_number:
#     print ('Higher')
# elif guess == magic_number:
#     print ('You Guessed Correctly!')
# else:
#     print ("Lower")

# -- Step 2 --
# magic_number = int(input('What is the magic number? '))
# guess = int(input('What is your guess? '))
# while guess < magic_number:
#     print ('Higher')
#     guess = int(input('What is your guess? '))
#     while guess > magic_number:
#         print ('Lower')
#         guess = int(input('What is your guess? '))
# if guess == magic_number:
#     print ('You Guessed Correctly!')

# -- Step 3 --
import random

# magic_number = random.randint(1,100)
# print (magic_number)
# guess = int(input('What is your guess? '))

# while guess < magic_number:
#     print ('Higher')
#     guess = int(input('What is your guess? '))
#     while guess > magic_number:
#         print ('Lower')
#         guess = int(input('What is your guess? '))
# if guess == magic_number:
#     print ('You Guessed Correctly!')    

# --- Stretch Challenge ---

# -- Step 2 --
# magic_number = random.randint(1,100)
# print (magic_number)
# guess = int(input('What is your guess? '))
# guess_amount = 0
# while guess != magic_number:
#     if guess < magic_number:
#         print ('Higher')
#         guess = int(input('Guess again: '))
#     else:
#         print ('Lower')
#         guess = int(input('Guess again? '))
#     guess_amount += 1
# print ('You Guessed Correctly! Well Done!')
# print (f'Incorrect Guesses Made: {guess_amount}')

# -- Step 3 --
new_attempt = 'Yes'
while new_attempt == 'Yes':
    magic_number = random.randint(1,100)
    print (magic_number)
    guess_amount = 0
    while True:
        guess = int(input('Guess the number: '))
        guess_amount += 1
        if guess < magic_number:
            print ('Higher')
        elif guess > magic_number:
            print ('Lower')
        else:
            print ('You Guessed Correctly! Well Done!')
            break
    print (f'Guesses Made: {guess_amount}')
    new_attempt = input('Would you like to play again (Yes/No)? ').capitalize()
print ('Thank you for playing!')