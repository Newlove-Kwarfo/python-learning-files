def toMetersConverter(distance, distance_unit):
    """
    Docstring for toMetersConverter

    :param distance: float - distance converting from in original unit
    :param distance_unit: int - of unit of the distance converting from

    Converts inputted distance to meters for further convertion
    """
    #storing meter value
    if distance_unit == 1:
        meter_distance = distance
        unit = "meters"

    #kilometers to meters convertion
    elif distance_unit == 2:
        meter_distance = distance * 1000
        unit = "kilometers"

    #miles to meters convertion
    elif distance_unit == 3:
        meter_distance = distance * 1609.344
        unit = "miles"

    #feet to meters convertion
    elif distance_unit == 4:
        meter_distance = distance * 0.3048
        unit = "feet"

    #inches to meters convertion
    elif distance_unit == 5:
        meter_distance = distance * 0.0254
        unit = "inches"

    return meter_distance, unit


def fromMetersConverter(distance, meter_distance, unit, new_distance_unit, dp_choice_dist ):
    """
    Docstring for fromMetersConverter
    
    :param distance: float - distance converting from in original unit
    :param meter_distance: float - value in meters of distance converting from
    :param unit: int - unit of the distance converting from
    :param new_distance_unit: int - of unit of the distance converting to
    :param dp_choice_dist: int - decimal placed of answer

    
    Converts inputted distance (convertrd to meters) to final unit chosen

    """

    #meters to meters convertion
    if new_distance_unit == 1:
        new_distance = meter_distance
        print(f'\nRESULT: {distance} {unit} = {round(new_distance, dp_choice_dist)} meters (rounded to {dp_choice_dist}dp)')

    #meters to kilometers convertion
    elif new_distance_unit == 2:
        new_distance = meter_distance / 1000
        print(f'\nRESULT: {distance} {unit} = {round(new_distance, dp_choice_dist)} kilometers (rounded to {dp_choice_dist}dp)')

    #meters to miles convertion
    elif new_distance_unit == 3:
        new_distance = meter_distance / 1609.34
        print(f'\nRESULT: {distance} {unit} = {round(new_distance, dp_choice_dist)} miles (rounded to {dp_choice_dist}dp)')

    #meters to feet convertion
    elif new_distance_unit == 4:
        new_distance = meter_distance / 0.3048
        print(f'\nRESULT: {distance} {unit} = {round(new_distance, dp_choice_dist)} feet (rounded to {dp_choice_dist}dp)')

    #meters to inches convertion
    elif new_distance_unit == 5:
        new_distance = meter_distance / 0.0254
        print(f'\nRESULT: {distance} {unit} = {round(new_distance, dp_choice_dist)} inches (rounded to {dp_choice_dist}dp)')



# Welcome statement and conversion choice selection
print('\nHello! Welcome to the Engineering Unit Converter!')

while True:
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
            print(f'\nRESULT: {temperature} Fahrenheit = {round(new_temperature, dp_choice_temp)} Celsius (rounded to {dp_choice_temp}dp)')

        # Ceclius to Farenheit convertion
        elif type_choice_temp == 2:
            new_temperature = (temperature * 9/5) + 32
            print(f'\nRESULT: {temperature} Celsius = {round(new_temperature, dp_choice_temp)} Fahrenheit (rounded to {dp_choice_temp}dp)')


    # DISTANCE CONVERTER
    elif conversion_choice == 2:
        #Print out units available to be converterted to and from
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
            while True:
                try:
                    distance = float(input("Enter distance: "))
                    if distance >= 0:
                        break
                    else: 
                        print("Error! Negative value given for distance!")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            #convert distance to meters
            meter_distance, unit = toMetersConverter(distance, distance_unit)
            #conver from meters to desired unit
            fromMetersConverter(distance, meter_distance, unit, new_distance_unit, dp_choice_dist)


    #Takes in input for user to either close program or run it again
    print('\nWould you like to exit the program?')
    print('YES/NO')
    exit_choice = input('Enter your choice here: ').strip().lower()

    while exit_choice not in [ 'yes', 'y', 'no', 'n']:
        print('\nInvalid input! Enter a  from the  choices provided.')
        exit_choice = input('YES/NO: ')

    if exit_choice in [ 'yes', 'y']:
        break
    elif exit_choice in ['no','n']:
        continue