class Employee:
    def __init__(self, name, address, pan, basic, tds, deduct, hra, da):
        self.name = name
        self.address = address
        self.pan = pan
        self.basic = basic
        self.tds = tds
        self.deduct = deduct
        self.hra = hra
        self.da = da
    
    def get_gross_pay(self):
        return self.basic + self.da

    def get_net_pay(self):
        return self.get_gross_pay() - self.deduct

    @classmethod
    def get_obj_by_prompt(cls):
        name = input("Enter name: ")
        address = input("Enter address: ")
        pan = input("Enter pan: ")
        basic = int(input("Enter basic (int): "))
        tds = int(input("Enter tds (int): "))
        deduct = int(input("Enter deductions (int): "))
        hra = int(input("Enter hra (int): "))
        da = int(input("Enter da (int): "))

        emp = cls(name, address, pan, basic, tds, deduct, hra, da)
        return emp
 
    def get_dict(self):
        dct = {
                "name": self.name,
                "address": self.address,
                "pan": self.pan,
                "basic": self.basic,
                "tds": self.tds,
                "deduct": self.deduct,
                "hra": self.hra,
                "da": self.da,
                }
        return dct

emp_lst = []
while(True):
    count = len(emp_lst) + 1
    option = input(f"\n\nDo you wish to add Employee {count} (y/n): ")
    if option == "n":
        break
    elif option == "y":
        emp = Employee.get_obj_by_prompt()
        emp_lst.append(emp)
        print(f"\nEmployee {count} created")
    else:
        print("Invalid input")

if len(emp_lst) > 0:
    print("\n\nDisplaying Employee Details")
    print("--------------------------------------------------------")
    for emp in emp_lst:
        dct = emp.get_dict()
        print("Employee Details:", dct)
        print(f"\nThe gross salary of {emp.name} is {emp.get_gross_pay()}")
        print(f"The net salary of {emp.name} is {emp.get_net_pay()}")
        print("--------------------------------------------------------")
else:
    print("No Employees added")
