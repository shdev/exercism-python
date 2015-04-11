class Luhn(object):
    def __init__(self, number):
        super(Luhn, self).__init__()
        self.number = number

    def is_valid(self):
        return self.checksum() == 0

    def addends(self):

        return_value = []

        number = str(self.number)

        odder = len(number) % 2

        for i in xrange(0, len(number)):
            j = int(number[i])
            if i % 2 == odder:
                j = j * 2
            if j > 9:
                j -= 9
            return_value += [j]

        return return_value

    def checksum(self):
        return sum(self.addends()) % 10

    @classmethod
    def create(cls, number):
        l = Luhn(number * 10)
        if l.checksum():
            return number * 10 + (10 - l.checksum())
        else:
            return number * 10
