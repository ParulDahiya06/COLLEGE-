name = "John Doe"
age = 28
skills = ["Python", "SQL", "Power BI"]
education = ("BSc Computer Science", 2020)
contact_details = {
    "email": "john.doe@example.com",
    "phone": "+64-21-123-4567",
    "city": "Auckland"
}
certifications = {"Azure", "AWS"}

print("Component          | Data Type   | Value")
print("-------------------------------------------------------")
print(f"Name              | String      | {name}")
print(f"Age               | Integer     | {age}")
print(f"Skills            | List        | {skills}")
print(f"Education         | Tuple       | {education}")
print(f"Contact Details   | Dictionary  | {contact_details}")
print(f"Certifications    | Set         | {certifications}")
