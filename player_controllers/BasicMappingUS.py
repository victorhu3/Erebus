from library import *
from abstractionLayer import *
from distance import *
import math
import time

initDist()
while myRobot.step(timeStep) != -1:
    getDist()
    for i in range(0, len(dist)):
        if dist[i] != 0:
            position[i][0] = math.cos(math.radians(sensorAngle[i])) * dist[i] + sensorPos[i][0]
            position[i][1] = math.sin(math.radians(sensorAngle[i])) * dist[i] + sensorPos[i][1]
            file.write(str(position[i][0]) + ", " + str(position[i][1]) + "\n")
    sleep(1000)
    

#reload world to close file
file.close()