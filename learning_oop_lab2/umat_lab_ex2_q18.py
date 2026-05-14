# 18. Write a menu driven program to read, add, and subtract two polynomials.
class Polynomials:
    def __init__(self):
        self.p1_x2 = 0
        self.p1_x = 0
        self.p1_c = 0
        self.p2_x2 = 0
        self.p2_x = 0
        self.p2_c = 0

    def read(self):
        print(f'\nEnter your coefficients from the coefficient of the highest order variable\n to lowest order in the form a,b,c.  Example: 2,0,4.5')
        polynomial1 = input('\nEnter the coefficients of your first polynomial: ')
        polynomial2 = input('\nEnter the coefficients of your second polynomial: ')

        p1x2, p1x, p1c = map(float, polynomial1.split(','))
        p2x2, p2x, p2c = map(float, polynomial2.split(','))

        self.p1_x2 = p1x2
        self.p1_x = p1x
        self.p1_c = p1c
        self.p2_x2 = p2x2
        self.p2_x = p2x
        self.p2_c = p2c

    def add(self):
        x2_result = self.p1_x2 + self.p2_x2
        x_result = self.p1_x + self.p2_x
        c_result = self.p1_c + self.p2_c

        print(f'\nThe sum of the two plynomials is: {x2_result}x^2 + {x_result}x + {c_result}')

    def subtract(self):
        x2_result = self.p1_x2 - self.p2_x2
        x_result = self.p1_x - self.p2_x
        c_result = self.p1_c - self.p2_c

        print(f'\nThe difference of the two plynomials is: {x2_result}x^2 + {x_result}x + {c_result}')

polynomial = Polynomials()

print('\nWelcome! This program can perform the following actions on two polynomials:\n')

while True:
    actions =  ['0. Read(Enter your polynomials here)', '1. Add', '2. Subtract', '3. Exit']
    for action in actions:
        print(action)
    chosen_action = int(input('Enter the number of an option here to select it: '))

    if chosen_action == 0:
        polynomial.read()
    elif chosen_action == 1:
        polynomial.add()
    elif chosen_action == 2:
        polynomial.subtract()
    elif chosen_action == 3:
        print('Goodbye')
        break
    else:
        print('Invalid input')
    
