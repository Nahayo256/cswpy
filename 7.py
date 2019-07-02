#Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0.
#Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
#Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.

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

my_new_restaurant = Restaurant('kali Restaurant','italian food')

print(my_new_restaurant.name)
print(my_new_restaurant.cuisine_type)
my_new_restaurant.describe_restaurant()
my_new_restaurant.open_restaurant()
my_new_restaurant.number_served()
my_new_restaurant.increment_number_served(2)
my_new_restaurant.number_served()
