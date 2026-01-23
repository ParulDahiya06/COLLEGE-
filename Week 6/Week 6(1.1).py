# StudentRecords class manages student details and scores
class StudentRecords:
    def __init__(self):
        # Dictionary to store student ID as key and student name as value
        self.students = {}

        # Dictionary to store student ID as key and MSE800 score as value
        self.mse800_scores = {}

    # Method to add a student
    def add_student(self, student_id, name, mse800_score):
        self.students[student_id] = name
        self.mse800_scores[student_id] = mse800_score

    # Method to display all students
    def display_students(self):
        print("Student Details and MSE800 Scores:\n")
        for student_id in self.students:
            print(
                f"ID: {student_id}, "
                f"Name: {self.students[student_id]}, "
                f"MSE800 Score: {self.mse800_scores[student_id]}"
            )


# ----- Main Program -----
# Create an object of the StudentRecords class
records = StudentRecords()

# Add five students
records.add_student("S001", "Aman", 85)
records.add_student("S002", "Rohit", 78)
records.add_student("S003", "Neha", 92)
records.add_student("S004", "Pooja", 88)
records.add_student("S005", "Karan", 81)

# Display stored data
records.display_students()

