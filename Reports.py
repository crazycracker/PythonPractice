class Reports:

    student_list = []
    faculty_list = []

    def get_student_by_roll_number(self, _roll_number):
        for x in self.student_list:
            if x.roll_number == _roll_number:
                return x
        return None

    def get_student_by_name(self, _name):
        for x in self.student_list:
            if x.student_name == _name:
                return x
        return None

    def get_student_by_batch_id(self, batch_id):
        for x in self.student_list:
            if x.batch_id == batch_id:
                return x
        return None

    def get_faculty_by_batch_id(self, batch_id):
        for x in self.faculty_list:
            if x.batch_id == batch_id:
                return x
        return None
