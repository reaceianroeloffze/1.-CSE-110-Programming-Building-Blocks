
with open('life-expectancy.csv') as file:
    next(file)
    # file.readline()
    
    search_year = int(input('Enter the year you would like to search: '))

    highest_year = -1
    lowest_year = 9999
    highest_expectancy = -1
    lowest_expectancy = 9999
    max_country = ''
    min_country = ''
    expectancies = []

    year_max_value = -1
    year_min_value = 9999
    year_max_country = -1
    year_min_country = 9999
    max_year = -1
    min_year = 9999
    year_list = []


    for line in file:

        # line = line.strip()
        
        parts = line.split(',')

        country = parts[0]
        country_code = parts[1]
        data_year = int(parts[2])
        life_expectancy = float(parts[3])

        expectancies.append(life_expectancy)

        if life_expectancy > highest_expectancy:
            highest_expectancy = life_expectancy
            highest_year = data_year
            max_country = country
        
        if life_expectancy < lowest_expectancy:
            lowest_expectancy = life_expectancy
            lowest_year = data_year
            min_country =  country

        if data_year == search_year:
            
            year_list.append(life_expectancy)

            if life_expectancy > year_max_value:
                year_max_value = life_expectancy
                max_year = data_year
                year_max_country = country
            
            if life_expectancy < year_min_value:
                year_min_value = life_expectancy
                min_year = data_year
                year_min_country =  country


    expectancy_average = sum(expectancies)/len(expectancies)
    print(f"The maximum expectancy is: {highest_expectancy} in the year: {highest_year}, in {max_country}")
    
    print(f"The minimum expectancy is: {lowest_expectancy} in the year: {lowest_year}, in {min_country}")

    print(f'The expectancy average is: {expectancy_average:.3f}')
    
    # if len(year_list) > 0:
    list_average = sum(year_list)/len(year_list)
    print(f'For the year: {search_year}')
    print(f'The average life expectancy across all countries was: {list_average:.3f}')
    print(f'The max life expectancy was in {year_max_country} with {year_max_value}')
    print(f'The min life expectancy was in {year_min_country} with {year_min_value}')
    



    
    
    
    
    

    


       