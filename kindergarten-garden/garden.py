class StudentHasNoGreenThumbException(Exception):
    def __init__(self, value="Don't gives water to the plants."):
        super(StudentHasNoGreenThumbException, self).__init__()
        self.value = value

    def __repr__(self):
        return self.value


class Garden(object):
    """docstring for Garden"""
    def __init__(self, plants, students=['Alice', 'Bob', 'Charlie', 'David',
                                         'Eve', 'Fred', 'Ginny', 'Harriet',
                                         'Ileana', 'Joseph', 'Kincaid',
                                         'Larry', ]):
        super(Garden, self).__init__()
        self._plants = plants
        self.students = sorted(students)

    def plants(self, student):
        idx = self.students.index(student)
