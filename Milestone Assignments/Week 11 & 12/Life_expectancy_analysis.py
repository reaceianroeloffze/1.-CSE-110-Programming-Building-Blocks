with open('life-expectancy.csv') as csv_file:

    csv_file.readline()

    # --- Variables & list for 'All' ---
    max_life_val = -1
    min_life_val = 9999999999999
    max_year = -1
    min_year = 999999999
    max_country = ''
    min_country = ''
    overall_expectancy_data = []

    # --- Variables & list for 'Year' ---
    int_year_max_val = -1
    int_year_min_val = 999999999999
    int_year_max_country = ''
    int_year_min_country = ''
    year_of_interest = ''
    year_expectancy_data = []

    # --- Variables & list for 'Code' ---
    int_code_max_val = -1
    int_code_min_val = 999999999999
    int_code_max_year = -1
    int_code_min_year = 99999999
    code_of_interest = ''
    code_expectancy_data = []

    while True:
        list_of_interest = input('Which set of data would you like to retrieve (All/Year/Country?) ').capitalize()

        if list_of_interest == 'All':
            print ('\nRetreiving all data\n')
            break

        elif list_of_interest == 'Year':
            year_of_interest = int(input("Which year's data would you like to retrieve? "))
            print ('\nRetreiving data\n')
            break

        elif list_of_interest == 'Country':
            code_of_interest = input("Which Country's data would you like to retrieve (type the code or the name of the country)? ")
            print ('\nRetreiving data\n')
            break

        else:
            print ('\n\033[34;1minput not recognised.\033[0m\n')

    for data in csv_file:
        data_split = data.split(',')
        country = data_split[0]
        code = data_split[1]
        year = int(data_split[2])
        life_expectancy = float(data_split[3])

        # --- Display everything ---
        if list_of_interest == 'All':
            print (f'\033[37;1mCountry: \033[31;1m{country}\033[0m | \033[37;1mCode: \033[33;1m{code}\033[0m | \033[37;1mYear: \033[35;1m{year}\033[0m | \033[37;1mLife Expecatancy: \033[32;1m{life_expectancy}\033[0m')

            overall_expectancy_data.append(life_expectancy)

            # --- Overall min & max values ---
            if life_expectancy > max_life_val:
                max_life_val = life_expectancy
                max_year = year
                max_country = country

            if life_expectancy < min_life_val:
                min_life_val = life_expectancy
                min_country = country
                min_year = year

            if year > max_year:
                max_year = year

            if year < min_year:
                min_year = year

        # --- Display data for selected year ---
        if list_of_interest == 'Year':

            if year == year_of_interest:
                print (f'\033[37;1mCountry: \033[31;1m{country}\033[0m | \033[37;1mCode: \033[33;1m{code}\033[0m | \033[37;1mYear: \033[35;1m{year}\033[0m | \033[37;1mLife Expecatancy: \033[32;1m{life_expectancy}\033[0m')

                year_expectancy_data.append(life_expectancy)

                # --- min & max values based on chosen year ---
                if life_expectancy > int_year_max_val:
                    int_year_max_val = life_expectancy
                    int_year_max_country = country

                if life_expectancy < int_year_min_val:
                    int_year_min_val = life_expectancy
                    int_year_min_country = country

        # --- Display data based on selected country code ---
        if list_of_interest == 'Country':

            # --- min & max values based on chosen code ---
            if code == code_of_interest.upper() or country == code_of_interest.title():
                print (f'\033[37;1mCountry: \033[31;1m{country}\033[0m | \033[37;1mCode: \033[33;1m{code}\033[0m | \033[37;1mYear: \033[35;1m{year}\033[0m | \033[37;1mLife Expecatancy: \033[32;1m{life_expectancy}\033[0m')

                code_expectancy_data.append(life_expectancy)

                if life_expectancy > int_code_max_val:
                    int_code_max_val = life_expectancy
                    int_code_max_year = year

                if life_expectancy < int_code_min_val:
                    int_code_min_val = life_expectancy
                    int_code_min_year = year

                if year > max_year:
                    max_year = year

                if year < min_year:
                    min_year = year

    # --- Expectancy average overall ---
    if len(overall_expectancy_data) > 0:

        overall_expectancy_average = sum(overall_expectancy_data) / len(overall_expectancy_data)

        # --- Overall max, min & average expectancy values ---
        print (f'\n\033[37;1mMax overall life expentancy: \033[32;1m{max_life_val}\033[0m \033[37;1min\033[0m \033[31;1m{max_country}\033[0m\033[37;1m, year\033[0m \033[35;1m{max_year}\033[0m \n\033[37;1mMin overall life expectancy: \033[32;1m{min_life_val}\033[0m \033[37;1min\033[0m \033[31;1m{min_country}\033[0m\033[37;1m, year\033[0m \033[35;1m{min_year}\n\033[37;1mAverage overall life expectancy in dataset: \033[32;1m{overall_expectancy_average:.3f} \033[0m')
        print (f'\n\033[37;1mEarliest record of life expectancy in this dataset: \033[35;1m{min_year}\n\033[37;1mLatest record of life expectancy in this dataset: \033[35;1m{max_year}\033[0m')

    # --- Expectancy average by year ---
    if len(year_expectancy_data) > 0:

        year_expectancy_average = sum(year_expectancy_data) / len(year_expectancy_data)

        # --- max, min & average expectancy values based on chosen year ---
        print (f'\n\033[37;1mFor year \033[35;1m{year_of_interest}\033[37;1m:\nMax life expectancy then: \033[32;1m{int_year_max_val} \033[37;1min \033[31;1m{int_year_max_country}\n\033[37;1mMin life expectancy then: \033[32;1m{int_year_min_val} \033[37;1min \033[31;1m{int_year_min_country}\n\033[37;1mAverage life expectancy in all countries then: \033[32;1m{year_expectancy_average:.3f}\033[0m')

    # --- Expectancy average by code/country ---
    if len(code_expectancy_data) > 0:

        code_expectancy_average = sum(code_expectancy_data) / len(code_expectancy_data)

        # --- max, min & average expectancy values based on chosen code ---
        print (f'\n\033[37;1mFor chosen code \033[33;1m{code_of_interest}\033[37;1m:\nMax life expectancy then: \033[32;1m{int_code_max_val} \033[37;1min \033[31;1m{int_code_max_year}\n\033[37;1mMin life expectancy then: \033[32;1m{int_code_min_val} \033[37;1min \033[31;1m{int_code_min_year}\n\033[37;1mAverage yearly life expectancy: \033[32;1m{code_expectancy_average:.3f}\033[0m')
        print (f'\n\033[37;1mEarliest record of life expectancy in this dataset: \033[35;1m{min_year}\n\033[37;1mLatest record of life expectancy in this dataset: \033[35;1m{max_year}\033[0m')
