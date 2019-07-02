#Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored
#in a user profile.

#Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.

class User():
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title ()
        self.last_name = last_name.title ()
        self.username = username
        self.email = email

    def describe_user(self):
        print('\n'+ self.first_name + ' ' + self.last_name)
        print('username: ' + self.username )
        print('email: ' + self.email )
    def greet_user(self):
        print('\nwelcome '+ self.username + ".")
andy= User('andy','nahayo','naandy','naandy@gmail.com')
andy.describe_user()
andy.greet_user()
#Create several instances representing different users, and call both methods
# for each user.

bella= User('bella','kaze','belkaz','belkaz@gmail.com')
bella.describe_user()
bella.greet_user()

nicole= User('nicole','eve','niev','niev@gmail.com')
nicole.describe_user()
nicole.greet_user()

john= User('john','cage','joca','joca@gmail.com')
john.describe_user()
john.greet_user()

