# # --- Core requirements ---
# # -- 01: --
# # - Creating Lists for bank acccounts and balances -
# from statistics import mean


# bank_accounts = []
# account_balances = []

# # - Creating a looping input for the name of the bank account and the balance -
# account_name = ''

# while account_name != 'Quit':
#     account_name = input('Please enter the name of your account: ').title()
#     if account_name != 'Quit':
#         balance_in_account = float(input("Please enter this account's balance: R"))
#         bank_accounts.append(account_name)
#         account_balances.append(balance_in_account)
# print ()

# # -- 02: Looping through the lists using an index and printing names andbalances next to each other --
# print ('Account Information:')

# for i in range(len(bank_accounts)):
#     accounts = bank_accounts[i]
#     balances = account_balances[i]
#     print (f'{i}. {accounts} - R{balances:.2f}')
# print ()

# # -- 03: Computing and printing the total and average of all balances --
# balance_total = sum(account_balances)
# balance_average = balance_total / len(account_balances)
# print (f'Total balance across all accounts: R{balance_total:.2f}')
# print (f'Balance Average: R{balance_average:.2f}')
# # OR
# import statistics
# balance_average = mean(account_balances)
# print (f'Balance Average: R{balance_average:.2f}')

# # --- Stretch Challenge ---
# # -- 01: Displaying the the account name with the highest balance and the balance itself --
# max_balance = ''
# max_name = ''
# for i in range(len(bank_accounts)):
#     accounts = bank_accounts[i]
#     balances = account_balances[i]
    
#     if 

# print (f'Highest balance: - {max_balance}')

# # -- 02: Asking the user to update an account --
# acc_update = 'yes'

# while acc_update == 'yes':
#     acc_update = input('Would you like to update an account? ').capitalize()
    
#     if acc_update == 'yes':
#         acc_index = int(input('Which Account would you like to update? '))
#         new_amount = float(input('What is the now amount? R'))
    
#         account_balances[acc_index] = new_amount
    
#     print('Account Information:')
#     for i in range(len(bank_accounts)):
#         print (f'{i}. {accounts} - R{balances[i]}')

accounts = []
balances = []

acc_name = ''

while acc_name != 'Quit':
    acc_name = input('Name your account: ').title()
    
    if acc_name != 'Quit':
        acc_balance = float(input('What is your balance: R'))
        accounts.append(acc_name)
        balances.append(acc_balance)
    
print ()
print ('Account Info:')

for i in range(len(accounts)):
    acc = accounts[i]
    acc_bal = balances[i]
    print (f'{i}. {acc} - R{acc_bal:.2f}')

print ()
    
balance_total = sum(balances)
balance_avg = balance_total / len(accounts)
print (f'Total: R{balance_total:.2f}\nAverage: R{balance_avg:.2f}')

import statistics

balance_avg = statistics.mean(balances)
print (f'Average: R{balance_avg:.2f}')

max_name = None
max_balance = -1

for i in range(len(accounts)):
    acc = accounts[i]
    acc_bal = balances[i]

    if acc_bal > max_balance:
        max_balance = acc_bal
        max_name = acc

print (f'Max Balance: {max_name} - {max_balance}')

acc_update = ''

while acc_update != 'no':
    acc_update = input('Would you like to update an account? ').capitalize()
    
    if acc_update != 'no':
        acc_index = int(input('Which Account would you like to update? '))
        new_amount = float(input('What is the now amount? R'))
    
        balances[acc_index] = new_amount
    
    print('Account Information:')
    for i in range(len(accounts)):
        print (f'{i}. {accounts[i]} - R{balances[i]}')