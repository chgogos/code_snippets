class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def how_many(cls):
        return cls.total_students


s1 = Student("Νίκος")
s2 = Student("Μαρία")

print("s1:", s1.name)
print("s2:", s2.name)
print("Πλήθος σπουδαστών:", Student.how_many())
print("Πλήθος σπουδαστών:", Student.total_students)
print("Πλήθος σπουδαστών:", s1.total_students)
print("Πλήθος σπουδαστών:", s1.__class__.total_students)
