from StudentScheduler import *
from Student import *


class Admin:
    scheduler = StudentScheduler()

    def __init__(self):
        pass

    def add_students(self, student_name, roll_number):
        students = Student(student_name, roll_number)
        Admin.scheduler.add_student(students)

    def show_all_student_details(self):
        Admin.scheduler.show_all_details()

