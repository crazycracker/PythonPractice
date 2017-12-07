from Admin import *

count = int(input("Enter the number of students to be added\n"))
check = 0
admin = Admin()

while check < count:
    student_name = input("enter student name\n")
    roll_number = input("enter roll number of the student\n")
    admin.add_students(student_name, int(roll_number))
    check += 1

print("You have added following students\n")
admin.show_all_student_details()
del check
del count
del admin
