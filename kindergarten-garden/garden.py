class GardenError(Exception):
    def __init__(self, value):
        super(GardenError, self).__init__()
        self.value = value

    def __repr__(self):
        return self.value


class StudentHasNoGreenThumbException(GardenError):
    def __init__(self, value="Don't gives water to the plants."):
        super(StudentHasNoGreenThumbException, self).__init__(value)


class Garden(object):

    _plant_conversion = {
        'V': 'Violets',
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
    }

    def __init__(self, plants, students=['Alice', 'Bob', 'Charlie', 'David',
                                         'Eve', 'Fred', 'Ginny', 'Harriet',
                                         'Ileana', 'Joseph', 'Kincaid',
                                         'Larry', ]):
        super(Garden, self).__init__()
        self._plants = plants.splitlines()

        plant_abbrevs_set = set(self._plants[0] + self._plants[1])

        if not plant_abbrevs_set.issubset(self._plant_conversion.keys()):
            raise GardenError("Can't match plant abbreviation to name")

        self.students = sorted(students)

    def plants(self, student):
        try:
            idx = self.students.index(student) * 2
            plant_abbrevs = self._plants[0][idx:idx + 2] + \
                self._plants[1][idx:idx + 2]

            return [self._plant_conversion[p] for p in plant_abbrevs]

        except ValueError:
            raise StudentHasNoGreenThumbException(
                student + 'was not allowed to work with plants.')
