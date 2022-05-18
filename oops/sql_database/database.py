import pymysql

def custom_input(label, _type = str):
    _input = None 

    while type(_input) != _type:
        try:
            _input = input(f"{label} : ")
            _input = _type(_input)
        except:
            print("Input must be", _type.__name__)
    return _input 

class EmployeeDatabase:
    def __init__(self, pymysql):
        print("Initializing Database...\n")

        self.db = pymysql.connect(
                    host="172.16.34.105",
                    user="mca063",
                    password="mca063",
                    database="mca063"
                )

        self.cursor = self.db.cursor()

    def drop_table_and_create(self):
        self.drop_table_if_exists()
        self.create_table()

    def drop_table_if_exists(self):
        print("Droping table employee...\n")
        sql = """
        DROP TABLE IF EXISTS employee
        """
        self.cursor.execute(sql)

    def create_table(self):
        print("Creating table employee...\n")
        sql = """
        CREATE TABLE employee(
            slno INTEGER PRIMARY KEY,
            name VARCHAR(30),
            address VARCHAR(200),
            emp_code VARCHAR(20),
            dob VARCHAR(10),
            age INTEGER,
            mobile VARCHAR(10),
            status VARCHAR(100),
            designation VARCHAR(100)
        );
        """
        self.cursor.execute(sql)

    def insert_employee(self, 
            slno, name, address, emp_code, dob, age,
            mobile, status, designation):
        sql = f"""
        INSERT INTO employee
            (slno, name, address, emp_code, dob, age, mobile, status, designation)
        VALUES ({slno}, {name}, {address}, {emp_code}, {dob}, {age}, {mobile}, {status}, {designation})

        """
        self.cursor.execute(sql)
        print("Successfully inserted employee...\n")
    
    def display(self):

        sql = """
        SELECT * FROM employee
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        if (len(rows) > 0):
            print("Displaying all Employees...\n")
        else:
            print("No employees added...\n")
        for index, row in enumerate(rows):
            slno, name, address, emp_code, dob, age, mobile, status, designation = row

            details = f"""Employee Number: {index + 1}
-----------------------
Sl no: {slno}
Name: {name}
Address: {address}
Employee code: {emp_code}
Age: {age}
Mobile: {mobile}
Status: {status}
Designation: {designation}
            """
            print(details)

    def delete(self, slno):
        sql = f"""
        DELETE FROM employee
        WHERE slno = {slno}
        """
        self.cursor.execute(sql)

        print(f"Successfully deleted employee with slno: {slno}...")
    
    def update_address(self, slno, address):
        sql = f"""
        UPDATE employee
        SET address = "{address}"
        WHERE slno = {slno}
        """
        self.cursor.execute(sql)
        self.save()
        print(f"Successfully updated address of employee with slno: {slno}...")

    def save(self):
        self.db.commit()

# Drive code
emp_db = EmployeeDatabase(pymysql)

while(True):
    print("""Options:
---------
1. Drop table and create new table
2. Insert
3. Update address
4. Delete
5. Display
6. Save
7. Save and Quit
8. Quit without saving
    """)

    choice = custom_input("Enter your choice", int)

    if (choice == 1):
        emp_db.drop_table_and_create()

    elif (choice == 2):
        slno = custom_input("Enter slno", int)
        name = custom_input("Enter name")
        address = custom_input("Enter address")
        emp_code = custom_input("Enter Employee code")
        dob = custom_input("Enter date of birth")
        age = custom_input("Enter age", int)
        mobile = custom_input("Enter mobile number")
        status = custom_input("Enter status")
        designation = custom_input("Enter designation")
   
        emp_db.insert_employee(slno, name, address, emp_code, dob, age,
            mobile, status, designation)

    elif (choice == 3):
        slno = custom_input("Enter slno", int)
        address = custom_input("Enter address")
        emp_db.update_address(slno, address)

    elif (choice == 4):
        slno = custom_input("Enter slno", int)
        emp_db.delete(slno)

    elif (choice == 5):
        emp_db.display()

    elif (choice == 6):
        emp_db.save()

    elif (choice == 7):
        emp_db.save()
        print("Database saved. Quitting...\n")
        break

    elif (choice == 8):
        print("Quitting...\n")
        break
    
    else:
        print("Invalid input")
