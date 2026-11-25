import skyfield; from skyfield.api import load; import time; import numpy as np; import settings

ts = load.timescale()
t = ts.now()

planets = load("de440.bsp")


PlanetPos = np.zeros((8,3))
PlanetVel = np.zeros((8,3))

sun = planets["sun"]
mercury = planets["MERCURY BARYCENTER"]
venus = planets["VENUS BARYCENTER"]
earth = planets["EARTH BARYCENTER"]
mars = planets["MARS BARYCENTER"]
jupiter = planets["JUPITER BARYCENTER"]
saturn = planets["SATURN BARYCENTER"]
uranus = planets["URANUS BARYCENTER"]
neptune = planets["NEPTUNE BARYCENTER"]
PlanetData = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]


def PosUpdate ():
    while settings.update:
        for i in range(len(PlanetData)):
            if settings.barycentric:
                PlanetPos[i] = (PlanetData[i]-sun).at(t).position.au
            else:
                PlanetPos[i] = (PlanetData[i]).at(t).position.au





