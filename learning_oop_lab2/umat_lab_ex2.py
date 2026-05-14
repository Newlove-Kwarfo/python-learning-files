# 1. Write a program that has a class Point with attributes as the X and Y coordinates.
# Make two objects of this class and find the midpoint of both the points.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod  #This means it doesn't depend on any particular object — it just does a calculation.
    def midpoint(point1, point2):
        midpoint = (((point1.x + point2.x)/2),((point1.y + point2.y)/2))
        return midpoint
    
p1 = Point(2,3)
p2 = Point(4,8)
print(Point.midpoint(p1, p2))
"""

# 2. Write a program that has a class Cars. Create two objects and set car1 to be a
# red convertible with price ₵10 thousand and name Pugo, and car2 to be a blue
# sedan named Mavo worth ₵76 thousand.
"""
class Cars:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

car1 = Cars('Pugo', '₵10,000', 'Red Convertible')
car2= Cars('Mavo', '₵76,000', 'Blue Sedan')
"""

# 3. Write a program that uses a class attribute to define some default titles for faculty
# in a college. Display the name along with title and department of the college.
"""
class Faculty:
    titles = ['Mr.', 'Mrs.', 'Dr.', 'Prof']
    def __init__(self, name, department, title_index):
        self.name = name
        self.department = department
        self.title = Faculty.titles[title_index]

    def get_staff(self):
        return f'{self.title} {self.name} of the {self.department} department'
    
staff1 = Faculty('John Doe', 'CPEN', 0)
print(staff1.get_staff())

staff2 = Faculty('Elsie Koffman', 'Boimedical Engineering', 3)
print(staff2.get_staff())
"""

# 4. Add a method reflect_x to class Point, which returns a new point which is the
# reflection of the point about the x-axis. For example, Point (7, 8). reflect_x is
# Point (7, -8).
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflex_x(self):
        reflected_y = self.y - 2*(self.y)
        return f'{self.x}, {reflected_y}'
    
p1 = Point(2,5)
print(p1.reflex_x())
"""

# 5. Write a static method that checks whether all words in a list starts with a vowel.
"""
def vowel_start(list):
    vowels = ('a', 'e', 'i','o', 'u')
    for words in list:
        if not words.lower().startswith(vowels):
            return 'Not all the words in the list starts with a vowel'
    return 'All words in the list start with a vowel'

myList = ['girl', 'apple', 'orb']
print(vowel_start(myList))
"""

# 6. Make a class triangle. Enter its three sides and calculate its area.
"""
from math import sqrt

class Triangle:
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3

    def get_area(self):
        s = (self.a + self.b+ self.c)/2
        area = sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return f' Area = {area}'
    
triangle1= Triangle(4,5,6)
print(triangle1.get_area())
"""

#There may be a lot of problems in calculataion and bugs with somme of these menu driven codes

# 7. Write a menu driven program to read, display, simplify, add, and subtract two fractions.
"""
import umat_lab_ex2_q7
"""

# 8. Write a menu driven program to read, display, add and subtract two complex numbers.
"""
import umat_lab_ex2_q8
"""

# 9. Write a menu driven program to read, display, add, and subtract two distances.
"""
import umat_lab_ex2_q9

"""

# 10. Write a menu driven program to read, display, add, and subtract two time objects.
"""
import umat_lab_ex2_q10
"""

# 11. Write a menu driven program to read, display, add, and subtract two height objects.
"""
import umat_lab_ex2_q11
"""

# 12. Write a program to read two POINTS and calculate the distance between them.
"""
from math import sqrt

class Points():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance_between(self):
        '''Calculates the distance between two points'''
        distance = sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2))
        print(f'\nThe distance between ({self.x1} , {self.y1}) and ({self.x2} , {self.y2}) is {round(distance, 5)} units')

print('Welcome! This program takes two points/coordinates and calculates the distance between them\n')
point1 = input('Enter the first point: ')
point2 = input('Enter the second point: ')

x1, y1 = map(float, point1.split(','))
x2, y2 = map(float, point2.split(','))

points = Points(x1, y1, x2, y2)
points.distance_between()
"""

# 13. Write a class that has a list of integers as data members and read(),
# display(), find_largest(), find smallest(), sum(), and
# find_mean() as its member functions
"""
class Integers:
    def __init__(self):
        self.data_members = data_members = []

    def read(self):
        count = int(input('How many members do you want to enter?: '))
        for i in range(count):
            num = int(input('Enter an integer: '))
            self.data_members.append(num)

    def display(self):
        print(f'The numbers you inputed are: {self.data_members}')

    def find_largest(self):
        largest = max(self.data_members)
        print(f'The largest number entered is {largest}')

    def find_smallest(self):
        smallest = min(self.data_members)
        print(f'The smallest number entered is {smallest}')

    def sum(self):
        total = sum(self.data_members)
        print(f'The sum of the numbers entered is {total}')

    def mean(self):
        avg = (sum(self.data_members))/(len(self.data_members))
        print(f'The average of the numbers entered is {avg}')

numbers = Integers()
numbers.read()
numbers.display()
numbers.find_largest()
numbers.find_smallest()
numbers.sum()
numbers.mean()
"""

# 14.Make a class Book with members, title, author, publisher, and ISBN number. The
# functions of the class should read and display the data.
"""
class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.publisher = ''
        self.ISBN_number = ''

    def read(self):
        title = input('Enter the title of the book: ')
        author = input('Enter the author of the book: ')
        publisher = input('Enter the publisher of the book here: ')
        ISBN = input('Enter the ISBN number of the book: ')
        print('\n')

        self.title = title
        self.author = author
        self.publisher = publisher
        self.ISBN_number = ISBN

    def display(self):
        info = {'Title':self.title, 'Author':self.author, 'Publisher':self.publisher, 'ISBN':self.ISBN_number}
        for something in info:
            print(f'{something} of the book = {info[something]}')


book1 = Book()
book1.read()
book1.display()
"""

# 15. Write a program that swaps two members of a class.
"""
class Kelcy:
    def __init__(self, goldilost, locked_in):
        self.goldilost = goldilost
        self.locked_in = locked_in

    def swap(self):
        new_goldilost = self.goldilost
        new_locked_in = self.locked_in

        self.locked_in = new_goldilost
        self.goldilost = new_locked_in

fish = Kelcy('a', 'b')
print(fish.goldilost)
print(fish.locked_in)
fish.swap()
print(fish.goldilost)
print(fish.locked_in)

"""

# 16. Write a program to find mean of two numbers belonging to two different objects of
# the same class.
"""
def mean(num1, num2):
    avg = (num1.value + num2.value)/2
    print(f'The mean is {avg}')

class Numbers:
    def __init__(self, value):
        self.value = value

number1 = Numbers(2)
number2 = Numbers(4)
mean(number1, number2)

"""

# 17. Write a program that has a class student with data members-roll numbers and marks in
# three subjects. Make at least four objects of this class. Use one or more functions
# that finds total of each student and then sorts the student's records in descending
# order based on their marks.
"""
def rank(*args):
    new_args = sorted(args, key = lambda student: student.total(), reverse=True )
    for person in new_args:
        print(f'{person.roll} has a total mark of {person.total()}')

class Student:
    def __init__(self, roll_no, subject1, subject2, subject3, ):
        self.roll = roll_no
        self.sub1 = subject1
        self.sub2 = subject2
        self.sub3 = subject3

    def total(self):
        self.sum = self.sub1 + self.sub2 + self.sub3
        return self.sum

student1 = Student('00001', 23, 45, 67)
student2 = Student('00002', 35, 55, 74)
student3 = Student('00003', 67, 89, 98)
student4 = Student('00004', 89, 78, 85)

rank(student1, student2, student3, student4)

"""

# 18. Write a menu driven program to read, add, and subtract two polynomials.
"""
import umat_lab_ex2_q18
"""

# 19. Write a program that uses a time structure within a class. Enter any time and your
# favourite show's time. The program must display how much time is left for it to start.
"""
class Time:
    def __init__(self):
        self.h1 = 0
        self.m1 = 0
        self.h2 = 0
        self.m2 = 0

    def read(self):
        print('Enter your values in the form "1:00" ')
        time = input('Enter any time: ')
        show_time = input('Enter the time your favourite show begin: ')

        h1, m1 = map(int, time.split(':'))
        h2, m2 = map(int, show_time.split(':'))

        self.h1 = h1
        self.m1 = m1
        self.h2 = h2
        self.m2 = m2


    def difference(self):
        current_mins = (self.h1*60) + self.m1
        show_mins = (self.h2*60) + self.m2

        diff = show_mins - current_mins
        hours = diff // 60
        mins = diff % 60

        if diff == 0:
            print('Hurry! Your favourite show is starting right now!!😍')
        elif diff > 0:
            print(f'Your favourite show beigns in {hours} hour(s) {mins} minute(s)')
        else:
            diff = -diff
            hours = diff // 60
            mins = diff % 60
            print(f'Your favourite show began {hours} hours {mins} minutes ago')


time = Time()
time.read()
time.difference()

"""

# 20. Write a menu driven program to add or delete items from your inventory of
# stationary items. You can use a dictionary to store item and the brand.
"""
import umat_lab_ex2_q20

"""

# 21. Write a menu driven program to read, add, subtract, multiply, divide, and
# transpose two matrices.
"""
import umat_lab_ex2_q21
"""

# 22. Write a program that displays the details of a cricket player. The details must
# include his name, matched played, run rate, wickets taken, maiden overs, overs
# played, number of centuries, and half centuries, etc.
"""
import  umat_lab_ex2_q22
"""
