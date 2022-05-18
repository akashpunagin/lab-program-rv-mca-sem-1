class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self, age=None, place=None):
        print(f"Hello! My name is {self.name}")
        if age:
            print(f"My age is {age}")
        if place:
            print(f"I live in {place}")     

p = Person("Raju")

print("\nCalling without age and name")
p.say_hello()

print("\nCalling with only age and not place")
p.say_hello(12)

print("\nCalling with age and place")
p.say_hello(12, "Bangalore")
