class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
s1=Student("Preetha",25)
s2=Student("Sathish",27)
s1.display()
s2.display()