import main; import settings; from vpython import *

scene.width = 1920   # Default is 640
scene.height = 1080   # Default is 400
mercury = sphere(pos=vector(*main.PlanetPos[0]), radius=(600*1.6308e-5), color=color.red)
venus = sphere(pos=vector(*main.PlanetPos[1]), radius=(600*4.0453e-5), color=color.blue)
earth = sphere(pos=vector(*main.PlanetPos[2]), radius=(600*4.2588e-5), color=color.green)
mars = sphere(pos=vector(*main.PlanetPos[3]), radius=(600*2.2657e-5), color=color.purple)
jupiter = sphere(pos=vector(*main.PlanetPos[4]), radius=(300*4.6733e-4), color=color.red)
saturn = sphere(pos=vector(*main.PlanetPos[5]), radius=(300.*3.8926e-4), color=color.white)
uranus = sphere(pos=vector(*main.PlanetPos[6]), radius=(600*1.6953e-4), color=color.blue)
neptune = sphere(pos=vector(*main.PlanetPos[7]), radius=(400*1.6459e-4), color=color.red)
sun = sphere(pos=vector(*main.PlanetPos[8]), radius=(3*4.6505e-3), color=color.yellow)
scene.autoscale = False 
scene.camera.follow(mercury)

PlanetVar = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, sun]

while True:
    scene.camera.follow(None)
    main.PosUpdate()
    for i in range(len(PlanetVar)):
        PlanetVar[i].pos = vector(*main.PlanetPos[i])
    rate(settings.ups)


