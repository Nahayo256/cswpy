class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

# class my_dog():
    # my_dog = Dog('willie', 6)
    # print("My dog's name is " + my_dog.name.title() + ".")
    # print("My dog is " + str(my_dog.age) + " years old.")
# class Dog():
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()