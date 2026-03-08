class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    
class Employee(Person):
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
    def get_employee_info(self):
        print(f"Employee ID: {self.employee_id}\nSalary: {self.salary}")

class Manager(Employee):
    def __init__(self, department):
        self.department = department
    def get_manager_info(self):
        print(f"Department: {self.department}")

n = Person("Vivek", 19)
x = Employee(1098, 50000)
z = Manager("Software Developer")
n.introduce()
x.get_employee_info()
z.get_manager_info()

