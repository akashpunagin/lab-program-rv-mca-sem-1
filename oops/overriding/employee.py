class Employee():
    raise_amt = 1.04
    _type = "Employee"

    def __init__(self, first_name, last_name, emp_id, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_id = emp_id
        self.pay = pay

    def get_salary(self):
        return self.raise_amt * self.pay

    def print_details(self):
        print(f"\n{self._type} Details")
        print(f"-----------------------")
        print(f"Name\t\t{self.first_name} {self.last_name}")
        print(f"Employee Id\t{self.emp_id}")
        print(f"Basic Pay\t{self.pay}")
        print(f"Base Salary\t{self.get_salary()}")

class Developer(Employee):
    raise_amt = 1.05
    _type = "Developer"

    def __init__(self, first_name, last_name, emp_id, pay):
        super().__init__(first_name, last_name, emp_id, pay)

    def get_salary(self):
        return self.raise_amt * self.pay

class Manager(Employee):
    raise_amt = 1.06
    _type = "Manager"

    def __init__(self, first_name, last_name, emp_id, pay):
        super().__init__(first_name, last_name, emp_id, pay)

    def get_salary(self):
        return self.raise_amt * self.pay

employee = Employee("Raj", "Khan", 10, 1000)
employee.print_details()

developer = Developer("Kumar", "Khan", 11, 1000)
developer.print_details()

manager = Manager("Bhaskar", "Gowda", 12, 1000)
manager.print_details()

