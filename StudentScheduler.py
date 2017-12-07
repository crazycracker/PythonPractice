class StudentScheduler:
    students = list()

    def __init__(self):
        pass

    def add_student(self, student):
        self.students.append(student)

    def show_all_details(self):
        for x in self.students:
            print("Roll Number %d and Student Name is %s" % (x.roll_number, x.student_name))
