class Allergies(object):
    _allergie_items = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                       'tomatoes', 'chocolate', 'pollen', 'cats', ]

    def __init__(self, score):
        super(Allergies, self).__init__()
        self.score = score
        self.list = [self._allergie_items[idx]
                     for idx in xrange(0, len(self._allergie_items))
                     if self.score & 2 ** idx == 2 ** idx]

    def is_allergic_to(self, item):
        return item in self.list
