import main; import settings; from vpython import *

ball = sphere(pos=vector(0, 0, 0), radius=1, color=color.cyan)
while True:
    rate(60)