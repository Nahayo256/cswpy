#Add an attribute called login_attempts to your User
#class from Exercise 9-3 (page 166)
#Write a method called increment_
#login_attempts() that increments the value of login_attempts by 1.

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
andy= User('andy','nahayo','naandy','naandy@gmail.com', 'Bujumbura')
andy.describe_user()
andy.greet_user()

print("\nMaking 3 login attempts...")
andy.increment_login_attempts()
andy.increment_login_attempts()
andy.increment_login_attempts()
print(" Login attempts: " + str (andy.login_attempts))

print("Resetting login attempts...")
andy.reset_login_attempts()
print(" Login_attempts: " + str(andy.login_attempts))

