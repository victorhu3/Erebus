from library import *
from abstractionLayer import *
#from distance import *
import math
import time

lidar = myRobot.getLidar("Hokuyo UTM-30LX")
lidar.enable(100)
lidar.enablePointCloud()
pointCloud = lidar.getPointCloud()

while myRobot.step(timeStep) != -1:
    pointCloud = lidar.getPointCloud()
    for point in pointCloud:
        if point.x != 0 or point.z != 0:
            file.write(str(point.x) + "," + str(point.z) + "\n")
    sleep(1000)

#reload world to close file
file.close()