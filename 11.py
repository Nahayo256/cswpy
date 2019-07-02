#Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title ()
        self.last_name = last_name.title ()
        self.username = username
        self.email = email
        self.location = location.title ()
        self.login_attempts = 0
    def describe_user(self):
        print('\n'+ self.first_name + ' ' + self.last_name)
        print('username: ' + self.username )
        print('email: ' + self.email )
        print('location: ' + self.location )
    def greet_user(self):
        print('\nwelcome '+ self.username + ".")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ['can delete posts', 'can reset passwords', 'can ban user']
    
    def show_privileges(self):
        print("\nPrivileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")

andy = Admin('andy','nahayo','naandy','naandy@gmail.com', 'Bujumbura')
andy.describe_user()

andy.privileges.show_privileges()

print("\nAdding privileges...")

andy.privileges.show_privileges()