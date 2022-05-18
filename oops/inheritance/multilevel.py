def custom_input(label, _type = str):
    _input = None 

    while type(_input) != _type:
        try:
            _input = input(label)
            _input = _type(_input)
        except:
            print("Input must be", _type)
    return _input 

class Student:
    def __init__(self):
        self.name = None
        self.usn = None
        self.age = None

    def get_data(self):
        self.name = custom_input("Enter name: ")
        self.age = custom_input("Enter age: ", int)
        self.usn = custom_input("Enter USN: ")

class Derived1(Student):
    nSubjects = 5
    def __init__(self):
        super().__init__()
        self.sem = None
        self.subjects = list()

    def get_derived_data(self):
        super().get_data()
        self.sem = custom_input("Enter semester: ", int)
        
        for index in range(self.nSubjects):
            marks = custom_input(f"Enter subject-{index+1} marks: ", int)
            self.subjects.append(marks)

class Derived2(Derived1):
    def display_data(self):
        print(f"NAME: {self.name}\nAGE: {self.age}\nUSN: {self.usn}\nSEM: {self.sem}")
   
        print("Subject Details: ")
        for i,marks in enumerate(self.subjects):
            print(f"Subject-{i+1}: {marks}")

    def get_percentage(self):
        total = sum(self.subjects)

        return (total * 100) / 500

s1 = Derived2()

s1.get_derived_data()
s1.display_data()
print("Percentage: ", s1.get_percentage())
