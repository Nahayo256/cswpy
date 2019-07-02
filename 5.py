#Three Restaurants: Start with your class from Exercise 9-1. Create three
#different instances from the class, and call describe_restaurant() for each
#instance.

class restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title ()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.name +' serves the best '+ self.cuisine_type + ".")
    def open_restaurant(self):
        print(self.name + " is now open.")

a = restaurant('Medelin Restaurant','Mexican food')
a.describe_restaurant()

b = restaurant('Village Restaurant','Ugandan food')
b.describe_restaurant()

c = restaurant('KFC Restaurant','fast food')
c.describe_restaurant()