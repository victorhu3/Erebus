from abstractionLayer import *
from library import *

#NOTE: all distances in mm

'''
Dist from center of robot to center of front/back dist sensors 
Used for calculating dist of objects relative to center of robot
'''
frontCenter = 107.78
backCenter = 134.72

'''
Coordinates of each dist sensor relative to center of robot
In order of 16 dist sensors (start at front left, go clockwise)
Needed because distances measured by sensors are relative to sensor, not robot,
which is needed to find absolute position of walls

Calculated by assuming front and back sensors arranged in shape of ellipse
(x/a)^2 + (y/b)^2 = 1
Front:
    a = 126.68
    b = 190.5
Back:
    a = 171.03
    b = 100.53

x = (ab)/(sqrt(b^2 + a^2(tan(theta)^2)))
y = xtan(theta)
To calculate coordinates on ellipse based on angle

Add frontCenter and backCenter to y coordinates to account for gap between
dist sensor and center of robot
'''
sensorPos = [
[-190.5, 0], [-110.62, 92.82], [-83.05, 143.85], [-32.47, 184.14], #quadrant 2 sensors
[32.47, 184.14], [83.05, 143.85], [110.62, 92.82], [190.5, 0], #quadrant 1 sensors
[171.03, 0], [98.13, -82.34], [54.96, -95.2], [17.63, -99.99], #quadrant 4 sensors
[-17.63, -99.99], [-54.96, -95.2], [-98.13, -82.34], [-171.03, 0] #quadrant 3 sensors
]
sensorAngle = [180, 140, 120, 100, 80, 60, 40, 0, 0, -40, -60, -80, -100, -120, -140, -180]

def initDist():
    for i in range(0, 8):
        sensorPos[i][1] += frontCenter
    for i in range(8, 16):
        sensorPos[i][1] += backCenter

def getDist():
    for i in range(len(sensors)):
        dist[i] = sensors[i].getValue()
    
