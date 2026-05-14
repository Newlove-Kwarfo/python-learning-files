# 9-4. Number Served: Start with your program from Exercise 9-1 (restaurant.py).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a
# day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('This is retaurant is called {name} and it is a {type} restaurant'.format(name=self.name, type = self.type))
    
    def open_restairant(self):
        print(f'{self.name} restaurant is now open! Welcome!')

    def set_number_served(self, meals_served):
        self.number_served = meals_served

    def increment_number_served(self, food_served):
        self.number_served += food_served


    
restaurant = Restaurant('Chinatown', 'chinese')

# restaurant.number_served = 6
# print(restaurant.number_served)

# restaurant.set_number_served(54)
# print(restaurant.number_served)

restaurant.increment_number_served(90)
print(restaurant.number_served)
