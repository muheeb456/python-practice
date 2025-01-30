students =[]

def get_students():
    with open("./student_records.txt") as file:
        for line in file:
            name , dept = line.rstrip().split(',')
            students.append({"name":name,"dept":dept})
    print("Stduents fetched successfully")

def add_student():
    with open("./student_records.txt","a") as file:
        name = input("Enter student name ")
        dept = input("Enter student dept ")
        file.write(f'{name},{dept}\n')
        print("Student added successfully")

def get_name(student):
    return student["name"]

def get_dept(student):
    return student["dept"]

def display_students(sortBy="name"):
    sort_key = get_name if sortBy=="name" else get_dept
    print(f"{"Student":10} Department")
    for student in sorted(students,key=sort_key):
        print(f'{student["name"]:10} {student["dept"]}')

            