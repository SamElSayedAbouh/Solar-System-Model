import skyfield; from skyfield.api import load; import time; import numpy as np; import settings; from datetime import timedelta

ts = load.timescale()

planets = load("de440.bsp")


PlanetPos = np.zeros((9,3))
PlanetVel = np.zeros((9,3))

mercury = planets["MERCURY BARYCENTER"]
venus = planets["VENUS BARYCENTER"]
earth = planets["EARTH BARYCENTER"]
mars = planets["MARS BARYCENTER"]
jupiter = planets["JUPITER BARYCENTER"]
saturn = planets["SATURN BARYCENTER"]
uranus = planets["URANUS BARYCENTER"]
neptune = planets["NEPTUNE BARYCENTER"]
sun = planets["SUN"]

PlanetData = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, sun]
s=0
def PosUpdate ():
    global s
    s = s +10
    t = ts.now() + s
    if settings.update:
        for i in range(len(PlanetData)):
            if settings.barycentric == False :
                PlanetPos[i] = (PlanetData[i]-sun).at(t).position.au
            else:
                PlanetPos[i] = (PlanetData[i]).at(t).position.au
            print("in pos update")
            print(PlanetPos)




