def custom_input(label, _type = str):
    _input = None 

    while type(_input) != _type:
        try:
            _input = input(label)
            _input = _type(_input)
        except:
            print("Input must be", str(_type).split("'")[1])
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

    def display_data(self):
        print(f"NAME: {self.name}\nAGE: {self.age}\nUSN: {self.usn}")

class PGStudent(Student):
    def __init__(self):
        super().__init__()
        self.sem = None
        self.fees = None
        self.stipend = None

    def get_pg_data(self):
        super().get_data()
        self.sem = custom_input("Enter semester: ", int)
        self.fees = custom_input("Enter fees: ", int)
        self.stipend = custom_input("Enter stipend: ", int)

    def display_pg_data(self):
        super().display_data()
        print(f"SEM: {self.sem}\nFEES: {self.fees}\nSTIPEND: {self.stipend}")

class UGStudent(Student):
    def __init__(self):
        super().__init__()
        self.sem = None
        self.fees = None
        self.stipend = None

    def get_ug_data(self):
        super().get_data()
        self.sem = custom_input("Enter semester: ", int)
        self.fees = custom_input("Enter fees: ", int)
        self.stipend = custom_input("Enter stipend: ", int)

    def display_ug_data(self):
        super().display_data()
        print(f"SEM: {self.sem}\nFEES: {self.fees}\nSTIPEND: {self.stipend}")

ug = UGStudent()
pg = PGStudent()

print("UG Student")
ug.get_ug_data()

print("\nPG Student")
pg.get_pg_data()

print("\nDetails of UG Student")
ug.display_ug_data()

print("\nDetails of PG Student")
pg.display_pg_data()
