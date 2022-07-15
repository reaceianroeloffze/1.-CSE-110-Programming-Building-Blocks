import math

# Function to determine Wind Chill based on a given value for temperature and wind speed:
def obtain_wind_chill(T, V):
    return 35.74 + 0.6215*T - 35.75*(pow(V, 0.16)) + 0.4275*T*(pow(V, 0.16))

# Function to convert °C to Degrees °F:
def obtain_celsius_in_fahrenheit(C):
    return C * (9/5) + 32

# Function to convert Kelvin to °F:
def obtain_kelvin_in_fahrenheit(K):
    return (K - 273.15) * (9/5) + 32

T = float(input('Please Enter Temperature: '))

while T:
    f_c_k = input('Fahrenheit, Kelvin or Celsius (°F/K/°C)? ').capitalize()

    if f_c_k in ('°F', 'F', 'Fahrenheit'):
        break
    elif f_c_k in ('°C', 'C', 'Celsius'):
        T = obtain_celsius_in_fahrenheit(T)
        break
    elif f_c_k in ('K', ' Kelvin'):
        T = obtain_kelvin_in_fahrenheit(T)
        break
    else:
        print('\nInvalid Input\n')

for V in range(5, 65, 5):
    print (f'\033[37;1mAt temperature \033[32;1m{T:.1f}\033[37;1m°F, with wind speed \033[34;1m{V}\033[37;1m mph, wind chill = \033[36;1m{obtain_wind_chill(T, V):.2f}\033[37;1m°F\033[0m')