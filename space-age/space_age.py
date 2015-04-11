class SpaceAge(object):
    _sec_to_year = 60 * 60 * 24 * 365.25

    _earth_to_mercury = 0.2408467
    _earth_to_venus = 0.61519726
    _earth_to_mars = 1.8808158
    _earth_to_jupiter = 11.862615
    _earth_to_saturn = 29.447498
    _earth_to_uranus = 84.016846
    _earth_to_neptune = 164.79132

    def __init__(self, seconds):
        super(SpaceAge, self).__init__()
        self.seconds = seconds

    def _to_year(self):
        return self.seconds / self._sec_to_year

    def on_earth(self):
        return round(self._to_year(), 2)

    def on_mercury(self):
        return round(self._to_year() / self._earth_to_mercury, 2)

    def on_venus(self):
        return round(self._to_year() / self._earth_to_venus, 2)

    def on_mars(self):
        return round(self._to_year() / self._earth_to_mars, 2)

    def on_jupiter(self):
        return round(self._to_year() / self._earth_to_jupiter, 2)

    def on_saturn(self):
        return round(self._to_year() / self._earth_to_saturn, 2)

    def on_uranus(self):
        return round(self._to_year() / self._earth_to_uranus, 2)

    def on_neptune(self):
        return round(self._to_year() / self._earth_to_neptune, 2)
