# --- SIngle rider ---

rider1_age = int(input('Age of Rider 1: '))
rider1_height = float(input('Height of Rider 1: '))

rider2_inq = input('Is there a second Rider (Yes/No?) ').capitalize()

if rider2_inq == 'No':
    if rider1_age >= 18 and rider1_height >= 62:
        ride_approval = True
    else:
        ride_approval = False

# --- 2 Riders ---

elif rider2_inq == 'Yes':
    rider2_age = int(input('Age of Rider 2: '))
    rider2_height = float(input('Height of Rider 2: '))
    if ((rider1_height >= 36 and rider2_height >= 36) and (rider1_age >= 18 or rider2_age >= 18)) or ((rider1_age >= 12 and rider2_age >= 12) and (rider1_height >= 52 and rider2_height >= 52)) or ((rider1_age >= 14 and rider2_age >= 16) or (rider1_age >= 16 and rider2_age >= 14) and (rider1_height >= 36 and rider2_height >= 36)):
        ride_approval = True
    else:
        ride_approval = False

if ride_approval:
    print ('Enjoy the ride and be safe!')
if not ride_approval:
    print ('Sorry, you are not eligible for this ride.')
