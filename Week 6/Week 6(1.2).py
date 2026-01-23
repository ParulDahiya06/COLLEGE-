# StudentRecords class manages student details and scores
class StudentRecords:
    def __init__(self):
        # Dictionary: student_id -> student_name
        self.students = {}

        # Dictionary: student_id -> MSE800 score
        self.mse800_scores = {}

    # Method to add student data
    def add_student(self, student_id, name, mse800_score):
        self.students[student_id] = name
        self.mse800_scores[student_id] = mse800_score

    # Method to combine dictionaries and return passed students only
    def get_passed_students(self):
        # New dictionary: student_id -> (name, score)
        passed_students = {}

        for student_id in self.students:
            score = self.mse800_scores.get(student_id, 0)

            # Check pass condition
            if score >= 50:
                passed_students[student_id] = {
                    "name": self.students[student_id],
                    "score": score
                }

        return passed_students


# ----- Main Program -----
records = StudentRecords()

# Add five students
records.add_student("S001", "Aman", 85)
records.add_student("S002", "Rohit", 45)
records.add_student("S003", "Neha", 92)
records.add_student("S004", "Pooja", 38)
records.add_student("S005", "Karan", 71)

# Generate dictionary of passed students
passed = records.get_passed_students()

# Display passed students
print("Passed Students (Score ≥ 50):\n")
for student_id, details in passed.items():
    print(
        f"ID: {student_id}, "
        f"Name: {details['name']}, "
        f"MSE800 Score: {details['score']}"
    )
