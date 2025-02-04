class Person:
    def __init__(self,name):
        self.name = name    # calls @name.setter method automatically
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("name must be proveded")
        self._name = name


class Student(Person):
    def __init__(self,name,major):
        super().__init__(name)
        self.major = major

    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self,major):
        if major not in ["CSE", "Mech", "EEE", "AIDS", "CE", "IT"]:
            raise ValueError("Invalid Major")
        self._major = major
    
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
        self.subject = subject
    
    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self,subject):
        if not subject:
            raise ValueError("subject must be proveded")
        self._subject = subject

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