import sqlite3

# Step 1: Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Step 2: Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    score REAL NOT NULL
)
""")

# Step 3: Insert sample student data
students_data = [
    (1, "Aman", 85),
    (2, "Rohit", 92),
    (3, "Neha", 78),
    (4, "Pooja", 95),
    (5, "Karan", 88)
]

cursor.executemany("""
INSERT OR REPLACE INTO Student (student_id, student_name, score)
VALUES (?, ?, ?)
""", students_data)

conn.commit()

# Step 4: SQL Query to get top 3 students by score
cursor.execute("""
SELECT student_id, student_name, score
FROM Student
ORDER BY score DESC
LIMIT 3
""")

top_students = cursor.fetchall()

# Step 5: Display Results
print("Top 3 Students Based on Scores:")
print("---------------------------------")
for student in top_students:
    print(f"ID: {student[0]}, Name: {student[1]}, Score: {student[2]}")

# Close connection
conn.close()
