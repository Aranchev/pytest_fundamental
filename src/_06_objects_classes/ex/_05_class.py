import statistics

class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) <= 21:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        b = 0
        for i in self.grades:
            b += i
        return b / len(self.grades)

    def __repr__(self):
        avg = f"{self.get_average_grade():.2f}"
        students = ', '.join(self.students)
        return (
            f"The students in {self.name}: {students}. "
            f"Average grade: {avg}"
        )

