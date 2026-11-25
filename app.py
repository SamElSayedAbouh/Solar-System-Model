import main; import settings; from vpython import *



# venus = sphere(pos=vector(*main.PlanetPos[0]), radius=(4.26349651 *10**-5), color=color.red)
# earth = sphere(pos=vector(*main.PlanetPos[2]), radius=(4.26349651 *10**-5), color=color.blue)
# venus = sphere(pos=vector(*main.PlanetPos[0]), radius=(4.26349651 *10**-5), color=color.red)
earth = sphere(pos=vector(0,0,0), radius=(1), color=color.blue)

a = vector(1,1,1)
while True:
    rate(settings.ups)

