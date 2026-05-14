# 9. Write a menu driven program to read, display, add, and subtract two distances.

class Distances:
    def __init__(self):
        self.d1 = 0
        self.d2 = 0
        self.chosen_unit = 0

    def read(self):
        print('What unit are you working in?')
        units = ['1. inches', '2. feet', '3. yards', '4. miles', '5. meters', '6. centimeters', '7. millimeters', '8. kilometers']
        for unit in units:
            print(unit)
        self.chosen_unit = int(input('Enter a number to pick an option: '))
        
        print('\nEnter your values in numeric form i.e 0, 1, 2.5 etc.\n')
        distance1 = float(input("Enter the first distance: "))
        distance2 = float(input("Enter the second distance: "))

        self.d1 = distance1
        self.d2 = distance2

    def display(self):
        '''Displays the two distances you want to work with'''
        if self.chosen_unit == 1:
            print(f'\nFirst distance : {self.d1} inches\nSecond distance: {self.d2} inches\n')
        elif self.chosen_unit == 2:
            if self.d1 == 1 and self.d1 == 0:
                print(f'\nFirst distance : {self.d1} foot\nSecond distance: {self.d2} feet\n')
            elif self.d2 == 1 and self.d2 == 0:
                print(f'\nFirst distance : {self.d1} feet\nSecond distance: {self.d2} foot\n')
            elif self.d2 == 1 and self.d2 == 0 and self.d1 == 1 and self.d1 == 0:
                print(f'\nFirst distance : {self.d1} foot\nSecond distance: {self.d2} foot\n')
            else:
                print(f'\nFirst distance : {self.d1} feet\nSecond distance: {self.d2} feet\n')
        elif self.chosen_unit == 3:
            print(f'\nFirst distance : {self.d1} yards\nSecond distance: {self.d2} yards\n')
        elif self.chosen_unit == 4:
            print(f'\nFirst distance : {self.d1} miles\nSecond distance: {self.d2} miles\n')
        elif self.chosen_unit == 5:
            print(f'\nFirst distance : {self.d1} meters = {self.d1} meters {self.d1} centimeters\nSecond distance: {self.d2} meters = {self.d2} meters {self.d2} centimeters\n')
        elif self.chosen_unit == 6:
            print(f'\nFirst distance : {self.d1} centimeters = {self.d1} centimeters {self.d1} millimeters\nSecond distance: {self.d2} centimeters = {self.d2} centimeters {self.d2} millimeters\n')
        elif self.chosen_unit == 7:
            print(f'\nFirst distance : {self.d1} millimeters\nSecond distance: {self.d2} millimeters\n')
        elif self.chosen_unit == 8:
            print(f'\nFirst distance : {self.d1} kilometers = {self.d1} kilometers {self.d1} meters\nSecond distance: {self.d2} kilometers = {self.d2} kilometers {self.d2} meters\n')
        

    def add(self):
        result = self.d1 + self.d2

        if self.chosen_unit == 1:
            print(f'\n{self.d1} inches + {self.d2} inches = {result} inches\n')
        elif self.chosen_unit == 2:
            if self.d1 == 1 and self.d1 == 0:
                print(f'\n{self.d1} foot + {self.d2} feet = {result} feet\n')
            elif self.d2 == 1 and self.d2 == 0:
                print(f'\n{self.d1} feett + {self.d2} foot = {result} feet\n')
            elif self.d2 == 1 and self.d2 == 0 and self.d1 == 1 and self.d1 == 0:
                print(f'\n{self.d1} foot + {self.d2} foot = {result} feet\n')
            else:
                print(f'\n{self.d1} feet + {self.d2} feet = {result} feet\n')
        elif self.chosen_unit == 3:
            print(f'\n{self.d1} yards + {self.d2} yards = {result} yards\n')
        elif self.chosen_unit == 4:
            print(f'\n{self.d1} miles + {self.d2} miles = {result} miles\n')
        elif self.chosen_unit == 5:
            print(f'\n{self.d1} meters + {self.d2} meters = {result} meters\n')
        elif self.chosen_unit == 6:
            print(f'\n{self.d1} centimeters + {self.d2} centimeters\n')
        elif self.chosen_unit == 7:
            print(f'\n{self.d1} millimeters + {self.d2} millmeters = {result} millimeters\n')
        elif self.chosen_unit == 8:
            print(f'\n{self.d1} kilometers + {self.d2} kilometers = {result} kilometers\n')
        

    def subtract(self):
        result = self.d1 - self.d2

        if self.chosen_unit == 1:
            print(f'\n{self.d1} inches - {self.d2} inches = {result} inches\n')
        elif self.chosen_unit == 2:
            if self.d1 == 1 and self.d1 == 0:
                print(f'\n{self.d1} foot - {self.d2} feet = {result} feet\n')
            elif self.d2 == 1 and self.d2 == 0:
                print(f'\n{self.d1} feett - {self.d2} foot = {result} feet\n')
            elif self.d2 == 1 and self.d2 == 0 and self.d1 == 1 and self.d1 == 0:
                print(f'\n{self.d1} foot - {self.d2} foot = {result} feet\n')
            else:
                print(f'\n{self.d1} feet - {self.d2} feet = {result} feet\n')
        elif self.chosen_unit == 3:
            print(f'\n{self.d1} yards - {self.d2} yards = {result} yards\n')
        elif self.chosen_unit == 4:
            print(f'\n{self.d1} miles - {self.d2} miles = {result} miles\n')
        elif self.chosen_unit == 5:
            print(f'\n{self.d1} meters - {self.d2} meters = {result} meters s\n')
        elif self.chosen_unit == 6:
            print(f'\n{self.d1} centimeters - {self.d2} centimeters = {result} centimeters\n')
        elif self.chosen_unit == 7:
            print(f'\n{self.d1} millimeters - {self.d2} millmeters = {result} millimeters\n')
        elif self.chosen_unit == 8:
            print(f'\n{self.d1} kilometers - {self.d2} kilometers = {result} kilometers \n')
        

distances = Distances()

print('\nWelcome, this is a program that can perform the following actions on distances:')

while True:
        actions = ['0. Read (Enter your values here)','1. Display (Displays your distance)', '2. Add', '3. Subtract', '4. Exit']
        for action in actions:
            print(action)
        chosen_action = int(input('Enter a number to pick an option: '))


        if chosen_action == 0:
            distances.read()
        elif chosen_action == 1:
            distances.display()
        elif chosen_action == 2:
            distances.add()
        elif chosen_action == 3:
            distances.subtract()
        elif chosen_action == 4:
            print('Goodbye!')
            break
        else:
            print('False input')

