class Person:
    def show(self):
        print("I am a Person")
class Employee(Person):
    def show(self):
        print("I am an Employee")
emp=Employee()
emp.show()