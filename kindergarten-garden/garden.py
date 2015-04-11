class StudentHasNoGreenThumbException(Exception):
    def __init__(self, value="Don't gives water to the plants."):
        super(StudentHasNoGreenThumbException, self).__init__()
        self.value = value

    def __repr__(self):
        return self.value

plant_conversion = {
    'V': 'Violets',
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
}


class Garden(object):
    """docstring for Garden"""
    def __init__(self, plants, students=['Alice', 'Bob', 'Charlie', 'David',
                                         'Eve', 'Fred', 'Ginny', 'Harriet',
                                         'Ileana', 'Joseph', 'Kincaid',
                                         'Larry', ]):
        super(Garden, self).__init__()
        self._plants = plants.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        try:
            idx = self.students.index(student) * 2
            plant_abrevs = self._plants[0][idx:idx + 2] + \
                self._plants[1][idx:idx + 2]

            return [plant_conversion[p] for p in plant_abrevs]

        except ValueError:
            raise StudentHasNoGreenThumbException(student + 'was not allowed to work with plants.')
