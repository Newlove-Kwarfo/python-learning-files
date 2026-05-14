# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

class Users:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def describe_user(self):
        print(f"This user's first name is {self.fname} and the last name is {self.lname}")

    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}. Welcome!")

class Privileges:
    privileges = ['Can add post', 'Can delete post', 'Can be User', 'Can cancel user']

    def show_privileges(self):
        for privelege in self.privileges:
            print(privelege)

class  Admin(Users):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


user1 = Users('John', 'Doe')
admin1 = Admin('LOid', 'Forger')
admin1.privileges.show_privileges()