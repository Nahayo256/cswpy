#An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title ()
        self.cuisine_type = cuisine_type
        self.served_numbering = 0
        self.set_number_served = 5
    def increment_number_served(self, customers_served):
        self.set_number_served += customers_served
    def number_served(self):
        print("This restaurent has " + str(self.set_number_served) + " customer served")
    def describe_restaurant(self):
        print(self.name +' serves the best '+ self.cuisine_type + ".")
    def open_restaurant(self):
        print(self.name + " is now open.")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type = 'ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors only: ")
        for flavor in self.flavors:
             print("- " + flavor.title())

ice_bite = IceCreamStand('The Ice Bite')
ice_bite.flavors = ['vanilla', 'chocolate', 'black cherry']
ice_bite.describe_restaurant()
ice_bite.show_flavors()

