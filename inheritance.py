class Person: #base class, parent class, abstract class
    def __init__(self, name, id, age, interests):
        self.name = name
        self.id = id
        self.age = age
        self.interests = interests
    def display(self):
        print(self.name)
        print(self.id)
        print(self.age)
        print(self.interests)


class Student(Person): #derived class
    def __init__(self, a, b, c, d, x, y, z):
        Person.__init__(self, a, b, c, d)
        self.major = x
        self.gpa = y
        self.minor = z
        self.taking_courses = []

    def display(self):
        Person.display(self)
        print(self.major)
        print(self.gpa)
        print(self.minor)

class Faculty(Person): #derived class
    def __init__(self, a, b, c, d, x, y, z):
        Person.__init__(self, a, b, c, d)
        self.department = x
        self.designation = y
        self.salary = z
        self.courses_taught = []

#polymorphism
    def display(self, ss="", tt=""):
        Person.display(self)
        print(self.department)
        print(self.designation)
        print(self.salary)

        if ss!="":
            print(ss)
        if tt!="":
            print(tt)


s1 = Student("MJ", "111", "18", "Music", "CS", 3.9, "Cyb")
s1.display() #1st form of invoking the function
s1.display("USA") #2nd form
s1.display("USA", "AR") #3rd form


