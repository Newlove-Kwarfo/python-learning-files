# 8. Write a menu driven program to read, display, add and subtract two complex numbers.
import math

class ComplexNumbers:
    def __init__(self,):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def read(self):
        num1_real = int(input("Enter the real part of the first number: "))
        num1_complex = int(input("Enter the imaginary part of the first number: "))
        num2_real = int(input("Enter the real part of the second number: "))
        num2_complex = int(input("Enter the imaginary part of the second number: "))

        self.a = num1_real
        self.b = num1_complex
        self.c = num2_real
        self.d = num2_complex

    def display(self):
        '''Displays the two numbers you want to work with'''
        print(f'\nFirst complex number : {self.a} + {self.b}i\nSecond complex number: {self.c} + {self.d}i\n')

    def add(self):
        real_result = self.a + self.c
        complex_result = self.b + self.d
        print(f'\n({self.a} + {self.b}i) + ({self.c} + {self.d}i) = ({real_result} + {complex_result}i)\n')

    def subtract(self):
        real_result = self.a - self.c
        complex_result = self.b - self.d
        print(f'\n({self.a} + {self.b}i) - ({self.c} + {self.d}i) = ({real_result} + {complex_result}i)\n')
              
# number1 = input('Enter your fist number here: ')
# number2 = input('Enter your second number here: ')
# numbers = ComplexNumbers(int(number1[0]),int(number1[2]),int(number2[0]),int(number2[2]))

numbers = ComplexNumbers()

print('\nWelcome, this is a program that can perform the following actions on complex numbers:')

# actions = ['1. Display (Displays your number)', '2. Add', '3. Subtract', '4. Exit']
# for action in actions:
#     print(action)
# chosen_action = int(input('Enter a number to pick an option: '))

# while chosen_action !=4:
#         if chosen_action == 1:
#             numbers.display()
#             chosen_action = 6
#         elif chosen_action == 2:
#             numbers.add()
#             chosen_action = 6
#         elif chosen_action == 3:
#             numbers.subtract()
#             chosen_action = 6
#         elif chosen_action == 6:
#             for action in actions:
#                 print(action)
#             chosen_action = int(input('Enter a number to pick an option: '))

while True:
        actions = ['0. Read (Enter your values here)','1. Display (Displays your number)', '2. Add', '3. Subtract', '4. Exit']
        for action in actions:
            print(action)
        chosen_action = int(input('Enter a number to pick an option: '))


        if chosen_action == 0:
            numbers.read()
        elif chosen_action == 1:
            numbers.display()
        elif chosen_action == 2:
            numbers.add()
        elif chosen_action == 3:
            numbers.subtract()
        elif chosen_action == 4:
            print('Goodbye!')
            break
        else:
            print('False input')

