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

class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range =315
        print(f'This car can go about {range} miles on full charge.')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_desriptive_name())
# my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()