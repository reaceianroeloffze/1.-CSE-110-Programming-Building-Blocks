# --- Single Rider ---

rider1_age = int(input('Age of Rider 1: '))
rider1_height = float(input('Height of Rider 1: '))

rider2_inq = input('Is there a second Rider (Yes/No?) ').capitalize()

if rider2_inq == 'No':
    if rider1_age >= 18 and rider1_height >= 62:
        ride_approved = True
    elif rider1_age >= 12 and rider1_age <= 17 and rider1_height >= 36:
        golden_passport = input('Do you have a Golden Passport (Yes/No)? ').capitalize()
        if golden_passport == 'Yes':
            rider1_age >= 18
            ride_approved = True
        else:
            ride_approved = False    
    else:
        ride_approved = False
    if ride_approved:
        print ('Enjoy the ride and be safe!')
    else:
        print('Sorry, you are not eligible for this ride.')

# --- 2 Riders ---

elif rider2_inq == 'Yes':
    rider2_age = int(input('Age of Rider 2: '))
    rider2_height = float(input('Height of Rider 2: '))
    if ((rider1_height >= 36 and rider2_height >= 36) and (rider1_age >= 18 or rider2_age >= 18)) or ((rider1_age >= 12 and rider2_age >= 12) and (rider1_height >= 52 and rider2_height >= 52)) or (rider1_age >= 14 and rider2_age >= 16 or rider1_age >= 16 and rider2_age >= 14):
        ride_approved = True
    elif (rider2_age >=12 and rider2_age <= 17) or (rider1_age <= 17 and rider1_age >= 12) and (rider1_height >= 36 and rider2_height >= 36):
        golden_passport = input('Do you have a Golden Passport (Yes/No)? ').capitalize()
        if golden_passport == 'Yes':
            # rider1_age >= 18 and rider2_age >= 18
            ride_approved = True
        else:
            ride_approved = False
    else:
        ride_approved = False

    if ride_approved:
        print ('Enjoy the ride and be safe! ')
    else:
        print('Sorry, you are not eligible for this ride.')


else:
    while rider2_inq != 'Yes' and rider2_inq != 'No':
        print ('Invalid response.')
        rider2_inq = input('Is there a second Rider (Yes/No? ').capitalize()
