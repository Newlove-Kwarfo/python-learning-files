# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('This is retaurant is called {name} and it is a {type} restaurant'.format(name=self.name, type = self.type))
    
    def open_restairant(self):
        print(f'{self.name} restaurant is now open! Welcome!')
    
# restaurant = Restaurant('Chinatown', 'chinese')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry']

    def show_flavors(self):
        for flavor in self.ice_cream_flavors:
            print(flavor)

stand1 = IceCreamStand('Cooler Side', 'Ice cream stand')
stand1.show_flavors()
