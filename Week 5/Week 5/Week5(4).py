#  Base Class 
class Person:
    # Person is the parent class
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}"


# Student Class 
# Student inherits from Person
class Student(Person):
    def __init__(self, student_id, name):
        # Call the constructor of Person
        super().__init__(student_id, name)
        self.student_id = student_id

    def display_student(self):
        return f"Student -> {self.display_info()}"


# Staff Class 
# Staff also inherits from Person
class Staff(Person):
    def __init__(self, staff_id, name, tax_num):
        super().__init__(staff_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_staff(self):
        return f"Staff -> {self.display_info()}, Tax Number: {self.tax_num}"


# General Staff Class
# General inherits from Staff (multi-level inheritance)
class General(Staff):
    def __init__(self, staff_id, name, tax_num, rate_of_pay):
        super().__init__(staff_id, name, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_general(self):
        return f"General Staff -> {self.display_staff()}, Rate of Pay: {self.rate_of_pay}"


# Academic Staff Class
# Academic also inherits from Staff
class Academic(Staff):
    def __init__(self, staff_id, name, tax_num, publications):
        super().__init__(staff_id, name, tax_num)
        self.publications = publications

    def display_academic(self):
        return f"Academic Staff -> {self.display_staff()}, Publications: {self.publications}"


# Main Program 
# Creating objects to test inheritance

student1 = Student(101, "Parul")
print(student1.display_student())

general_staff = General(201, "Neha", "TX123", 30)
print(general_staff.display_general())

academic_staff = Academic(301, "Dr Vansh", "TX999", 15)
print(academic_staff.display_academic())
