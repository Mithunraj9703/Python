class Emp:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def show_details(self):
        print("Role = ",self.role)
        print("Department = ",self.dept)
        print("Salary = ",self.sal)

class Eng(Emp):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("accountant","Finance",30000)

    def show(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
        super().show_details()

e1=Eng("Mithun",24)
e1.show()
# e1.show_details()