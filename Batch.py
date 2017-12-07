class Batch:

    def __init__(self, batch_id, courseName, facultyName, students):
        self.batch_id = batch_id
        self.courseName = courseName
        self.facultyName = facultyName
        self.students = students

    def __getattr__(self, item):
        return self.item


batch = Batch(0, 'je', 'vinay', 'vinay')
print(getattr(batch, 'courseName'))
