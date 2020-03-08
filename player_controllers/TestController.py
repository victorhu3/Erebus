from abstractionLayer import *
from controller import Robot

myRobot = Robot()
robotMaxSpeed = 10

timeStep = 32

wheels = get_wheels(myRobot)
    
wheels[0].setPosition(50.0)
wheels[1].setPosition(50.0)

while myRobot.step(timeStep) != -1:
    wheels[0].setVelocity(10)
    wheels[1].setVelocity(10)