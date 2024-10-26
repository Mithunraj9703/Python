class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Average marks of ",self.name," is ",sum/3)

s1=Student("karan",[67,89,72])
s1.name="Mithun"
s1.average()