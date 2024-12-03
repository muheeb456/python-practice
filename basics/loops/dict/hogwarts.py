students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin",
}

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")

students_data = [
    {"name": "Hermione", "house": "Griffindor","patronus": "otter"},
    {"name": "Harry", "house": "Griffindor","patronus": "Jack Russell terrier"},
    {"name": "Ron", "house": "Griffindor","patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin","patronus": None}
]

for student in students_data:
    print(student["name"], student["house"], student["patronus"], sep=", ")