# INHERITANCE Programming Problems

# 1. Write an abstract class Vehicle. Derive three classes Car, Motorcycle and
# Truck from it. Define appropriate methods and print the details of the vehicle.
"""
class Vehicle:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
        pass

    def display(self):
        print(f'This {self.__class__.__name__} is a {self.color} {self.year} {self.brand}'.title())

class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year, color)
        super().display()

class Motorcycle(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year, color)
        super().display()

class Truck(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year, color)
        super().display()

my_car = Car('BMW', '2007', 'Black')
my_motor = Motorcycle('R-0710', '2010', 'Black')
my_truck = Truck('Truck-kun', '2000', 'Red')

"""

# 2. Define a class Employee. Display the personal and salary details of five
# employees using single inheritance.
"""
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age 
        self.position = position
        self.salary = salary
        self.info = {'Name': self.name, 'Age': self.age, 'Position': self.position, 'Salary': self.salary}

    def display(self):
        for key, value in self.info.items():
            print(f'{key} = {value}')
        print('\n')

class JuniorOfficer(Employee):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age, position, salary)
        super().display()
    
employee_1= JuniorOfficer('John',23,'J.O','2000')
employee_2 =JuniorOfficer('Ama', 20, 'J.O', '2000')
employee_3 =JuniorOfficer('May', 23, 'J.O', '2000')
employee_4 =JuniorOfficer('James', 21, 'J.O', '2000')
employee_5 =JuniorOfficer('Jacque', 20, 'J.O', '2000')

"""

# 3. Define a class Student with data members as rollno and name.
# Derive a class Fees from Student that has a data member fees and functions to submit fees
# and generate receipt.
# Derive another class Result from Student that displays the marks and grade obtained by the student.
"""
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
    
    grades = {'Subject_1' : 'A','Subject_2' : 'A','Subject_3' : 'A','Subject_4' : 'A','Subject_5' : 'A',}

class Fees(Student):
    def __init__(self, roll_no, name):
        super().__init__(roll_no, name)
        self.fees = 3532.59
        self.fees_owed = 3532.59

    def submit_fees(self):
        print(f'\nYou have a fees debt of Ghc {self.fees_owed.__round__(2)}')
        self.fees_paid = float(input('Enter the amount of fees paid: '))
        print('\n')
        Fees.generate_receipt(self)

    def generate_receipt(self):
        self.balance = self.fees_owed - self.fees_paid
        receipt_info = {'Roll Number': self.roll_no, 'Student Name': self.name, 'Amount of Fees': self.fees, 'Amount of fees owed' : self.fees_owed.__round__(2), 'Amount of Fees Paid': self.fees_paid, 'Balance': self.balance.__round__(2)}
        print('RECEIPT')
        for tag, info in receipt_info.items():
            print(f'{tag} : {info}')
        self.fees_owed = self.balance

class Result(Student):
    def __init__(self, roll_no, name):
        super().__init__(roll_no, name)

    def display_grades(self):
        print('\nRESULTS')
        for subject, grade in self.grades.items():
            print(f'{subject} : {grade}')
            

student1 = Fees('00001', 'Eve')
student1.submit_fees()
student1 = Result('00001', 'Ava').display_grades()

"""

# 4. Define a class Employee with data members as empno, name, and
# designation. Derive a class Qualification from Employee that has data
# members UG, PG, and experience. Create another class Salary which is derived
# from both these classes to display the details of the employee and compute their
# increments based on their experience and educational qualification.

# 5. Write a program that has a class Student to store the details of students in a
# class. Derive another class Toppers from the Student that stores records of
# only top three students of the class.

# 6. Write a program that has a class Person. Derive a class Baseball_Player
# from Person and display all the details of a famous baseball player.

# 7. Write a program that extends the class Shape to calculate the area of a circle and
# a cone. (Hint: To calculate area of a circle only one variable is required so when
# creating object, pass the other variable with value 1)

# 8. Write a program that extends the class Result so that the final result of the
# Student is evaluated based on the marks obtained in tests, activities, and
# sports.

# 9. Write a program that extends the Employee class so that it stores two more data
# members DOB and Date of Hiring. The Date must be defined as a separate
# class.

# 10. Write a program that has a class Train with data members – no_of_seats_1
# st, no_of_seats_ 2Tier, and no_of_seats_3Tier —and member
# functions to set and display data. Derive a class Reservation that has data
# members— seats_ booked_1 st, seats_booked_2Tier, and seats_
# booked_3Tier—, and functions to book and cancel tickets, and display status.

# 11. Write a program that has a class Distance with members-kms and metres.
# Derive classes School and Office which store the distance from your house
# to school and office along with other details.

# 12. Write a program that extends the class Employee. Derive a class Manager from
# Employee so that it lists all the details of the manager as well as the details of
# employees working under that manager.

# 13. Write a program for a publishing company that markets both printed books and
# audio-visual lectures stored on CDs. Write a class Publication that stores
# title and price. Derive a class Book which has an additional member as
# no_pages and a class Lecture with member play_time.