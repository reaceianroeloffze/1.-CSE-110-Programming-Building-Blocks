# --- User Input ---
child_price = float(input("Children's meal price: "))
child_price_with_dessert = float(input("Children's meal price with dessert: "))
adult_price = float(input('Adult meal price: '))
adult_price_with_dessert = float(input('Adult meal price with dessert: '))
drink_price = float(input('Drink Price: '))
child_number = int(input('Number of Children: '))
adult_number = int(input('Number of Adults: '))
sales_tax_rate = float(input('Sales Tax Rate: '))
print ()

# --- Subtotal Prices and Number of Adults and Children ---

# -- Meal --
child_price_total_meal =  child_price * child_number
adult_price_total_meal = adult_price * adult_number
child_adult_price_total_meal = child_price_total_meal + adult_price_total_meal

# -- With Drinks --
child_price_total_with_drinks = drink_price * child_number
adult_price_total_with_drinks = drink_price * adult_number
child_adult_price_total_with_drinks = child_price_total_with_drinks + adult_price_total_with_drinks

# -- Meals with Dessert --
child_price_with_dessert_total = child_price_with_dessert * child_number
adult_price_with_dessert_total = adult_price_with_dessert * adult_number
child_adult_dessert_price_total = child_price_with_dessert_total + adult_price_with_dessert_total

# -- Subtotals --
child_adult_subtotal_meal = child_adult_price_total_meal
print (f'\033[31;1mMeal Subtotal\033[0m: \033[33;1m${child_adult_price_total_meal:.2f}\033[0m')
child_adult_meal_drink_subtotal = child_adult_price_total_with_drinks + child_adult_price_total_meal
print (f'\033[33;1mMeal Subtotal with drinks\033[0m: \033[31;1m${child_adult_meal_drink_subtotal:.2f}\033[0m')
child_adult_subtotal_with_dessert = child_adult_dessert_price_total
print (f'\033[31;1mMeal Subtotal with dessert\033[0m: \033[33;1m${child_adult_dessert_price_total:.2f}\033[0m')

# -- Grand Subtotal --
grand_subtotal = child_adult_price_total_meal + child_adult_meal_drink_subtotal + child_adult_dessert_price_total
print (f'\033[32;1mGrand Subtotal\033[0m: \033[35;1m${grand_subtotal:.2f}\033[0m')
print ()

# --- Sales Tax ---
tax_total = grand_subtotal * sales_tax_rate / 100
print (f'\033[35;1mSales Tax\033[0m: \033[32;1m${tax_total:.2f}\033[0m')
print ()

# --- Total Prices ---
total_meal_price = child_adult_subtotal_meal + tax_total
print (f'\033[34;1mMeal Total\033[0m: \033[36;1m${total_meal_price:.2f}\033[0m')
total_price_with_drinks = child_adult_meal_drink_subtotal + tax_total
print (f'\033[36;1mTotal with drinks\033[0m: \033[34;1m${total_price_with_drinks:.2f}\033[0m')
total_price_with_dessert = child_adult_subtotal_with_dessert + tax_total
print (f'\033[34;1mTotal with dessert\033[0m: \033[36;1m${total_price_with_dessert:.2f}\033[0m')

# -- Grand Total --
grand_total = total_meal_price + total_price_with_drinks + total_price_with_dessert
print (f'\033[32;1mGrand Total\033[0m: \033[35;1m${grand_total:.2f}\033[0m')
print()

# --- Amount Paid, tip and change due ---
amount_paid = float(input('Amount Paid: '))
gratuity = int(input('Gratuity: '))
change = amount_paid - grand_total - gratuity
print (f'\033[37;1mChange due\033[0m: \033[30;1m${change:.2f}\033[0m')
