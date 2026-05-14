# 19. Write a program that uses a time structure within a class. Enter any time and your
# favourite show's time. The program must display how much time is left for it to start.

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

