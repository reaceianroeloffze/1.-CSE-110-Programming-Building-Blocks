print ("\033[37;1mWelcome to RI's online shopping cart! We sell everything you could possibly think of!\033[0m")
print ()

# --- 02. Create Lists ---
menu_items = []
item_prices = [] # --- 01. Create list to display prices ---

# --- 01 Create Looping Menu ---
while True:
    print ('\033[37;1m Main Menu:\n\n1. Add Item\n2. View Cart\n3. Remove Item\n4. Compute Total\n5. Quit\033[0m')
    print ()
    menu_choice = input('\033[37;1mPlease choose an option: \033[0m').title()
    
    # --- 03 Allow Items to be added to the list ---
    if menu_choice in ('Add Item', 'Add', '1.', '1'):
        item = input ('What item would you like to add? type "\033[35;1mx\033[0m" to return to main menu: ').capitalize()
        if item != 'X':
            price = float(input(f'What is the price of \033[36;1m{item}\033[0m? $')) # --- 02. Ask for Prices of items ---
            print (f'\n\033[36;1m{item}\033[0m added to cart.\n')

            while item:
                menu_items.append(item)
                break

            while price:
                item_prices.append(price)
                break

            more_items = ''

            while more_items != 'X':
                more_items = input ('Would you like to add another item? ').capitalize()
                if more_items != "X":
                    price_more = float(input(f'What is the price of \033[36;1m{more_items}\033[0m? $')) # --- 02. Ask for Prices of items ---
                    print (f'\n\033[36;1m{more_items}\033[0m added to cart\n')

                    while more_items:
                        menu_items.append(more_items)
                        break

                    while price_more:
                        item_prices.append(price_more)
                        break

                else:
                    print ()
                    print ('\033[37;1mReturning to Main Menu\033[0m')
        else:
            print ()
            print ('\033[37;1mReturning to Main Menu\033[0m')

    # --- 04 Display Items in List ---
    elif menu_choice in ('View Cart', 'View', '2.', '2'):
        print()
        print ('\033[33;1mItems in Cart:\033[0m')
        print ()
        
        for i in range(len(menu_items)):
            item = menu_items[i]
            price = item_prices[i]
            print (f'\033[37;1m{i + 1}. {item} - ${price:.2f}\033[0m') # --- 03 & 04. Display index number, items and prices together. --- 06. Display prices to 2 decimal places --- Displays numbered list from 1 ---
            
        print ()
        print ('\033[37;1mReturning to Main Menu\033[0m')
        
    # --- 07 & 08: Removing items from stored list ---
    elif menu_choice in ('Remove Item', '3.', '3'):
        print ()
        print ('\033[33;1mCurrent Items in Cart:\033[0m')
        print ()
        
        for i in range(len(menu_items)):
            item = menu_items[i]
            price = item_prices[i]
            print (f'\033[37;1m{i + 1}. {item} - ${price:.2f}\033[0m ') # --- Displays numbered list from 1 --- 06. Display prices to 2 decimal places ---
        print ()
            
        remove_item = int(input('Which Item would you like to remove? Type "\033[35;1m0\033[0m" when you are done removing items: '))
        
        if remove_item != 0:
            if remove_item <= len(menu_items): # --- Condition to remove items within list boundaries ---
                menu_items.pop(remove_item - 1) # --- item names removed and 0-based index set ---
                item_prices.pop(remove_item - 1) # --- prices removed and 0-based index set ---
                # --- Can remove both first and last items in list ---
                print ('\033[30;1mItem successfully removed.\033[0m')
            else:
                print ()
                print ('\033[31;1mInvalid Option\033[0m') # --- If input value exceeds length of list ---
                        
            while remove_item != 0:
                print ()
                print ('\033[33;1mCurrent Items in Cart:\033[0m')
                print ()
                
                for i in range(len(menu_items)):
                    item = menu_items[i]
                    price = item_prices[i]
                    print (f'\033[37;1m{i + 1}. {item} - ${price:.2f}\033[0m ') # --- Displays numbered list from 1 --- 06. Display prices to 2 decimal places ---
                print ()
                
                remove_item = int(input('Would you like to remove another item? '))
                
                if remove_item != 0:
                    if remove_item <= len(menu_items): # --- Condition to remove items within list boundaries ---
                        menu_items.pop(remove_item - 1) # --- item names removed and 0-based index set ---
                        item_prices.pop(remove_item - 1) # --- prices removed and 0-based index set ---
                        # --- Can remove both first and last items in list ---
                        print ('\033[30;1mItem successfully removed.\033[0m')
                    else:
                        print ()
                        print ('\033[31;1mInvalid Option\033[0m') # --- If input value exceeds length of list ---
            else:
                print ()
                print ('\033[37;1mReturning to Main Menu\033[0m')
        else:
            print ()
            print ('\033[37;1mReturning to Main Menu\033[0m')

    # --- 05. Compute and display total price amount of all items ---
    elif menu_choice in ('Compute total', '4.', '4'):
        print(f'\nTotal cost of all items: \033[35;1m${sum(item_prices):.2f}\033[0m') # --- 06. Display prices to 2 decimal places ---
        
        checkout = ''
        
        while True:
            checkout = input('would you like to checkout (Yes/No)? ').capitalize()
            if checkout == 'Yes' or checkout == 'No':
                break
            print()
            print ('\033[31;1mInvalid Option\033[0m')
            print ()
            
        if checkout == 'Yes':
            print()
            print ('\033[33;1mItems purchased:\033[0m')
            print ()

            for i in range(len(menu_items)):
                item = menu_items[i]
                price = item_prices[i]
                print (f'\033[37;1m{i + 1}. {item} for ${price:.2f}\033[0m') # --- 06. Display prices to 2 decimal places ---

            print ()
            print ('\033[32;1mThank you for your purchase!\033[0m')
            print ()
            print ('\033[37;1mReturning to Main Menu\033[0m')
        elif checkout == 'No':
            print ()
            print ('\033[37;1mReturning to Main Menu\033[0m')
                    
    elif menu_choice in ('Quit', '5.', '5'):
        break
    else:
        print ()
        print ('\033[31;1mInvalid Option\033[0m')
    print ()
    
print ('Thank you for shopping with us! Please come again!')
print ()