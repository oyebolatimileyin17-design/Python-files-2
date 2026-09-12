# Object Oriented Programming In Python
# Upper is a method in the print function acting on the object 
#of type string 
#Note that .upper works for strings and not integers because 
#To create your own class 
#A method is a function that goes into a class 
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        pass

