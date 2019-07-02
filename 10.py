#An administrator is a special kind of user. Write a class called
#Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

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
        self.privileges = ['can delete posts', 'can reset passwords', 'can ban user']

    def show_privileges(self):
        print("\nPrivileges: ")
        for privilege in self.privileges:
            print("- " + privilege)

andy = Admin('andy','nahayo','naandy','naandy@gmail.com', 'Bujumbura')
andy.describe_user() 
andy.show_privileges()
