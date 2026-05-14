# Welcome statement and conversion choice selection
print('\nHello! Welcome to the Engineering Unit Converter!')


print('\nChoose your conversion type:')
print('1. Temperature\n2. Distance')

#Validates that conversion choice is a number in the choices given
while True:    
    try:
        conversion_choice = int(input('Please input the number next to your desired choice: '))
        if conversion_choice in [1,2]:
            break
        else: 
            print('\nInvalid input! Enter a number from the choices provided. i.e 1 or 2')
    except ValueError:
            print("Invalid input! Please enter a number.")
   
# TEMPERATURE CONVERTER
if conversion_choice == 1:
    print('\nWhich type of temperature conversion are you doing?')
    print('1. Fahrenheit to Celsius \n2. Celsius to Fahrenheit')

    #Validates that type of temperature conversion choice is a number in the choices given before allowing user to move on
    while True: 
        try:
            type_choice_temp = int(input('Please input the number next to your desired choice: '))
            if type_choice_temp in [1,2]:
                break
            else: 
                print('\nInvalid input! Enter a number from the choices provided. i.e 1 or 2')
        except ValueError:
            print("Invalid input! Please enter a number.")

    #Takes in and validates the number of decimal places to round answer to  before allowing user to move on
    #Max decimal place is 15 because the precision of float is 15
    print('\nHow many decimal places do you want your answer rounded to?')
    while True:
        try:
            #dp_choice_temp refers to decimal point choice for temperature
            dp_choice_temp = int(input('Please input the number of decimal places (max 15): '))
            dp_choice_temp = max(0, min(dp_choice_temp, 15))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    #Validates that temperature value is a number in the choices given before allowing user to move on
    while True:
        try:
            temperature = float(input('\nEnter the temperature value: '))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")            

    #Fahrenheit to Celcius convertion
    if type_choice_temp == 1:
        new_temperature = ((temperature - 32) * 5) / 9
        print(f'\nRESULT: {temperature} Fahrenheit = {round(new_temperature, dp_choice_temp)} Celsius ({dp_choice_temp}dp)')

    # Ceclius to Farenheit convertion
    elif type_choice_temp == 2:
        new_temperature = (temperature * 9/5) + 32
        print(f'\nRESULT: {temperature} Celsius = {round(new_temperature, dp_choice_temp)} Fahrenheit ({dp_choice_temp}dp)')


# DISTANCE CONVERTER
elif conversion_choice == 2:

    #Print out units available to be converterted to and from
    print('\nAvailable Units for conversion to and from:')
    units = ['meters (m)', 'kilometers (km)', 'miles (mi)', 'feet (ft)', 'inches (in)']

    for i, unit in enumerate(units, start = 1):
            print(f'{i}. {unit}')

    #Takes in unit user is converting from
    # And validates that it is a number in the choices given before allowing user to move on
    print('\nWhich unit are you converting FROM?: ')
    while True:
        try:
            distance_unit = int(input('Please input the number next to your desired choice: '))
            if distance_unit in range(1,6):
                break
            else: 
                print('\nInvalid input! Please input the number NEXT to your desired choice: ')
        except ValueError:
            print("Invalid input! Please enter a number.")

    #Takes in unit user is converting to
    # And validates that it is a number in the choices given before allowing user to move on
    print('\nWhich unit are you converting TO?: ')
    while True:
        try:
            new_distance_unit = int(input('Please input the number next to your desired choice: '))
            if new_distance_unit in range(1,6):
                break
            else: 
                print('\nInvalid input! Please input the number NEXT to your desired choice: ')
        except ValueError:
            print("Invalid input! Please enter a number.")

    #Takes in and validates the number of decimal places to round answer to  before allowing user to move on
    #Max decimal place is 15 because the precision of float is 15
    print('\nHow many decimal places do you want your answer rounded to?')
    while True:
        try:
            dp_choice_dist = int(input('Please input the number of decimal places  (max 15): '))
            dp_choice_dist = max(0, min(dp_choice_dist, 15))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
     
    #Checks if the conversion selection is the same unit
    if distance_unit == new_distance_unit:
        print("\nYou selected the same units. No conversion needed!")

    else:
        #Validates that distance value is a positive number before allowing user to move o
        while True:
            try:
                distance = float(input("Enter distance: "))
                if distance >= 0:
                    break
                else: 
                    print("Error! Negative value given for distance!")
            except ValueError:
                print("Invalid input! Please enter a number.")


            # METERS CONVERSIONS

            #meters to kilometers convertion
            if distance_unit == 1 and new_distance_unit == 2:
                new_distance = distance / 1000
                print(f'\nRESULT: {distance} meters = {round(new_distance, dp_choice_dist)} kilometers ({dp_choice_dist}dp)')

            #meters to miles convertion
            elif distance_unit == 1 and new_distance_unit == 3:
                new_distance = distance / 1609.34
                print(f'\nRESULT: {distance} meters = {round(new_distance, dp_choice_dist)} miles ({dp_choice_dist}dp)')

            #meters to feet convertion
            elif distance_unit == 1 and new_distance_unit == 4:
                new_distance = distance / 0.3048
                print(f'\nRESULT: {distance} meters = {round(new_distance, dp_choice_dist)} feet ({dp_choice_dist}dp)')

            #meters to inches convertion
            elif distance_unit == 1 and new_distance_unit == 5:
                new_distance = distance / 0.0254
                print(f'\nRESULT: {distance} meters = {round(new_distance, dp_choice_dist)} inches ({dp_choice_dist}dp)')


            # KILOMETERS CONVERSIONS

            #kilometers to meters convertion
            elif distance_unit == 2 and new_distance_unit == 1:
                new_distance = distance * 1000
                print(f'\nRESULT: {distance} kilometers = {round(new_distance, dp_choice_dist)} meters ({dp_choice_dist}dp)')

            #kilometers to miles convertion
            elif distance_unit == 2 and new_distance_unit == 3:
                new_distance = distance * 0.621371
                print(f'\nRESULT: {distance} kilometers = {round(new_distance, dp_choice_dist)} miles ({dp_choice_dist}dp)')

            #kilometers to feet convertion
            elif distance_unit == 2 and new_distance_unit == 4:
                new_distance = distance * 3280.84
                print(f'\nRESULT: {distance} kilometers = {round(new_distance, dp_choice_dist)} feet ({dp_choice_dist}dp)')

            #kilometers to inches convertion
            elif distance_unit == 2 and new_distance_unit == 5:
                new_distance = distance * 39370.08
                print(f'\nRESULT: {distance} kilometers = {round(new_distance, dp_choice_dist)} inches ({dp_choice_dist}dp)')


            # MILES CONVERSIONS

            #miles to meters convertion
            elif distance_unit == 3 and new_distance_unit == 1:
                new_distance = distance * 1609.344
                print(f'\nRESULT: {distance} miles = {round(new_distance, dp_choice_dist)} meters ({dp_choice_dist}dp)')

            #miles to kilometers convertion
            elif distance_unit == 3 and new_distance_unit == 2:
                new_distance = distance * 1.609344
                print(f'\nRESULT: {distance} miles = {round(new_distance, dp_choice_dist)} kilometers ({dp_choice_dist}dp)')

            #miles to feet convertion
            elif distance_unit == 3 and new_distance_unit == 4:
                new_distance = distance * 5280
                print(f'\nRESULT: {distance} miles = {round(new_distance, dp_choice_dist)} feet ({dp_choice_dist}dp)')

            #miles to inches convertion
            elif distance_unit == 3 and new_distance_unit == 5:
                new_distance = distance * 63360
                print(f'\nRESULT: {distance} miles = {round(new_distance, dp_choice_dist)} inches ({dp_choice_dist}dp)')


            # FEET CONVERSIONS
            
            #feet to meters convertion
            elif distance_unit == 4 and new_distance_unit == 1:
                new_distance = distance * 0.3048
                print(f'\nRESULT: {distance} feet = {round(new_distance, dp_choice_dist)} meters ({dp_choice_dist}dp)')

            #feet to kilometers convertion
            elif distance_unit == 4 and new_distance_unit == 2:
                new_distance = distance * 0.0003048
                print(f'\nRESULT: {distance} feet = {round(new_distance, dp_choice_dist)} kilometers ({dp_choice_dist}dp)')

            #feet to miles convertion
            elif distance_unit == 4 and new_distance_unit == 3:
                new_distance = distance * 0.000189
                print(f'\nRESULT: {distance} feet = {round(new_distance, dp_choice_dist)} miles ({dp_choice_dist}dp)')

            #feet to inches convertion
            elif distance_unit == 4 and new_distance_unit == 5:
                new_distance = distance * 12
                print(f'\nRESULT: {distance} feet = {round(new_distance, dp_choice_dist)} inches ({dp_choice_dist}dp)')


            # INCHES CONVERSIONS

            #inches to meters convertion
            elif distance_unit == 5 and new_distance_unit == 1:
                new_distance = distance * 0.0254
                print(f'\nRESULT: {distance} inches = {round(new_distance, dp_choice_dist)} meters ({dp_choice_dist}dp)')

            #inches to kilometers convertion
            elif distance_unit == 5 and new_distance_unit == 2:
                new_distance = distance * 0.0000254
                print(f'\nRESULT: {distance} inches = {round(new_distance, dp_choice_dist)} kilometers ({dp_choice_dist}dp)')

            #inches to miles convertion
            elif distance_unit == 5 and new_distance_unit == 3:
                new_distance = distance * 0.0000157828
                print(f'\nRESULT: {distance} inches = {round(new_distance, dp_choice_dist)} miles ({dp_choice_dist}dp)')

            #inches to feet convertion
            elif distance_unit == 5 and new_distance_unit == 4:
                new_distance = distance / 12
                print(f'\nRESULT: {distance} inches = {round(new_distance, dp_choice_dist)} feet ({dp_choice_dist}dp)')