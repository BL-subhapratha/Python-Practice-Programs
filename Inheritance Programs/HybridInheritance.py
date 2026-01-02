class University:
    def __init__(self, u_name, location):
        self.u_name = u_name
        self.location = location
    def __str__(self):
        return f"University name is {self.u_name}, located at {self.location}"
    
class Course(University):
    def __init__(self, u_name, loc, c_name):
        University.__init__(self, u_name, loc)
        self.c_name = c_name
    
    def __str__(self):
        return University.__str__(self) + f" and has {self.c_name} course in the university.\n"
    
class Branch(University):
    def __init__(self, u_name, loc, b_name):
        University.__init__(self, u_name, loc)
        self.b_name = b_name

    def __str__(self):
        return University.__str__(self) + f" and the branch name is {self.b_name}.\n"
    
class Student(Branch, Course):
    def __init__(self, u_name, loc, b_name, c_name, s_name, s_dept, s_rolnum):
        Branch.__init__(self, u_name, loc, b_name)
        Course.__init__(self, u_name, loc, c_name)
        self.name = s_name
        self.dept = s_dept
        self.rollnumber = s_rolnum
    
    def __str__(self):
        return Branch.__str__(self) + f"\nStudent {self.name} is from {self.dept} with rollnumber {self.rollnumber} and is studying the {self.c_name} at {self.u_name}."

class Faculty(Branch):
    def __init__(self, u_name, loc, b_name, f_name, subject):
        Branch.__init__(self, u_name, loc, b_name)
        self.f_name = f_name
        self.subject = subject

    def __str__(self):
        return Branch.__str__(self) + f"{self.f_name} is a faculty in the {self.u_name} and teaches {self.subject}."

course = Course("SRM", "Chengalpattu", "CSE")
print(course)

branch = Branch("SRM", "Chenalpattu", "Valliammai College")
print(branch)

student = Student("SRM", "Chengalpattu", "Valliammai", "Computer Science", "Subha", "CSE", 1)
print(student)

faculty = Faculty("SRM", "Chengalpattu", "CSE", "Shruthi", "Computer Science")
print(faculty)