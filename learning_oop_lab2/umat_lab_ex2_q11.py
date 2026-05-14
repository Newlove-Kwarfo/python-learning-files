# 11. Write a menu driven program to read, display, add, and subtract two height objects.

class Heights:
    def __init__(self):
        self.h1 = 0
        self.h2 = 0

    def read(self):  
        print('What unit are you working in?')
        units = ['1. inches', '2. feet', '3. meters', '4. centimeters']
        for unit in units:
            print(unit)
        self.chosen_unit = int(input('Enter a number to pick an option: '))

        try:
            height1 = float(input("Enter the first height: "))
            height2 = float(input("Enter the second height: "))

        except ValueError:
            print('Enter your values in the form "a.bcd..." where a, b, c... are integers')
            height1 = float(input("Enter the first height: "))
            height2 = float(input("Enter the second height: "))

        self.h1 = height1
        self.h2 = height2

    def display(self):
        '''Displays the two heights you want to work with'''
        if self.chosen_unit == 1:
            print(f'\nFirst height : {self.h1} inches\nSecond height: {self.h2} inches\n')
        elif self.chosen_unit == 2:
            if self.h1 == 1 and self.h1 == 0:
                print(f'\nFirst height : {self.h1} foot\nSecond height: {self.h2} feet\n')
            elif self.h2 == 1 and self.h2 == 0:
                print(f'\nFirst height : {self.h1} feet\nSecond height: {self.h2} foot\n')
            elif self.h2 == 1 and self.h2 == 0 and self.h1 == 1 and self.h1 == 0:
                print(f'\nFirst height : {self.h1} foot\nSecond height: {self.h2} foot\n')
            else:
                print(f'\nFirst height : {self.h1} feet\nSecond height: {self.h2} feet\n')
        elif self.chosen_unit == 3:
            print(f'\nFirst height : {self.h1} meters \nSecond height: {self.h2} meters\n')
        elif self.chosen_unit == 4:
            print(f'\nFirst height : {self.h1} centimeters \nSecond height: {self.h2} centimeter\n')

    def add(self):
        result = self.h1 + self.h2

        if self.chosen_unit == 1:
            print(f'\n{self.h1} inches + {self.h2} inches = {result} inches\n')
        elif self.chosen_unit == 2:
            if self.h1 == 1 and self.h1 == 0:
                print(f'\n{self.h1} foot + {self.h2} feet = {result} feet\n')
            elif self.h2 == 1 and self.h2 == 0:
                print(f'\n{self.h1} feett + {self.h2} foot = {result} feet\n')
            elif self.h2 == 1 and self.h2 == 0 and self.h1 == 1 and self.h1 == 0:
                print(f'\n{self.h1} foot + {self.h2} foot = {result} feet\n')
            else:
                print(f'\n{self.h1} feet + {self.h2} feet = {result} feet\n')
        elif self.chosen_unit == 3:
            print(f'\n{self.h1} meters + {self.h2} meters = {result} meters\n')
        elif self.chosen_unit == 4:
            print(f'\n{self.h1} centimeters + {self.h2} centimeters = {result} centimeters\n')
        

    def subtract(self):
        result = self.h1 - self.h2

        if self.chosen_unit == 1:
            print(f'\n{self.h1} inches - {self.h2} inches = {result} inches\n')
        elif self.chosen_unit == 2:
            if self.h1 == 1 and self.h1 == 0:
                print(f'\n{self.h1} foot - {self.h2} feet = {result} feet\n')
            elif self.h2 == 1 and self.h2 == 0:
                print(f'\n{self.h1} feet - {self.h2} foot = {result} feet\n')
            elif self.h2 == 1 and self.h2 == 0 and self.h1 == 1 and self.h1 == 0:
                print(f'\n{self.h1} foot - {self.h2} foot = {result} feet\n')
            else:
                print(f'\n{self.h1} feet - {self.h2} feet = {result} feet\n')
        elif self.chosen_unit == 3:
            print(f'\n{self.h1} meters - {self.h2} meters = {result} meters =\n')
        elif self.chosen_unit == 4:
            print(f'\n{self.h1} centimeters - {self.h2} centimeters = {result} centimeters\n')

heights = Heights()

print('\nWelcome, this is a program that can perform the following actions on heights:')

while True:
        actions = ['0. Read  (Enter your value here)','1. Display (Displays your height)', '2. Add', '3. Subtract', '4. Exit']
        for action in actions:
            print(action)
        chosen_action = int(input('Enter a number to pick an option: '))


        if chosen_action == 0:
            heights.read()
        elif chosen_action == 1:
            heights.display()
        elif chosen_action == 2:
            heights.add()
        elif chosen_action == 3:
            heights.subtract()
        elif chosen_action == 4:
            print('Goodbye!')
            break
        else:
            print('False input')

