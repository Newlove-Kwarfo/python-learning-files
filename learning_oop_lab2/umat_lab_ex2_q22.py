# 20. Write a menu driven program to add or delete items from your inventory of stationary items.
# You can use a dictionary to store item and the brand.

class Stationary:
    def __init__(self):
        self.stationary = {}

    def display_items(self):
        print('\nSTATIONARY LIST')
        for key, value  in self.stationary.items():
            print(f'{key} - {value}')

    def add_items(self):
        count = int(input('How many items do you want to add?: '))
        for i in range(count):    
            new_item = input('Enter an item to add to your stationary list: ')
            brand = input('Enter brand for stationary above. Enter "None" if none: ')
            self.stationary[new_item] = brand

    def delete_items(self):
        count = int(input('How many items do you want to remove?: '))
        for i in range(count):    
            new_item = input('Enter an item to remove from your stationary list: ')
            self.stationary.pop(new_item)

items = Stationary()

while True:
    actions = ['1. Add items', '2. Delete items', '3. Display items', '4. Exit']
    for action in actions:
        print(action)
    chosen_action = int(input('Enter the number of the option you want to select: '))

    if chosen_action == 1:
        items.add_items()
    elif chosen_action == 2:
        items.delete_items()
    elif chosen_action == 3:
        items.display_items()
    elif chosen_action == 4:
        print('Goodbye!')
        break
    else:
        print('Invalid input')


"""
#Using list menthod
class Stationary:
    def __init__(self):
        self.stationary = []

    def display_items(self):
        print('\nSTATIONARY LIST')
        for items in self.stationary:
            print(items)

    def add_items(self):
        count = int(input('How many items do you want to add?: '))
        for i in range(count):    
            new_item = input('Enter an item to add to your stationary list: ')
            self.stationary.append(new_item)

    def delete_items(self):
        count = int(input('How many items do you want to remove?: '))
        for i in range(count):    
            new_item = input('Enter an item to remove from your stationary list: ')
            self.stationary.remove(new_item)

items = Stationary()

while True:
    actions = ['1. Add items', '2. Delete items', '3. Display items', '4. Exit']
    for action in actions:
        print(action)
    chosen_action = int(input('Enter the number of the option you want to select: '))

    if chosen_action == 1:
        items.add_items()
    elif chosen_action == 2:
        items.delete_items()
    elif chosen_action == 3:
        items.display_items()
    elif chosen_action == 4:
        print('Goodbye!')
        break
    else:
        print('Invalid input')

"""
