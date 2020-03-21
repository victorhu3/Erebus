from controller import Robot
from abstractionLayer import *

myRobot = Robot()
robotMaxSpeed = 10

timeStep = 32

#get camera node
camera = get_camera(myRobot)
#get wheels list
wheels = get_wheels(myRobot)

collecting = False
startTime = 99999999999

file = open("../../../player_controllers/SensorData.csv", "w")

#get distance sensors
sensors = get_distance_sensors(myRobot, timeStep)

#mapping lists
dist = [0] * len(sensors)
position = [[0 for i in range(2)] for j in range(len(sensors))]
