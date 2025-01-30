import student

while(True):
    student.add_student()
    quit = input("Add another? Y/N")
    if(quit.lower()=="n"):
        break

student.get_students()
student.display_students()
