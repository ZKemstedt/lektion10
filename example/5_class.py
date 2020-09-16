

class Lesson():
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def print_students(self):
        print("---------- List of students ----------")
        for student in self.students:
            print(f"* {student}")
        print(f"Total: {len(self.students)}\n")

    def find_by_first_name(self, name):
        return next(filter(lambda s: s if s.name == name else False, (self.students)))

    def remove_by_name(self, name):
        return self.remove_student(self.find_by_first_name(name))


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student - {self.name}"


# Create a Lesson instance for lession_10
lesson_10 = Lesson()

# add students
student_names = (("Rasmus", 43), ("Joel", 33), ("Noname", 100))
for name, age in student_names:
    lesson_10.add_student(Student(name, age))

# Print all students
lesson_10.print_students()

# Remove wrongful entry
lesson_10.remove_by_name("Noname")

# Print all students again
lesson_10.print_students()
