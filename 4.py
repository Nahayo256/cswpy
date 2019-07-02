#Make a class called Restaurant. The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type.

class restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title ()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.name +' serves the best '+ self.cuisine_type + ".")
    def open_restaurant(self):
        print(self.name + " is now open.")

restaurant = restaurant('kali Restaurant','italian food')

print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


#Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.