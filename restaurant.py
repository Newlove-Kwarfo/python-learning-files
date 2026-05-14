# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print('This is retaurant is called {name} and it is a {type} restaurant'.format(name=self.name, type = self.type))
    
    def open_restairant(self):
        print(f'{self.name} restaurant is now open! Welcome!')
    
restaurant = Restaurant('Chinatown', 'chinese')
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restairant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
restaurant2 = Restaurant("Hyung's Place", 'Korean')
restaurant3 = Restaurant('Authentically Black', 'African')
restaurant4 = Restaurant('Perfecto', 'Latina')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()
