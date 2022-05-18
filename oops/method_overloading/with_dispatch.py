from multipledispatch import dispatch

class Person:
    def __init__(self, name):
        self.name = name

    @dispatch()
    def say_hello(self):
        print(f"My name is {self.name}")

    @dispatch(int)
    def say_hello(self, age):
        print(f"My name is {self.name}\nMy age is {age}")

    @dispatch(int, str)
    def say_hello(self, age, place):
        print(f"My name is {self.name}\nMy age is {age}\nI live in {place}")

p = Person("Raju")

print("\nWithout arguements")
p.say_hello()

print("\nWith 1 arguement")
p.say_hello(21)

print("\nWith 2 arguements")
p.say_hello(21, "Bangalore")
