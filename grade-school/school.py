from collections import defaultdict


class School(object):

    def __init__(self, name):
        super(School, self).__init__()
        self._name = name
        self.db = defaultdict(set)

    def add(self, student, grade):
        self.db[grade].add(student)

    def grade(self, query_grade):
        return self.db[query_grade]

    def sort(self):
        return [(grade, tuple(students))
                for grade, students in self.db.iteritems()]
