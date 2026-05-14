import math

#Assignment 1
# Write a program that accepts two numbers and finds their average

'''print('This program  accepts two numbers and finds their average')
number1=int(input('Enter the first number: '))
number2=int(input('Enter the second number: '))
result=(number1+number2)/2
print(f'The average of {number1} and {number2} is {result}')'''

#Assignment 2
#Write a program that accepts two numbers and displays
#the result of exponentiation and floor division
'''s program  accepts two numbers and displays the result of exponentiation and floor division')
number1=int(input('Enter the first number: '))
number2=int(input('Enter the second number: '))
exponent_result=(number1**number2)
floor_division_result= number1//number2
print(f'{number1} to the power {number2} is {exponent_result}')
print(f'The result of the floor division of {number1} and {number2} is {floor_division_result}')'''

#Assignment 3
#Write a program that accepts three numbers
#and finds (a + b) * c, and also the average of all three
'''a= int(input('Enter the first number: '))
b= int(input('Enter the second number: '))
c= int(input('Enter the third number: '))
result1= (a+b)*c
result2= (a+b+c)/3
print(f'({a} + {b}) times {c} is {result1}')
print(f'the average of {a}, {b} and {c} is {result2}')'''

#Assignment 4
# Write a program that calculates the square root of the sum of two numbers squared
'''a= int(input('Enter the first number: '))
b= int(input('Enter the second number: '))
result = math.sqrt(a**2 + b**2)
print(f'{a} squared plus {b} squared equals {result}')'''

#Assignment 5
# Write a program that calculates the roots of a quadratic equation ax² + bx + c = 0
'''print('This program calculates using the quadratic formula ax² + bx + c = 0')
a= int(input('Enter the first number (a): '))
b= int(input('Enter the first second (b): '))
c= int(input('Enter the first third (c): '))
discriminant = b**2-(4*a*c)
result1= (-b + discriminant)/(2*a)
result2= (-b - discriminant)/(2*a)
if result1 == result2 :
    print(f'the root of {a}x² + {b}x + {c} = 0 is {result1}')
else:
    print(f'the roots of {a}x² + {b}x + {c} = 0 is {result1} and {result2}')'''

#Assignment 6
# Write a program that calculates the area of a rectangle
'''print('This program calculates the area of a rectangle')
length = int(input('Enter the length of the rectangle: '))
width = int(input('Enter the width/breadth of the rectangle: '))
area = length * width
print(f'The area of a rectangle of length {length} and {width} is {area}')'''

#Assignment 7
# Write a program that calculates the area of a circle
'''print('This program calculates the area of a circle')
radius = int(input('Enter the radius of the circle: '))
area = round(math.pi*radius**2, 3)
print(f'The area of a circle of radius {radius} is {area}')'''

#Assignment 8
# Write a program that calculates the volume of a cylinder
print('This program calculates the volume of a cylinder')
radius = int(input('Enter the radius of a cylinder: '))
height = int(input('Enter the height of a cylinder: '))
area = round(math.pi*(radius**2)*height, 3)
print(f'The volume of a cylinder of radius {radius} and height {height} is {area}')