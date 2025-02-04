class Person:
    def __init__(self,name):
        if not name:
            raise ValueError("name must be proveded")
        self.name = name

class Student(Person):
    def __init__(self,name,major):
        super().__init__(name)
        if major not in ["CSE", "Mech", "EEE", "AIDS", "CE", "IT"]:
            raise ValueError("Invalid Major")
        self.major = major

    def __str__(self):
        return f"[name : {self.name}, major : {self.major}]"

    @classmethod    
    def get(cls):
        name = input("Enter student name: ")
        major = input("Enter major: ")
        return cls(name,major) 
            
class Professor(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        if not subject:
            raise ValueError("subject must be proveded")
        self.subject = subject
    
    def __str__(self):
        return f"{self.name} is a professor in {self.subject}" 
    
    @classmethod    
    def get(cls):
        name = input("Enter professor name: ")
        subject = input("Enter subject: ")
        return cls(name,subject) 



def main():
    student = Student.get()
    print(student)
    prof = Professor.get()
    print(prof)
    
if __name__ == "__main__":
    main()