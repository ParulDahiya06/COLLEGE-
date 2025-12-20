# The outputs will be different if the Student class does not correctly initialize the _name attribute inherited from Person, and similar only when both classes set and use the same attribute consistently.

class Person:
    def __init__(self, name, address, age):
        self._name = name          # highlighted on right
        self.address = address
        self.age = age

    def greet(self):
        print("Greetings and felicitations from the maestro " + self._name)

class Student(Person):
    def __init__(self, name, address, age, student_id):
        # call parent __init__ to set _name, address, age
        super().__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
        print("Hi " + self._name)   # highlighted on left
# test 

p = Person("Alice", "123 Main St", 20)
s = Student("Alice", "123 Main St", 20, "S12345")

p.greet()   # Person greeting
s.greet()   # Student greeting
