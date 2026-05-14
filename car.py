class Car:
    '''A somple attempt to respresent a car.'''
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f'{self.year} {self.make} {self.model} '
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's miliage"""
        print(f'This car has {self.odometer_reading} miles on it')

    #Modifying an Attribute’s Value Through a Method
    def update_odometer (self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer. Input a positive number")


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_desriptive_name())
# # my_new_car.odometer_reading = 45      #Modifying an Attribute’s Value Directly
# my_new_car.update_odometer(27)
# my_new_car.read_odometer()

my_used_car = Car('BMW', 's5', '2002')
print(my_used_car.get_desriptive_name())

my_used_car.update_odometer(900)
print(my_used_car.odometer_reading)

my_used_car.increment_odometer(200)
print(my_used_car.odometer_reading)

