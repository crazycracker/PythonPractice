class Faculty:
    faculty_name = ''
    batch_list = []
    course_list = []

    def __init__(self, faculty_name, batch_list, course_list):
        self.faculty_name = faculty_name
        self.batch_list = batch_list
        self.course_list = course_list

    def __add__batch(self, batch):
        self.batch_list.append(batch)

    def __add__course(self, course):
        self.course_list.append(course)
