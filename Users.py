# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class Users:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def describe_user(self):
        print(f"This user's first name is {self.fname} and the last name is {self.lname}")

    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}. Welcome!")

user1 = Users('John', 'Doe')
user2 = Users('Ama', 'Kwarteng')
user3 = Users('Kwaku', 'Mordecai')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
