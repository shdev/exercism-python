import functools


class PlanetError(Exception):
    pass


class SpaceAge(object):
    EARTHYEAR = 31557600
    PERIODS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132,
    }

    def __init__(self, age):
        self.seconds = age

    def on_planet(self, planet):
        if planet not in self.PERIODS:
            raise PlanetError(
                "{} is not a planet in the solar system.".format(planet))
        return round(self.seconds / self.PERIODS[planet] / self.EARTHYEAR, 2)

    def __getattr__(self, attr):
        try:
            planet = attr.split('_')[1]
        except IndexError:
            raise AttributeError("No such attribute '{}'".format(attr))
        return functools.partial(self.on_planet, planet=planet)
