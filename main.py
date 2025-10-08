class Human:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def work(self):
        print(f"{self.name} is hardworking.")

    def walking(self):
        print(f"{self.name} is going to the lab.")

class Student(Human):
    def __init__(self, name, age, nationality, student_id, major):
        super().__init__(name, age, nationality)  # inherit base attributes
        self.student_id = student_id
        self.major = major

    def study(self):
        print(f"{self.name} is studying {self.major}.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")

class Teacher(Human):
    def __init__(self, name, age, nationality, subject, years_experience):
        super().__init__(name, age, nationality)
        self.subject = subject
        self.years_experience = years_experience

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_exam(self):
        print(f"{self.name} is grading exams.")
# Create objects
student = Student("John", 22, "English", "S123", "Software Engineering")
teacher = Teacher("Mr. Smith", 40, "American", "Computer Science", 15)

student.work()
teacher.walking()

student.study()
student.take_exam()

teacher.teach()
teacher.grade_exam()
