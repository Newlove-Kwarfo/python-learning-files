# 7. Write a menu driven program to read, display, simplify, add, and subtract two fractions.
from math import gcd

class Fractions:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def read(self):
        try:
            fraction1 = input('Enter the first fraction: ')
            fraction2 = input('Enter the second faction: ')
            f1_num, f1_den = map(int, fraction1.split('/'))
            f2_num, f2_den = map(int, fraction2.split('/'))
        except ValueError:
            print('Error! Input your fractions in the from "a/b" where a and b are integers')
            fraction1 = input('Enter the first fraction: ')
            fraction2 = input('Enter the second faction: ')
            f1_num, f1_den = map(int, fraction1.split('/'))
            f2_num, f2_den = map(int, fraction2.split('/'))

        self.a = f1_num
        self.b = f1_den
        self.c = f2_num
        self.d = f2_den        

    def display(self):
        '''Displays the two fractions you want to work with'''
        print(f'\nFirst fraction : {self.a}/{self.b}\nSecond fraction: {self.c}/{self.d}\n')


    def simplify(self):
        f1_num = self.a//gcd(self.a, self.b)
        f1_den = self.b//gcd(self.a, self.b)
        f2_num = self.c//gcd(self.c, self.d)
        f2_den = self.d//gcd(self.c, self.d)
        if f1_num == f1_den:
            fraction1_simple = f'{f1_num}/{f1_den} = {f1_num}'
        else:
            fraction1_simple = f'{f1_num}/{f1_den}'
        if f2_num == f2_den:
            fraction2_simple = f'{f2_num}/{f2_den} = {f2_num}'
        else:
            fraction2_simple = f'{f2_num}/{f2_den}'
        return f'\nFirst fraction :{self.a}/{self.b} simplifies to {fraction1_simple} \nSecond fraction: {self.c}/{self.d} simplifies to {fraction2_simple}\n'

    def add(self):
        denominator = (self.d*self.b)
        numerator = (self.d*self.a) + (self.b*self.c)
        numerator_simple = numerator//gcd(numerator, denominator)
        denominator_simple = denominator//gcd(numerator, denominator)
        if numerator == numerator_simple and denominator == denominator_simple:
            if numerator_simple == denominator_simple:
                print(f'\n{self.a}/{self.b} + {self.c}/{self.d} = {numerator}/{denominator} = {numerator}\n')
            else:
                print(f'\n{self.a}/{self.b} + {self.c}/{self.d} = {numerator}/{denominator}\n')
        else:
            if numerator_simple == denominator_simple:
                print(f'\n{self.a}/{self.b} + {self.c}/{self.d} = {numerator}/{denominator} = {numerator_simple}/{denominator_simple} = {numerator_simple}\n')
            else:
                print(f'\n{self.a}/{self.b} + {self.c}/{self.d} = {numerator}/{denominator} = {numerator_simple}/{denominator_simple}\n')

    def subtract(self):
        denominator = (self.d*self.b)
        numerator = (self.d*self.a) - (self.b*self.c)
        numerator_simple = numerator//gcd(numerator, denominator)
        denominator_simple = denominator//gcd(numerator, denominator)
        if numerator == numerator_simple and denominator == denominator_simple:
            if numerator_simple == denominator_simple:
                print(f'\n{self.a}/{self.b} - {self.c}/{self.d} = {numerator}/{denominator} = {numerator}\n')
            else:
                print(f'\n{self.a}/{self.b} - {self.c}/{self.d} = {numerator}/{denominator}\n')
        else:
            if numerator_simple == denominator_simple:
                print(f'\n{self.a}/{self.b} - {self.c}/{self.d} = {numerator}/{denominator} = {numerator}\n')
            else:
                print(f'\n{self.a}/{self.b} - {self.c}/{self.d} = {numerator}/{denominator}\n')
                
fractions = Fractions()
print('\nWelcome, this is a program that can perform the following actions on fractions:')

while True:
        actions = ['0. Read (Enter your fraction)','1. Display (Displays your fraction)', '2. Simplify', '3. Add', '4. Subtract', '5. Exit',]
        for action in actions:
            print(action)
        chosen_action = int(input('Enter a number to pick an option: '))

        if chosen_action == 0:
            fractions.read()
        elif chosen_action == 1:
            fractions.display()
        elif chosen_action == 2:
            print(fractions.simplify())
        elif chosen_action == 3:
            fractions.add()
        elif chosen_action == 4:
            fractions.subtract()
        elif chosen_action == 5:
            print('Goodbye!\n')
            break
        else:
            print('Invalid entry\n')

