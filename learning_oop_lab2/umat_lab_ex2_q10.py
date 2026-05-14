# 10. Write a menu driven program to read, display, add, and subtract two time objects.

class Times:
    def __init__(self):
        self.t1h = 0
        self.t1m = 0
        self.t1s = 0
        self.t2h = 0
        self.t2m = 0
        self.t2s = 0

    def read(self):
        try: 
            time1 = input("Enter the first time: ")
            time2 = input("Enter the second time: ")
            time1_hour, time1_minute, time1_second = map(int, time1.split(':'))
            time2_hour, time2_minute, time2_second = map(int, time2.split(':'))
            
        except ValueError:
            print('Enter your values in the form "00:00:00"')
            time1 = input("Enter the first time: ")
            time2 = input("Enter the second time: ")
            time1_hour, time1_minute, time1_second = map(int, time1.split(':'))
            time2_hour, time2_minute, time2_second = map(int, time2.split(':'))

        self.t1h = time1_hour
        self.t1m = time1_minute
        self.t1s = time1_second
        self.t2h = time2_hour
        self.t2m = time2_minute
        self.t2s = time2_second

    def display(self):
        '''Displays the two times you want to work with'''
        print(f'\nFirst time = {self.t1h} hour {self.t1m} minutes {self.t1s} seconds\nSecond time = {self.t2h} hour {self.t2m} minutes {self.t2s} seconds\n')

    def add(self):
        second_result = self.t1s + self.t2s
        minute_result = self.t1m + self.t2m
        hour_result = self.t1h + self.t2h
        if second_result == 60:
            second_result = 0
            minute_result += 1
        elif second_result > 60:
            second_result -= 60
            minute_result += 1
        if minute_result == 60:
            minute_result = 0
            hour_result += 1
        elif minute_result > 60:
            minute_result -= 60
            hour_result += 1
        print(f'\n{self.t1h} hour {self.t1m} minutes {self.t1s} seconds +  {self.t2h} hour {self.t2m} minutes {self.t2s} seconds\n = {hour_result} hours  {minute_result} minutes {second_result} seconds\n')


    def subtract(self):
        hour_result = self.t1h - self.t2h
        minute_result = self.t1m - self.t2m
        second_result = self.t1s - self.t2s
        if second_result < 0:
            second_result = second_result + 60
            minute_result -= 1
        if minute_result < 0:
            minute_result = minute_result + 60
            hour_result -= 1
        if hour_result <= 0:
            hour_result = 0
        print(f'\n{self.t1h} hour {self.t1m} minutes {self.t1s} seconds -  {self.t2h} hour {self.t2m} minutes {self.t2s} seconds\n = {hour_result} hours  {minute_result} minutes {second_result} seconds\n')


times = Times()

print('\nWelcome, this is a program that can perform the following actions on times:')

while True:
        actions = ['0. Read (Enter your values here)','1. Display (Displays your distance)', '2. Add', '3. Subtract', '4. Exit']
        for action in actions:
            print(action)
        chosen_action = int(input('Enter a number to pick an option: '))


        if chosen_action == 0:
            times.read()
        elif chosen_action == 1:
            times.display()
        elif chosen_action == 2:
            times.add()
        elif chosen_action == 3:
            times.subtract()
        elif chosen_action == 5:
            times.read()
        elif chosen_action == 4:
            print('Goodbye!')
            break
        else:
            print('False input')

