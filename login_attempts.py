# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class Users:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"This user's first name is {self.fname} and the last name is {self.lname}")

    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}. Welcome!")

    def increment_login_attempts(self, login_attempts):
        self.login_attempts += login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0




user1 = Users('John', 'Doe')
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)