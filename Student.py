class Student:
    _roll_number = 0
    _student_name = ''
    _course_list = []

    def __init__(self, student_name, roll_number, course_list):
        self.roll_number = roll_number
        self.student_name = student_name
        self.course_list = course_list

    @property
    def roll_number(self):
        return self._roll_number

    @roll_number.setter
    def roll_number(self, roll_number):
        self._roll_number = roll_number

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, student_name):
        self._student_name = student_name

    @property
    def course_list(self):
        return self._course_list

    @course_list.setter
    def course_list(self, course_list):
        self._course_list = course_list
